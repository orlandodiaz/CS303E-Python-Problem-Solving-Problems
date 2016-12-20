#  File: Benford.py

#  Description: Verify Benford's law for the US Census data of 2009

#  Student Name: Orlando Reategui

#  Student UT EID: or3562

#  Course Name: CS 303E

#  Unique Number: 51635

#  Date Created: 04/25/2015

#  Date Last Modified: 04/25/2015

def main():
  #reads the file and stores all the population data into a list
  pop_num = []
  inFile = open ("./Census_2009.txt", "r")
  count = 0
  for line in inFile:
    if (count == 0):
      count += 1
      continue
    else:
      count += 1
      line = line.strip()
      word_list = line.split()
      pop_num.append (word_list[-1])
  inFile.close()
  #define frequency dictionary
  frequency = {}
  #define  keys; set initial values to 0
  for i in range(1,10):
    frequency[i] = 0
  #main loop that reads every number in the list of populations
  for i in range(0,len(pop_num)):
    number = pop_num[i]
    #strips every other digit except for the first
    number = number[0:1]
    #loop to add frequency to the correspondent key
    for i in range(1,10):
      if int(number) == i:
        frequency[i] = frequency[i] + 1
  #Print table headers
  print("Digit \t Count \t %")
  #loop to print the rest of the rows
  for i in range(1,10):
    print(i,"\t",frequency[i], "\t",round(100 * (frequency[i] / len(pop_num)),1))
main()
