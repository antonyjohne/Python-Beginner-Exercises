"""
Question 3
Level 1

With a given integral number i, write a program to generate a dictionary that contains (i, i*i) between 1 and n (both included). 
The program should then print the dictionary.

Suppose the following input is supplied to the program: 8
Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

"""

input_num = int(input("Enter a number: "))
output_dict = {i:i*i for i in range(1, input_num+1)}
print(f"The output is : {output_dict}")
