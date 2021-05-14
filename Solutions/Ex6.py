"""
Question 6
Level 2

Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
The fixed values of C and H are 50 & 30 respectively
D is the variable whose values should be input to your program in a comma-separated sequence.

Let us assume the following comma separated input sequence is given to the program: 100,150,180
The output of the program should be: 18,22,24

"""

from math import sqrt

c, h = 50, 30
input_str = input("Enter a list of numbers: ")
input_list = input_str.split(",")
output_list = []

for d in input_list:
	q = str(int(sqrt((2*c*int(d))/h)))
	output_list.append(q)

output_str = ",".join(output_list)
print(f"The result is: {output_str}")