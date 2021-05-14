"""
Question 2
Level 1

Write a program which can compute the factorial of a given number.
The results should be printed in a comma-separated sequence on a single line.

Suppose the following input is supplied to the program: 8
Then, the output should be: 40320

"""

input_num = int(input("Enter a number: "))
result = 1

while(input_num > 1):
	result = result * input_num
	input_num -= 1


print(f"The factorial is: {result}") 