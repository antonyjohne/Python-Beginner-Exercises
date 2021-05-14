"""
Question 12
Level 2

Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""

output_list = []

for i in range(1000,3001):
	key = True
	
	for j in str(i):
		if(int(j)%2 != 0):
			key = False
			break

	if (key==True):
		output_list.append(str(i))

print(",".join(output_list))