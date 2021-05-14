"""
Question 4
Level 1

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

Suppose the following input is supplied to the program: 34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

"""

input_num = input("Enter a list of numbers: ")
output_list = input_num.split(",")
output_tuple = tuple(output_list)
print(output_list,"\n",output_tuple)