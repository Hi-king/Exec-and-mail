#!/usr/bin/python
# -*- coding:utf-8 -*-
DOC='''
===========================================
 simplemail.py
-------------------------------------------
 arguments
    |- to-address
    |- (message)
        |- default: "no message"
    |- (SUBJECT)
        |- default: "from python"
 output
    |- e-mail from ogaki@iis.u-tokyo.ac.jp
-------------------------------------------
 author: K.ogaki
 mail: ogaki@ut-vision.org
===========================================
'''
CONFIGFILE=".execandmailconf"

import sys
import smtplib
from email.mime.text import MIMEText

def confread(filename):
    try:
        f_read = open(filename)
    except:
        print("fatal error: %s cannot open" % filename)
        exit(1)
    else:
        for line in f_read:
            if(line[0]=="#" or line[0]=="\n"):
                continue
            else:
                lines=tuple( line.rstrip().split("=") )
                #print lines
                exec ('global %s \n%s = "%s"' % (lines[0], lines[0], lines[1]))

if __name__ == '__main__':
    #MYADDR, DEFAULTSUBJECT, DEFAULTMESSAGE, SERVER, PORT, FROMADDR, USERNAME, PASSWORD
    confread(CONFIGFILE)
    subject = DEFAULTSUBJECT
    msg =DEFAULTMESSAGE

    ## === read args === ##
    if(len(sys.argv) >= 2):
        toaddr = sys.argv[1]
    else:
        print DOC
        exit(1)
    if(len(sys.argv) >=3):
        msg = sys.argv[2]
    if(len(sys.argv) >=4):
        subject = sys.argv[3]
  
    ## === main === ##
    msg=MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = FROMADDR
    msg['To'] = toaddr
  
    s=smtplib.SMTP(SERVER, PORT, USERNAME)
    #s.set_debuglevel(True)
    s.ehlo()
    s.starttls()
    s.ehlo()
  
    s.login(USERNAME, PASSWORD) #user, pass
    
    print FROMADDR, toaddr
    s.sendmail(FROMADDR, toaddr, msg.as_string())
    s.close()
