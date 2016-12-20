#  File: Day.py

#  Description: Print out the day of the week for that date

#  Student Name: Orlando Reategui

#  Student UT EID: or3562

#  Course Name: CS 303E

#  Unique Number: 51635

#  Date Created: 2/14/2015

#  Date Last Modified: 2/14/2015

def main():
 # Check whether the year is between 1900 and 2011
  c = 0			#year
  while (c < 1900) or (c > 2100):
    c = eval(input("Enter year: "))

# Check whether month is in the range of 1 to 12
  a  = 0		#month
  while (a < 1) or (a > 12):
    a = eval(input("Enter month: ")) 

# Assign a true/false variable to leap year
  leap_year = (c % 400 == 0) or ((c % 100 != 0) and (c % 4 == 0))
  
#Determine the day range that is appropiate for the month
  b = 0			#day
  if (a == 2):
    if (leap_year):
     while (b < 1) or  (b > 29):
        b = eval(input("Enter day: "))
    else:
      while (b < 1) or (b > 28):
        b = eval(input("Enter day: "))
  else:
    while (b < 1) or (b > 31):
      b = eval(input("Enter day: "))
    
#The century
  d = c // 100

#The year of the century
  c = c % 100

#Make adjustments to calendar so that the year begins in Jan and ends in Dec
  if (a < 3):
    a = a + 10
    c = c - 1
  else:
    a = a - 2

#Algorithm to compute the day of the week. "r" gives the day of the week
  w = (13 * a - 1) // 5
  x = c // 4
  y = d // 4
  z = w + x + y + b + c - 2 * d
  r = z % 7
  r = (r + 7) % 7

#Assign string names to the actual day of the week values
  if r == 0:
    r = "Sunday"
  if r == 1:
    r = "Monday"
  if r == 2:
    r = "Tuesday"
  if r == 3:
    r = "Wednesday"
  if r == 4:
    r = "Thursday"
  if r == 5:
    r = "Friday"
  if r == 6:
    r = "Saturday"

#Print the day of the week
  print("The day is", r)
main()
