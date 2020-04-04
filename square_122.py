#!/usr/bin/env python3

import sys
import math

"""Finds the missing vertex of a square"""

def m_point(p1, p2):
   x1, y1 = p1[0], p1[1]
   x2, y2 = p2[0], p2[1]

   out = (((x1 + x2) / 2), ((y1 + y2) / 2))
   return out

def dist(p1, p2):
   x1, y1 = p1[0], p1[1]
   x2, y2 = p2[0], p2[1]

   out = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
   return out

def square(inp):
   pts = []
   for x in inp:
      x = x.strip().split()
      l = int(x[0])
      r = int(x[1])
      pts.append((l, r))

   h1 = dist(pts[0], pts[1])
   h2 = dist(pts[0], pts[2])
   h3 = dist(pts[1], pts[2])
   if (h1 >= h2) and (h1 >= h3):
      hypo = h1
      p1, p2, p3 = pts[0], pts[1], pts[2]
   elif (h2 >= h1) and (h2 >= h3):
      hypo = h2
      p1, p2, p3 = pts[0], pts[2], pts[1]
   else:
      hypo = h3
      p1, p2, p3 = pts[1], pts[2], pts[0]

   mid = m_point(p1, p2)
   out = [0, 0]
   x_out = (2 * mid[0]) - p3[0]
   y_out = (2 * mid[1]) - p3[1]
   x_out = math.ceil(x_out)
   y_out = math.ceil(y_out)

   out[0] = str(x_out)
   out[1] = str(y_out)
   out = " ".join(out)
   return out

def main():
   inp = sys.stdin.readlines()
   print(square(inp))

if __name__ == "__main__":
   main()
