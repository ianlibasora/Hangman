#!/usr/bin/env python

import sys
import os

def add(x, y):
   out = x + y
   return out

def minus(x, y):
   out = x - y
   return out

def multiply(x, y):
   out = x * y
   return out

def divide(x, y):
   out = x / y
   return out
   #note: "//"" returns the floor func

def power(x, y):
   out = x ** y
   return out

#allow for multiple arguments?
#--> use % 3 to check if length is ok
#iterate through lst

box = "------------------------------------------------------\n"
print(box)
print(" * Input 2 numbers, separated by operator\n")
print(" *  Input operator of choice in block letters\n")
print(" - Ex. 2 ADD 4\n")
print(" * Calculation will follow BIMDAS **N/A**\n")
print(" *** Terms to use: ***\n")
print(" - ADD                      - MINUS\n")
print(" - MULTIPLY                 - DIVIDE\n")
print(" - POWER                    - N/A\n")
print(box)

inp = sys.stdin.readline()
inp = inp.split()

if len(inp) % 3 == 0:
   x = float(inp[0].strip())
   op = str(inp[1].strip())
   y = float(inp[2].strip())

   print("\n  **  Answer:  **\n")
   if op == "ADD":
      print(add(x, y))
   elif op == "MINUS":
      print(minus(x, y))
   elif op == "MULTIPLY":
      print(multiply(x, y))
   elif op == "DIVIDE":
      print(divide(x, y))
   elif op == "POWER":
      print(power(x, y))
else:
   print(box)
   print("Invalid input\n")
