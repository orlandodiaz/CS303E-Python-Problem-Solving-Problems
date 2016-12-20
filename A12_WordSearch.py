#  File: WordSearch.py

#  Description: Search a list of words vertically and horizontally in a given file.

#  Student Name: Orlando Reategui

#  Student UT EID: or3562

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 303E 

#  Unique Number: 51635

#  Date Created: 04/06/2015

#  Date Last Modified: 04/06/2015

def main():
  #Open file to read
  file = open ("hidden.txt", "r")
  #Open file to output
  output = open ("found.txt", "w")
  
  #function to align output correctly later
  def align(string1, string2):
      return "{:<12s}{:>10s}".format(string1, string2)

  #word = input("Enter the word you want to find")
  # read m by n
  line = file.readline()
  # strip \n
  line = line.strip()
  #split the results
  line = line.split(" ")
  #rows is m
  rows = int(line[0])
  #columns is n
  columns = int(line[1])

  #read empty line
  line = file.readline()

  # read table and put lines  in a 2-d list
  a = []
  for i in range(rows):
    line = file.readline()
    line = line.strip()
    line = line.replace(" ", "")
    a.append(line)

  #read empty line
  line = file.readline()
  
  #read word count
  line = file.readline()
  #strip \n
  line = line.strip()
  wordcount = int(line)
  
  #Repeat process with different words
  for i in range(rows):
    line = file.readline()
    line = line.strip()
    word = line

    # Find words vertically
    #Set vertical found words to False
    vfound = False
    for j in range(columns):
      string = ''
      for k in range(rows):
        string = string + a[0+k][j]
      #is word is in vertical string
      if (word in string):
        value = str((string.index(word)) + 1) + '   ' +  str(j + 1)
        output.write(align(word, value + '\n'))
        vfound = True
      #if not, is it backwards
      elif (word in string[::-1]):
        value = str(rows - (string[::-1].index(word))) + '   ' +  str(j+1)
        output.write(align(word, value + '\n'))
        vfound = True
      else:
        continue
	#set horizontal found words to False
    hfound = False
    #Finds words horizontally, works both ways
    if vfound == False:
      for s in range(len(a)):
        col = a[s]
        # If word is found horizontally, write to found.txt
        if word in col:
          value = str(s+1) + '   ' + str(col.index(word) + 1)
          output.write(align(word, value + '\n'))
          hfound = True
        # If word is found horizontally (Backwards), write to found.txt
        elif word[::-1] in col:
          value = str(s+1) + '   ' + str(rows - col[::-1].index(word))
          output.write(align(word, value + '\n'))
          hfound = True
    #If no vertical or horizontal words found, then write 00 next to the word
    if vfound == False and hfound == False:
      value = '0   0'
      output.write(align(word, value + '\n'))
  #Close files
  file.close()
  output.close()
main()
