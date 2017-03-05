#!/usr/local/bin/python3

import json
import sys

loopcount = 0

def process_list(obj, key, pad):
   listcount = 0
   for i in obj:
      print ("{} {} -> [{}]".format(pad, key, listcount))
      display_two(i)
      listcount += 1


def display_two(obj):
   global loopcount
   loopcount += 1
   leading = "->" * loopcount
   try:
      for key,val in obj.items():
         if isinstance(val,dict):
            print("{} {} ->".format(leading,key))
            display_two(val)
         elif isinstance(val, list):
            process_list(val, key, leading)
         else:
            print ('{} {} = {}'.format(leading,key,val ))
   except AttributeError:
      process_list( obj, "HEAD", leading)
   loopcount -= 1

with open(sys.argv[1], 'r') as f:
     data = json.load(f)
display_two(data)

