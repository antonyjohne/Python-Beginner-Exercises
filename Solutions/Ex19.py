"""
Question 19
Level 3

You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
The priority of the sort is: name > age > score.

If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

"""

from operator import itemgetter

input_list = []
print("Enter a list of data: ")

while True:
	input_tuple = input()

	if(input_tuple != ""):
		input_list.append(tuple(input_tuple.split(",")))

	else:
		break

list_sorted = sorted(input_list, key=itemgetter(0,1,2))
print(list_sorted)