"""
Question 23
Level 3

Write a Python program to compute the sum of the digits of the number 2 power n, where n is input by the user.

If the input provided is 2 power 10 then 2^10 = 1024 and the sum of its digits is 1 + 0 + 2 + 4 = 7

"""

input_num =  int(input("Enter a number: "))
power = 2**input_num
total = 0

for i in str(power):
	total+=int(i)

print(f"The output is: {total}")