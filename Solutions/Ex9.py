"""
Question 9
Level 2

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

"""

print("Enter a String:")

input_list = []

while True:
	lines = input()

	if lines:
		input_list.append(lines)

	else:
		break

print("The output is:")

for i in input_list:
	print(i.upper())
