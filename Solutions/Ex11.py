"""
Question 11
Level 2

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Input: 0100,0011,1010,1001
Then the output should be: 1010

"""

input_list = [i for i in input("Enter a series of numbers: ").split(",")]
output_list = [str(i) for i in input_list if int(i,2)%5==0]
print(f"The output is: {','.join(output_list)}")
