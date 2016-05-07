#! /usr/bin/python

import thread
import time
import sys
from subprocess import Popen, PIPE
import json

delay = 1
r_ns = 'test'
r_set = 'queues'

if len(sys.argv) < 4:
  print 'Usage: messenger.py LOCAL REMOTE MESSAGE'
  exit(1)

local = sys.argv[1]
remote = sys.argv[2]
message = sys.argv[3]

if not local :
  print 'LOCAL required'
  exit(1)

if not remote :
  print 'REMOTE required'
  exit(1)

if not message :
  print 'MESSAGE required'
  exit(1)

send_count = 1
send_queue = '{0}:{1}'.format(local, remote)
recv_queue = '{0}:{1}'.format(remote, local)

def init():
  print '==================================='
  print '>> received'
  print '<< sent'
  print '==================================='
  p = Popen(["/usr/bin/ascli", "udf-record-apply", r_ns, r_set, recv_queue, 'mqueue', 'init', local, remote], stdin=PIPE, stdout=PIPE)
  p = Popen(["/usr/bin/ascli", "udf-record-apply", r_ns, r_set, send_queue, 'mqueue', 'init', remote, local], stdin=PIPE, stdout=PIPE)

def recv():
  while 1:
    p = Popen(["/usr/bin/ascli", "udf-record-apply", r_ns, r_set, recv_queue, 'mqueue', 'receive'], stdin=PIPE, stdout=PIPE)
    output = p.stdout.read()
    messages = json.loads(output)
    if len(messages) > 0 :
      for message in messages:
        print ">> {0}".format(message)
      send()

def send():
  global send_count
  msg = "{0} ({1})".format(message, send_count)
  print "<< {0}".format(msg)
  send_count += 1
  p = Popen(["/usr/bin/ascli", "udf-record-apply", r_ns, r_set, send_queue, 'mqueue', 'send', msg], stdin=PIPE, stdout=PIPE)
  time.sleep(delay)

try:
  init()
  send()
  recv()
except:
  print "Good Bye"
