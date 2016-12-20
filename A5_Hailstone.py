#  File: Hailstone.py

#  Description: In this program I will verify the conjecture of the hailstone sequence in a user defined range

#  Student Name: Orlando Reategui

#  Student UT EID: or3562

#  Course Name: CS 303E

#  Unique Number: 51635

#  Date Created: 2/28/2015

#  Date Last Modified: 2/28/2015

def main():
  # We give start and end false values at first to begin prompting the user.
  start = -5
  end = -1
  #while start or end are negative or the starting number is greater than the ending number we keep prompting the user
  while (start) < 0 or (end) < 0 or (start) > (end):
  #Prompt the user to enter the starting and ending value
      start = eval(input("Enter starting number of the range: "))
      end = eval(input("Enter ending number of the range: "))
#We tell python that we have an empty list at first. This list will store all the cycles for each number in the defined range
  list = []
  
##Begin nested loops
#We use a for loop to repeat the while loop from start to end. For each occurrence we store the final cycle value in a list
  for num in range(start, end + 1):
    cycle = 0
  #The while loop is used determine how many cycles a number has.
    while num > 1:
  #If the number is even then num // 2. Then add one to the cycle
      if (num % 2) == 0:
        num = num // 2
        cycle = cycle + 1
  #If the number is odd then 3 * num + 1. Then add one to the cycle
      if (num % 2) == 1 and num != 1:
        num = 3 * num + 1
        cycle = cycle + 1
#We store the final cycle in a list
    list.append(cycle)
  
#Look in the list for the maximum value of cycles
  cycleLength = max(list)

#The number is the position of the number with the highest value in the list. Add one because index starts at 0
#If there are two or more numbers that have the same largest cycle length, then print only the last number. 
  number  = max((x, i) for i, x in enumerate(list))[1] + 1

#Print out the results to the console
  print("The number", number, "has the longest cycle length of", str(cycleLength) + ".")

main()