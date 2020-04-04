#!/usr/bin/env python3

import sys

"""Flood fill algor"""

class List(object):
   def __init__(self):
      self.lst = set()

   def add(self, other):
      self.lst.add(other)

   def isin(self, other):
      tmp = set()
      tmp.add((other[0], other[1]))
      return tmp.issubset(self.lst)

def filler(lst, y, x, box, seen):
   ymax, xmax = box
   try:
      if (lst[y][x] != "-"):
         return
   except IndexError:
      return

   if (y < 0) or (x < 0) or (x >= xmax) or (y >= ymax):
      return

   lst[y][x] = "#"
   seen.add((y, x))

   n, s, e, w = (y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)
   if True or seen.isin(e) is False:
      seen.add(e)
      filler(lst, e[0], e[1], box, seen)
   if True or seen.isin(w) is False:
      seen.add(w)
      filler(lst, w[0], w[1], box, seen)
   if True or seen.isin(s) is False:
      seen.add(s)
      filler(lst, s[0], s[1], box, seen)
   if True or seen.isin(n) is False:
      seen.add(n)
      filler(lst, n[0], n[1], box, seen)

def step(lst, box, seen):
   total = 0

   y = 0
   while y < len(lst):
      cur_y = lst[y]
      x = 0
      while x < len(cur_y):
         if cur_y[x] == "-":
            filler(lst, y, x, box, seen)
            total += 1
         x += 1
      y += 1

   return total

def main():
   tmp = sys.stdin.readline().strip().split()
   box = (int(tmp[0]), int(tmp[1]))
   lst = [list(x.strip()) for x in sys.stdin]
   seen = List()
   sys.setrecursionlimit(10100)
   print(step(lst, box, seen))

if __name__ == '__main__':
   main()
