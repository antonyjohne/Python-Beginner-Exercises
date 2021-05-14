"""
Question 21
Level 3

A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The numbers after the direction are steps. Write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.

Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2

Then, the output of the program should be:2

"""

from math import sqrt

input_list = []
print("Enter a list of directions: ")
ud , lr = 0, 0

while True:
	input_tuple = input()

	if(input_tuple != ""):
		input_list.append(tuple(input_tuple.split(' ')))

	else:
		break

for i in input_list:
	if(i[0] == "UP"):
		ud += int(i[1])

	elif(i[0] == "DOWN"):
		ud -= int(i[1])

	elif(i[0] == "LEFT"):
		lr += int(i[1])

	elif(i[0] == "RIGHT"):
		lr -= int(i[1])

total = round(sqrt((ud**2) + (lr**2)))
print(f"The total distance is: {total}")