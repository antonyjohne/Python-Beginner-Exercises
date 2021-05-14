"""
Question 7
Level 2

Write a program which takes 2 digits X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1,..., X-1  ;  j=0,1,...Y-1.

Suppose the following inputs are given to the program: 3,5
Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

"""

input_list = input("Enter 2 numbers: ").split(',')
x,  y = int(input_list[0]), int(input_list[1])

outer_list = []

for i in range(x):
	inner_list = []
	for j in range(y):
		inner_list.append(i*j)
	
	outer_list.append(inner_list)

print(outer_list)
