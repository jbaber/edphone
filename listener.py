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
  counter = 1
  while carry_on:
    if since(time_a) > 10 * interval:
        print("Outputting file")
        with open("{0:03}".format(counter), "w") as f:
          f.write(lines)
        lines = ""
        counter += 1
        time_a = datetime.now()
      else:
        lines += new_char
    time.sleep(interval)
