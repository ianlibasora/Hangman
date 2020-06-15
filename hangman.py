#!/usr/bin/env python3

# import os
from os import system, name, get_terminal_size
from random import randint

"""Hangman game"""

clear = lambda: system('cls' if name == 'nt' else 'clear')

def get_word(level):
   E = [
      "JOHN", "MARY", "CITY", "TOWN", "PEN", "WEB", "HELLO",
      "WORLD", "LINUX", "PARK", "TRAIN", "NAME", "PLAY", "OPEN"
   ]
   M = [
      "DRIMNAGH", "CASTLE", "CRUMLIN", "GAELIC", "LUNCH", "MATHS", "SCHOOL",
      "ENGLISH", "BIOLOGY", "PHYSICS", "PYTHON", "JAVA", "APPLE", "LEAVING"
   ]
   H = [
      "WALKINSTOWN", "UNIVERSITY", "COMPUTING", "SCIENCE", "GOVERNMENT", "JAVASCRIPT", "SECONDARY",
      "ADVENTURE", "OPERATING", "GITHUB", "STACKOVERFLOW", "AMAZON", "MICROSOFT", "CORONAVIRUS"
   ]
   dct = {"1": E, "2": M, "3": H}
   n = randint(0, 13)
   return dct[level][n]

def lst_update(lst, word, ltr):
   i = 0
   while i < len(word):
      if word[i] == ltr:
         lst[i] = word[i]
      i += 1
   return lst

# game operation
def game(word, box):
   clear()
   dct = {
      7: "\n" + box[2] + "--------\n" + ((box[2] + "|\n") * 6) +
      ((len(box[2]) - 5) * " ") + ("-" * 26) + "\n",
      6: "\n" + box[2] + "--------\n" + (box[2] + "|      |\n") +
      ((box[2] + "|\n") * 5) + ((len(box[2]) - 5) * " ") + ("-" * 26) + "\n",
      5: "\n" + box[2] + "--------\n" + (box[2] + "|      |\n") +
      (box[2] + "|      O\n") + ((box[2] + "|\n") * 4) +
      ((len(box[2]) - 5) * " ") + ("-" * 26) + "\n",
      4: "\n" + box[2] + "--------\n" + (box[2] + "|      |\n") +
      (box[2] + "|      O\n") + (box[2] + "|      |\n") +
      ((box[2] + "|\n") * 3) + ((len(box[2]) - 5) * " ") + ("-" * 26) + "\n",
      3: "\n" + box[2] + "--------\n" + (box[2] + "|      |\n") +
      (box[2] + "|      O\n") + (box[2] + "|      |\n") + box[2] + "|     /\n" +
      ((box[2] + "|\n") * 2) + ((len(box[2]) - 5) * " ") + ("-" * 26) + "\n",
      2: "\n" + box[2] + "--------\n" + (box[2] + "|      |\n") +
      (box[2] + "|      O\n") + (box[2] + "|      |\n") + box[2] + "|     / \\\n" +
      ((box[2] + "|\n") * 2) + ((len(box[2]) - 5) * " ") + ("-" * 26) + "\n",
      1: "\n" + box[2] + "--------\n" + (box[2] + "|      |\n") +
      (box[2] + "|     \\O\n") + (box[2] + "|      |\n") + box[2] + "|     / \\\n" +
      ((box[2] + "|\n") * 2) + ((len(box[2]) - 5) * " ") + ("-" * 26) + "\n",
      0: "\n" + box[2] + "--------\n" + (box[2] + "|      |\n") +
      (box[2] + "|     \\O/\n") + (box[2] + "|      |\n") + box[2] + "|     / \\\n" +
      ((box[2] + "|\n") * 2) + ((len(box[2]) - 5) * " ") + ("-" * 26) + "\n"
   }

   current = ["-" for x in word]
   fails = set()
   life = 7

   while life != 0:
      print(dct[life])
      print("{:^{}s} Lives Remaining: {}\n".format(" ".join(current), (box[0] - len(current)) // 2, life))
      print(box[2] + "Wrong guesses: {}\n".format(", ".join(fails)))

      check = False
      while check is False:
         guess = input("Your guess: ").upper()
         if guess.isalpha():
            check = True
         else:
            print("\nInvalid entry, try again")

      if guess in word:
         lst_update(current, word, guess)
         if "".join(current) == word:
            clear()
            print(dct[life])
            print("{:^{}s} Lives Remaining: {}\n".format(" ".join(current), (box[0] - len(current)) // 2, life))
            print(box[2] + "Wrong guesses: {}\n".format(", ".join(fails)))
            return True
      else:
         fails.add(guess)
         life -= 1

      clear()

   print(dct[life])
   print("{:^{}s} Lives Remaining: {}\n".format(" ".join(current), (box[0] - len(current)) // 2, life))
   print(box[2] + "Wrong guesses: {}\n".format(", ".join(fails)))
   return False

def main():
   clear()
   window_size = get_terminal_size()
   pad = " " * 19
   box = (window_size[0], window_size[1], " " * 10)

   # intro block
   print(pad + ("-" * (window_size[0] - (len(pad) * 2))) + pad)
   print(pad + "|{:^{}s}|".format("Hangman", window_size[0] - (len(pad) * 2) - 2) + pad)
   print(pad + "|{:^{}s}|".format("Game", window_size[0] - (len(pad) * 2) - 2) + pad)
   print(pad + "|{:^{}s}|".format(" ", window_size[0] - (len(pad) * 2) - 2) + pad)
   print(pad + "|{:^{}s}|".format("Version: 15.06.2020", window_size[0] - (len(pad) * 2) - 2) + pad)
   print(pad + "|{:^{}s}|".format("By Joseph Libasora", window_size[0] - (len(pad) * 2) - 2) + pad)
   print(pad + ("-" * (window_size[0] - (len(pad) * 2))) + pad + "\n")
   print(box[2] + "--------\n" + (box[2] + "|      |\n") +
      (box[2] + "|     \\O/\n") + (box[2] + "|      |\n") + box[2] + "|     / \\\n" +
      ((box[2] + "|\n") * 2) + ((len(box[2]) - 5) * " ") + ("-" * 32) + "\n")

   #wargame ref
   print("Would you like to play a game?")
   check = False
   while check is False:
      print("Pick difficulty level, 1 = Easy, 2 = Medium, 3 = Hard")
      level = input("Difficulty level: ")
      if level in ["1", "2", "3"]:
         check = True
      else:
         print("\nInvalid entry, try again")

   # game runtime management
   play = True
   while play is True:
      word = get_word(level)
      if game(word, box):
         print("Congratulations, you win\n")
      else:
         print("Too bad, the word was: " + word + ", you lose\n")

      print("Would you like to play again?")
      check = False
      while check is False:
         tmp = input("Play again?: [y/n] ").lower()
         if tmp == "n":
            play = False
            check = True
         elif tmp == "y":
            clear()
            check = True
         else:
            print("\nInvalid entry, try again")

if __name__ == "__main__":
   main()
