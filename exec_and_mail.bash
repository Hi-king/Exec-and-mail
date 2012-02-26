#!/bin/bash

Document='
=======================================
 exec_ and mail.bash
--------------------------------------
 execute $command and mail to $toaddr
---------------------------------------
 arguments
     |- $command
 output
     |- gnuplot in X-window
 options
     |-  -t $toaddr
---------------------------------------
dependent
---------------------------------------
 example
     |- hiking_exec_and_mail.bash less hoge.out
     |- hiking_exec_and_mail.bash -t hoge@gmail.com python hoge.py
=======================================
'

CONFIGFILE=".execandmailconf"
PYSCRIPTFILE="simplemail.py"

## --- default --- ##
cat $CONFIGFILE|while read line;do
if [ -z "$line" ];then
    continue
elif [ $(echo $line|cut -c 1) = "#" ];then
    continue
else
    echo "${line%%=*}=\"${line##*=}\"">...conf
fi 
done
eval $(cat ...conf)
rm ...conf
echo $DEFAULTTOADDR
toaddr=$DEFAULTTOADDR

PYSCRIPT=${0%/*}/$PYSCRIPTFILE

  # -------
  #  input
  # -------
  while getopts t OPT
  do
     case $OPT in
         "t")
            shift 1
            toaddr=$1
            shift 1
            ;;
     esac
  done

  # --- arguments ---
  if [ $# -lt 1 ];then
     echo "$Document"
     exit 1
  fi
  exec_command=$*  

# ------
#  exec
# ------
echo $exec_command
export out="hogehoge"
$exec_command|tee ...temp

if [ `cat ...temp|wc -l` -gt 55 ];then
    $PYSCRIPT $toaddr  "\"$(less -N ...temp|head -5)$(less -N ...temp|tail -50)\""  "\"$exec_command\""
else
    $PYSCRIPT $toaddr  "\"$(cat ...temp)\""  "\"$exec_command\""
fi
rm ...temp