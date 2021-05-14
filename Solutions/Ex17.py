"""
Question 17
Level 2

Write a program that computes the net amount of a bank account based a transaction log from console input. 
D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100

Then, the output should be: 500

"""

total = 0

print("Enter log amount: ")

while True:
	input_str = input()

	if(input_str!=""):
		if("D" in input_str):
			total+=int(input_str[2:])

		elif("W" in input_str):
			total-=int(input_str[2:])

	else:
		break

print(f"The total amount is: {total}")