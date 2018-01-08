#!/usr/bin/env python3

import sys
import time
from datetime import datetime

def since(time_a):
  return abs(time_a - datetime.now()).seconds


if __name__ == "__main__":
  interval = .1
  lines = ""
  carry_on = True
  time_a = datetime.now()
  in_stream = sys.stdin
  while carry_on:
    cur_line = in_stream.readline()
    if since(time_a) > 10 * interval:
      time_a = datetime.now()
      print("new file")
    print(cur_line)
    time.sleep(interval)
    if cur_line == "":
      carry_on = False
