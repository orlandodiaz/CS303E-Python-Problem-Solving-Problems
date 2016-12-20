#  File: EasterSunday.py

#  Description: Compute the date of Easter Sunday

#  Student Name: Orlando Reategui

#  Student UT EID: or3562

#  Course Name: CS 303E

#  Unique Number: 51635 

#  Date Created: 2/2/2015

#  Date Last Modified: 2/2/2015

def main():

#Prompt the user to enter year
	y = eval(input("Enter year:"))

#Use algorithm invented by Carl Friedrich Gaus to claculate exact date.
	a = y % 19
	b = y // 100
	c = y % 100
	d = b // 4
	e = b % 4
	g = (8 * b + 13) // 25
	h = (19 * a + b - d - g + 15) % 30
	j = c // 4
	k = c % 4
	m = (1 + 11 * h) // 319
	r = (2 * e + 2 * j - k - h + m + 32) % 7
	n = (h - m + r + 90) // 25
	p = (h - m + r + n + 19) % 32

#Associate the variable n with the actual name of the month
	if (n==4):
		month = "April"
	if (n==3):
		month = "March"

#Print the date Eastern Sunday falls in
	print("In", y, "Easter Sunday is on", p, month)

main()
