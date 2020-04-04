#!/usr/bin/env python3

import sys

"""Reads and sorts vertical words"""

def sorter(s):
   return s.lower()

def main():
   inp = [x.strip() for x in sys.stdin]
   words = ["" for i in range(len(inp[0]))]
   inp_str = "".join(inp)

   i = 0
   while i < len(inp_str):
      words[i % len(inp[0])] += inp_str[i]
      i += 1

   lst = sorted(words, key=sorter)
   run = len(lst[0])
   j = 0
   while j < run:
      out = ""
      for word in lst:
         out += word[j]

      print(out)
      j += 1

if __name__ == "__main__":
   main()
