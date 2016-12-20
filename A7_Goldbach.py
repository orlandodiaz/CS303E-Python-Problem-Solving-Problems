#  File: Goldbach.py

#  Description: Verify Goldbach's conjecture in a user defined range and determine what is the maximum number of pairs of prime numbers for a given even number in that range.

#  Student Name: Orlando Reategui

#  Student UT EID: or3562

#  Course Name: CS 303E

#  Unique Number: 51635

#  Date Created: 03/13/2015

#  Date Last Modified: 03/13/2015

#isPrime is the function to determine whether a number is prime or not. If it's not it will return False and vice versa.
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    if number == 1:
      return False
    else:
      return True

#Low is the lower Limit and high is the upper limit.
low = 3
high = 5

#We use a loop in order keep prompting the user until he submits the correct input.
#If it's not even or if it's below 4, we keep prompting.
while  ((low % 2) != 0) or (low < 4):
  low = eval(input("Enter a lower limit:"))
  
#If the lower limit set is correct, we use a similar procedure for entering the upper limit.
#If the upper limit is not even and while the low limit is high than the high limit, we keep prompting.
else:
  while  (high % 2) != 0 or (low > high):
    high = eval(input("Enter an upper limit:"))

#Set an empty list called a to store the numbers of pairs
a = []
#Begin for loop which will repeat the process starting from the lower limit up to the high limit. "high + 1" because it's in a range.
for i in range (low, high +1, 2):
  #Output is the pairs plus equals sign part. So for each time two prime numbers add up to the number i, those two numbers will be added to the output.
  output = ''
  #n is our count, basically.
  n = 2
  #Initially we begin with zero pairs
  pairs = 0
  #Unlike the for loop, the while loop's job is to find as many two prime numbers that add up to i.
  while n <= (i-n):
    if isPrime(n):
      if isPrime(i - n)  :
        #each new find we append to the output
        output += ' = ' +  str(n) + ' + ' + str(i-n)
        #increase count, and pairs
        n += 1
        pairs += 1
      else:
       #increase count only
       n += 1


    else:
      #increase count only
      n += 1
  #append pairs to our pairs list
  a.append(pairs)
  #Finally, print our low and high limits (i) and the output(possible pair combinations)
  print(i, output)


#Because we stored our pairs on a list, we print the maximum number of pairs present in the list called a
print("The maximum number of pairs = ", max(a))

