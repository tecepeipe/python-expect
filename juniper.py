#!/usr/bin/python2
import pexpect,sys,time,getpass

username = 'fsiadmfl'
#password = 'xxx'
password = getpass.getpass('password:')
devices_file = open ('routers.txt', 'r')
devices = devices_file.read().splitlines()
#host = '192.168.16.90'
for host in devices:
  ssh = 'ssh ' + username + '@' + host + ' -o \"StrictHostKeyChecking=no\"'
  print 'Working on: ' + host
  logfile =  open ('output/' + host + '.txt', 'wb')
  child = pexpect.spawn (ssh)
  #child.logfile = sys.stdout
  child.expect('Password:')
  time.sleep (0.3)
  child.sendline(password)
  child.logfile = logfile
  child.expect('>')
  time.sleep (2)
  child.sendline('show virtual-chassis')
  time.sleep (1)
  child.expect('>')
  child.sendline('exit')
