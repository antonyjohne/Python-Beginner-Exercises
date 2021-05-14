"""
Question 13
Level 2

Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program: hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

"""
letters, digits = 0 , 0

input_str = input("Enter a string: ")
for i in input_str:
	if(i.isalpha()):
		letters+=1

	elif(i.isdigit()):
		digits+=1

print(f"Letters: {letters} \nDigits: {digits}")