# File: Deal.py

# Description: This code simulates the Let's Make a Deal game show and proves that switching doors increases the chances of winning.

# Student Name: Orlando Reategui

# Student UT EID: or3562

# Course Name: CS 303E

# Unique Number: 51635

# Date Created: 2/21/2015

# Date Last Modified: 2/21/2015
def main():

#Import random library to use with the doors
import random

#Prompt the user how many rounds to play
rounds = eval(input("Enter the number of times you want to play:"))

#Header row of the table displaying prize, guess, view, and new guess
print("  Prize      Guess       View    New Guess")

#Initiate the number of wins and count variables
wins = 0
count = 0

##Initiate parent loop that will start a new round and print the results as long as it's below the rounds specified by the user.
while (count < rounds):

#Give the price and initial guess random selections like in a real game show
  prize = random.randint(1,3)
  guess = random.randint(1,3)
  
#Loop to determine what door is opened by Monty Hall
  view = 1
  while (view == prize) or (view == guess):
    view += 1
    
#Loop to determine what door the contestant switched to
  newGuess = 1
  while (newGuess == guess) or (newGuess == view):
    newGuess += 1
    
#Determine whether switching was a winning result. If it was, increase the winning number by one
  if newGuess == prize:
    wins += + 1
    
#Print the prize, guess, view, and newGuess row
  print("   ",prize,"        ",guess,"        ",view,"        ",newGuess) 
  count += 1
  
#Print the probability of wins by switching and not switching
print("Probability of winning if you switch =", round((wins / rounds),2))
print("Probability of winning if you do not switch =", round(1 - (wins / rounds),2))

main()