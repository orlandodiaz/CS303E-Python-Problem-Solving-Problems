#  File: MagicSquare.py

#  Description: Determine whether a 2-d list is a magic square and print the output in a new file.

#  Student Name: Orlando Reategui

#  Student UT EID: or3562

#  Course Name: CS 303E

#  Unique Number: 51635

#  Date Created: 04/11/2015

#  Date Last Modified: 04/11/2015

def main():
  # open file for reading
  in_file = open ("squares.txt", "r")
  # create file for writing
  results = open("results.txt", "a")
  # read number of squares
  line = in_file.readline()
  line = line.strip()
  num_squares = int (line)
  # write number of squares
  results.write(str(num_squares) + '\n')
  # read a blank line; write a blank line
  line = in_file.readline()
  results.write('\n')

  # read and process the number of squares
  for i in range (num_squares):
    line = in_file.readline()
    line = line.strip()    
    dim = int (line)
    
    # create 2-D list that is the square
    square = []

    # read data to populate the 2-D list
    for j in range (dim):
      line = in_file.readline()
      line = line.strip()
      row = line.split()

      # convert the strings to integers
      for k in range (dim):
        row[k] = int (row[k])

      # add row to the square
      square.append (row)

    # read blank line
    line = in_file.readline()

    # determine if square is magic and print result
    b = square
    def isMagic(b):
      # sum of each row
      for i in range (len(b)):
        sum_row = 0
      for j in range (len(b[i])):
        sum_row = sum_row + b[i][j]

      # sum of each column
      for j in range (len(b[0])):
        sum_col = 0
        for i in range (len(b)):
          sum_col += b[i][j]

      # sum diagonal left to right
      sum_lr = 0
      for i in range (len(b)):
        sum_lr += b[i][i]

      # sum diagonal right to left
      sum_rl = 0
      for i in range (len(b)):
        sum_rl += b[i][len(b) - 1 - i]
      # return True or False if they are all equal
      return (sum_row == sum_col == sum_lr == sum_rl)
    #Write Valid next to the dim number if its a magic number or not and vice versa.
    if isMagic(b):
      results.write(str(dim) + ' ' + 'Valid' + '\n')
    else:
      results.write(str(dim) + ' ' + 'Invalid' + '\n')

    #Format the square in the text file
    for y in range(0,dim):
      for u in range(0, dim):
        results.write(str(b[y][u]) + ' ')
      results.write('\n')
    results.write('\n')

  # close file
  results.close()
  in_file.close()
  print("The output has been written to results.txt")

main()
