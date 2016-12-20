#  File: DNA.py

#  Description: Finding the longest common base sequence in two DNA strands

#  Student Name: Orlando Reategui

#  Student UT EID: or3562	

#  Course Name: CS 303E

#  Unique Number: 51635

#  Date Created: 3/28/2015

#  Date Last Modified: 3/28/2015

def main():
  # open the file for reading
  in_file = open ("dna.txt", "r")

  # read the number of pairs
  num_pairs = in_file.readline()
  # strips the '\n' from the line
  num_pairs = num_pairs.strip()
  # convert to integer
  num_pairs = int (num_pairs)
  #print title
  print("Longest Common Sequences \n")
  
  # read pairs of dna strands
  for i in range (num_pairs):
    st1 = in_file.readline()
    st2 = in_file.readline()

    st1 = st1.strip()
    st2 = st2.strip()

    # make the strings uppercase
    st1 = st1.upper()
    st2 = st2.upper()

    # order the strands by size
    if (len(st1) > len(st2)):
      dna1 = st1
      dna2 = st2
    else:
      dna1 = st2
      dna2 = st1

   # get all substrings of dna1
    # list to store substrings of dna1
    dna1_list = []
    wnd = len(dna1)
    while (wnd > 1):
      start_idx = 0
      while ((start_idx + wnd) <= len (dna1)):
        sub_strand = dna1[start_idx: start_idx + wnd]
        #store those substring in a list
        dna1_list.append(sub_strand)
        start_idx = start_idx + 1
      # make the window smaller
      wnd = wnd - 1
      
   # get all substrings of dna2 and check them against dna1
    # list to store matching substring sequences in both dna strands
    in_dna = []
    wnd = len (dna2)
    # get all substrings of dna2
    while (wnd > 1):
      start_idx = 0
      while ((start_idx + wnd) <= len (dna2)):
        sub_strand = dna2[start_idx: start_idx + wnd]
		# check if it exists in dna1. If it does append it to the list called in_dna
        if sub_strand in dna1_list:
          in_dna.append(sub_strand)
        start_idx = start_idx + 1
      # make the window smaller
      wnd = wnd - 1
    #If our numer of largest common sequences found is not empty
    if in_dna != []:
      # store the largest string found in the in_dna list to a variable called maxlist
      maxlen = len(max(in_dna, key=len))
      maxlist = [s for s in in_dna if len(s) == maxlen]
      # If we have more than one largest common sequence, print each new sequence indented in a new line
      if len(maxlist) > 1:
        #loop to print the other largest common sequences if we have more than one
        for d in range(len(maxlist)-1):
          print("Pair", str(i+1) + ":",max(in_dna,key=len))
          print("       ",maxlist[d+1])
        #prints new line  
        print("")
      #If we have only one common sequence, then print that sequence only.
      else:
        print("Pair", str(i+1) + ":",max(in_dna,key=len),"\n")
    #Print "No Sequence Found" if there is largest common sequences found
    else:
      print("Pair", str(i+1) + ":","No Common Sequence Found \n")
    
  # close file
  in_file.close()
main()
