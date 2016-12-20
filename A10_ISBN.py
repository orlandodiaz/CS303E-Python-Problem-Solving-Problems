#  File: ISBN.py

#  Description: Verifies whether a list of ISBN numbers in a given text file are valid and outputs the results in a text file.

#  Student Name: Orlando Reategui

#  Student UT EID: or3562	

#  Course Name: CS 303E

#  Unique Number: 51635

#  Date Created: 4/04/2015

#  Date Last Modified: 4/04/2015

def main():

  #open the file for reading
  input = open ("isbn.txt", "r")
  #open the file to write
  output = open ("isbnOut.txt", "w")

  #define function to sum digits
  def sum_digits (n):
    sum_n = 0
    while (n > 0):
      sum_n = sum_n + (n % 10)
      n = n // 10
    return sum_n
  
  #read number of present lines one by one
  for i in range(len(open("isbn.txt").readlines())):
    #read the first line
    isbn_original = input.readline()
    #strip the '\n' from the end of the line
    isbn_original = isbn_original.strip()
    #remove dashes but store it in a new variable isbn
    isbn = isbn_original.replace('-','')
  
    #if 'X' is somewhere in our first 9 digits, set x_somewhere = True
    x_somewhere = False
    for i in range(0,len(isbn)-1):
      if isbn[i] == 'X':
        x_somewhere = True

    #initial sum value    
    sum = 0    
    #if we have no 'X' present in our first 9 digits, our code is valid, so proceed. 
    if x_somewhere == False:
      #if 'X' is present in the last digit, only sum the partial sum of the first 9 digits, convert X separately and add it to the sum later.
      if isbn[9] == 'X':
        #only sum the partial sum of the first 9 digits
        for i in range(1,10):
          sum = sum +  sum_digits(int(isbn[:i]))
        sum = sum + (sum_digits(int(isbn[:9])) + 10)
      else:
      #initiate loop to sum the partial sums of all the digits
        for i in range(1,11):
          sum = sum +  sum_digits(int(isbn[:i]))

    #check if our final sum is divisible by 11 and if we have no 'X' somewhere in our first 9 digits. If so, our ISBN is valid.
    if  (sum % 11)  == 0 and x_somewhere == False:
      output.write(isbn_original + '  ' + 'valid' + '\n' )
    #if our final sum is not divisible by or we have an X value in our first 9 digits our ISBN is invalid.
    else:
      output.write(isbn_original + '  ' + 'invalid' + '\n' )
main()




