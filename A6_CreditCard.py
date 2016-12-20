#  File: CreditCard.py

#  Description: Use Luhn's test to verify the authenticity of credit card numbers.

#  Student Name: Orlando Reategui

#  Student UT EID: or3562

#  Course Name: CS 303E

#  Unique Number: 51635

#  Date Created: 03/05/2015

#  Date Last Modified: 03/05/2015

#function to sum the digits of a given a number
def sum_digits(n):
  sum = 0
  while n > 0:
    sum = sum + (n % 10)
    n = (n // 10) 
  return sum 
  
#function to determine whether the credit card number is valid or not using Luhn's test
#d1_2, d1_3, represent the digits of the card after they have been multiplied by 2 and had their digits summed.
def is_valid(num):
  d1_2 = sum_digits((d1 * 2))
  d3_2 = sum_digits((d3 * 2))
  d5_2 = sum_digits((d5 * 2))
  d7_2 = sum_digits((d7 * 2))
  d9_2 = sum_digits((d9 * 2))
  d11_2 = sum_digits((d11 * 2))
  d13_2 = sum_digits((d13 * 2))
  d15_2 = sum_digits((d15 * 2))
  sum = (d0 + d1_2 + d2 + d3_2 + d4 + d5_2 + d6 + d7_2 +d8 +d9_2 + d10 + d11_2 + d12 + d13_2 + d14 + d15_2)
  #return true or false if the sum above is divisible by 10
  return (sum % 10) == 0  

#function that returns the credit card type in string format. It uses if statements to determine if the starting digit matches that of the credit card.
def cc_type(num):
  if len(str(num)) == 16:
    if (d15 == 3 and d14 == 4) or (d15 == 3 and d14 == 7):
      return 'American Express'
    elif (d15 == 6 and d14 == 0 and d13 == 1 and d12 == 1) or (d15 == 6 and d14 == 5):
      return 'Discover'
    elif (d15 == 5 and d14 == 0) or (d15 == 5 and (d14 >= 0 and d14 <= 5)):
      return 'MasterCard'
    elif (d15 == 4):
      return 'Visa'
    else:
      return ''
  else:
    if (d14 == 3 and d13 == 4) or (d14 == 3 and d13 == 7):
      return 'American Express'
    elif (d14 == 6 and d13 == 0 and d12 == 1 and d11 == 1) or (d14 == 6 and d13 == 5):
      return 'Discover'
    elif (d14 == 5 and d13 == 0) or (d12 == 5 and (d11 >= 0 and d10 <= 5)):
      return 'MasterCard'
    elif (d14 == 4):
      return 'Visa'
    else:
      return ''  
#main function which analyzes and defines the initial values for each digit in the credit card number
def main():
  num = eval(input("Enter a 15 or 16-digit credit card number:"))
  global d0
  global d1
  global d2
  global d3
  global d4
  global d5
  global d6
  global d7
  global d8
  global d9
  global d10
  global d11
  global d12
  global d13
  global d14
  global d15
  #We pull off the digits one by one by taking modulo 10 (to get the last digit) and using // 10 to chop the last digit.
  d0 = num % 10
  d1 =  (num // 10) % 10
  d2 =  (num // 100) % 10
  d3 =  (num // 1000) % 10
  d4 =  (num // 10000) % 10
  d5 =  (num // 100000) % 10
  d6 =  (num // 1000000) % 10
  d7 =  (num // 10000000) % 10
  d8 =  (num // 100000000) % 10
  d9 =  (num // 1000000000) % 10
  d10 = (num // 10000000000) % 10
  d11 = (num // 100000000000) % 10
  d12 = (num // 1000000000000) % 10
  d13 = (num // 10000000000000) % 10
  d14 = (num // 100000000000000) % 10
  d15 = (num // 1000000000000000) % 10
  
  ##if the credit card is 15 to 16 characters long we proceed, otherwise we thrown an error and exit the program
  if len(str(num)) == 15 or len(str(num)) == 16:
    if is_valid(num):
      print("Valid", cc_type(num), "credit card number")
    else:
      print("Invalid credit card number") 
  else:
    print("Not a 15 or 16-digit number")
    return
main()
