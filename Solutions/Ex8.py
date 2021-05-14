"""
Question 8
Level 2

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world

"""

input_list = input("Enter a list of words: ").split(",")
output_list = ",".join(sorted(input_list))
print(f"The output is: {output_list}")