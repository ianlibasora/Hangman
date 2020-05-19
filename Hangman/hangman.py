#!/usr/bin/env python3

import os
import random

"""Hangman game"""

def get_word(level):
   E = [
      "JOHN", "MARY", "CITY", "TOWN",
      "WORLD", "LINUX", "PARK", "TRAIN"
   ]
   M = [
      "DRIMNAGH", "CASTLE", "CRUMLIN", "GAELIC",
      "ENGLISH", "BIOLOGY", "PHYSICS", "PYTHON"
   ]
   H = [
      "WALKINSTOWN", "UNIVERSITY", "COMPUTING", "SCIENCE",
      "ADVENTURE", "OPERATING", "GITHUB", "STACKOVERFLOW"
   ]
   dct = {"1": E, "2": M, "3": H}
   n = random.randint(0, 7)

   return dct[level][n]

def main():
   print("----------------Hangman game----------------\nby Joseph Libasora\n\n")

   print("Pick difficulty level, 1 = Easy, 2 = Medium, 3 = Hard")
   level = input("Difficulty level: ")

   print(get_word(level))


   clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

   # inp = input("Clear?: [y/n] ")
   # if inp == "y":
   #    clear()
   #    print("Clear occured")
   # else:
   #    print("Clear pass")


if __name__ == "__main__":
   main()
