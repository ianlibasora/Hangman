#!/usr/bin/env python3

import os
import random

"""Hangman game"""

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def get_word(level):
   E = [
      "JOHN", "MARY", "CITY", "TOWN", "PEN",
      "WORLD", "LINUX", "PARK", "TRAIN"
   ]
   M = [
      "DRIMNAGH", "CASTLE", "CRUMLIN", "GAELIC", "LUNCH",
      "ENGLISH", "BIOLOGY", "PHYSICS", "PYTHON"
   ]
   H = [
      "WALKINSTOWN", "UNIVERSITY", "COMPUTING", "SCIENCE", "GOVERNMENT",
      "ADVENTURE", "OPERATING", "GITHUB", "STACKOVERFLOW"
   ]
   dct = {"1": E, "2": M, "3": H}
   n = random.randint(0, 8)
   return dct[level][n]

def game(word, box):
   clear()
   dct = {
      8: "\n" + box[2] + "-------\n" + ((box[2] + "|\n") * 6) +
      ((len(box[2]) - 5) * " ") + "--------------------------------\n",
      7: box[2],
      6: box[2],
      5: box[2],
      4: box[2],
      3: box[2],
      2: box[2],
      1: box[2],
      0: box[2]
   }
   print(dct[8])

   life = 8
   while life != 0:

      life -= 1

   return False


def main():
   clear()
   window_size = os.get_terminal_size()
   pad = " " * 19
   box = (window_size[0], window_size[1], pad)


   # intro block
   print(pad + ("-" * (window_size[0] - (len(pad) * 2))) + pad)
   print(pad + "|{:^{}s}|".format("Hangman", window_size[0] - (len(pad) * 2) - 2) + pad)
   print(pad + "|{:^{}s}|".format("Game", window_size[0] - (len(pad) * 2) - 2) + pad)
   print(pad + "|{:^{}s}|".format(" ", window_size[0] - (len(pad) * 2) - 2) + pad)
   print(pad + "|{:^{}s}|".format("Version: 19.05.2020", window_size[0] - (len(pad) * 2) - 2) + pad)
   print(pad + "|{:^{}s}|".format("By Joseph Libasora", window_size[0] - (len(pad) * 2) - 2) + pad)
   print(pad + ("-" * (window_size[0] - (len(pad) * 2))) + pad + "\n")


   play = True
   while play is True:

      check = False
      while check is False:
         print("Pick difficulty level, 1 = Easy, 2 = Medium, 3 = Hard")
         level = input("Difficulty level: ")
         if level in ["1", "2", "3"]:
            check = True
         else:
            print("\nTry again, improper difficulty")


      if game(get_word(level), box) is True:
         print("\nCongratulations, you win\n")
      else:
         print("\nYou lose\n")


      check = False
      print("Would you like to play again?")
      while check is False:
         tmp = input("Play again?: [y/n] ").lower()
         if tmp == "n":
            play = False
            check = True
         elif tmp == "y":
            clear()
            check = True
         else:
            print("\nError, invalid response")

if __name__ == "__main__":
   main()
