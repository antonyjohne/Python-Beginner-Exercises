"""
Question 14
Level 2

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the input supplied to the program is: Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

"""

upper, lower = 0 , 0
input_str = input("Enter a string: ")
for i in input_str:
	if(i.isupper()):
		upper+=1

	elif(i.islower()):
		lower+=1

print(f"Upper Case: {upper} \nLower Case: {lower}")