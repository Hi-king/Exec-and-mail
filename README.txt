=====================================
 exec_and_mail.bash
-------------------------------------
 Execute command and mail the result
-------------------------------------
USAGE
  arguments
      |- $command
  options
      |-  -t $toaddr
-------------------------------------
SETUP
  1. put 3files(exec_and_mail.bash, simplemail.py, .execandmailconf) to executable directory
  2. write your own config to .execandmailconf
-------------------------------------
DEPENDENT
  python2.x
  bash
-------------------------------------
example
     |- hiking_exec_and_mail.bash less hoge.out
     |- hiking_exec_and_mail.bash -t hoge@gmail.com python hoge.py
=====================================
