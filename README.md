# Python Beginner Exercises

I've been learning the python programming language over the past few weeks, and have compiled/practiced a list of Exercises that helped me solidify my programming skills and familiarize myself with the language. These exercises are only for Beginners who have just started their programming quest and want to get thier feet wet in python. The 3 Levels indicate varying degrees of increasing difficulty with respect to a Beginner.

If you would like to learn Python from scratch, I highly recommend checking out "Corey Schafer" channel on Youtube. His method of teaching is very lucid and intuitive.

Channel Link: https://youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

________________________________________________________________________________________________________________________

Question 1
Level 1

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).

The numbers obtained should be printed in a comma-separated sequence on a single line.


________________________________________________________________________________________________________________________
Question 2
Level 1

Write a program which can compute the factorial of a given number.
The results should be printed in a comma-separated sequence on a single line.

Suppose the following input is supplied to the program: 8

Then, the output should be: 40320


________________________________________________________________________________________________________________________
Question 3
Level 1

With a given integral number i, write a program to generate a dictionary that contains (i, i*i) between 1 and n (both included). 
The program should then print the dictionary.

Suppose the following input is supplied to the program: 8

Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


________________________________________________________________________________________________________________________
Question 4
Level 1

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

Suppose the following input is supplied to the program: 34,67,55,33,12,98

Then, the output should be:\
['34', '67', '55', '33', '12', '98']\
('34', '67', '55', '33', '12', '98')


________________________________________________________________________________________________________________________
Question 5
Level 1

Define a class which has at least two methods:

getString: to get a string from console input\
printString: to print the string in upper case.

Also please include simple test function to test the class methods.


________________________________________________________________________________________________________________________
Question 6
Level 2

Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 * C * D)/H]\
The fixed values of C and H are 50 & 30 respectively\
D is the variable whose values should be input to your program in a comma-separated sequence.

Let us assume the following comma separated input sequence is given to the program: 100,150,180

The output of the program should be: 18,22,24


________________________________________________________________________________________________________________________
Question 7
Level 2

Write a program which takes 2 digits X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

Note: i=0,1,..., X-1  ;  j=0,1,...Y-1.

Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 


________________________________________________________________________________________________________________________
Question 8
Level 2

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program: without,hello,bag,world

Then, the output should be: bag,hello,without,world


________________________________________________________________________________________________________________________
Question 9
Level 2

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:\
Hello world\
Practice makes perfect

Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT


________________________________________________________________________________________________________________________
Question 10
Level 2

Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again

Then, the output should be: again and hello makes perfect practice world


________________________________________________________________________________________________________________________
Question 11
Level 2

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Input: 0100,0011,1010,1001

Then the output should be: 1010


________________________________________________________________________________________________________________________
Question 12
Level 2

Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.

The numbers obtained should be printed in a comma-separated sequence on a single line.


________________________________________________________________________________________________________________________
Question 13
Level 2

Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program: hello world! 123

Then, the output should be:\
LETTERS 10\
DIGITS 3


________________________________________________________________________________________________________________________
Question 14
Level 2

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the input supplied to the program is: Hello world!

Then, the output should be:\
UPPER CASE 1\
LOWER CASE 9


________________________________________________________________________________________________________________________
Question 15
Level 2

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program: 9

Then, the output should be: 11106


________________________________________________________________________________________________________________________
Question 16
Level 2

Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9

Then, the output should be: 1,3,5,7,9


________________________________________________________________________________________________________________________
Question 17
Level 2

Write a program that computes the net amount of a bank account based a transaction log from console input. D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:\
D 300\
D 300\
W 200\
D 100

Then, the output should be: 500


________________________________________________________________________________________________________________________
Question 18
Level 3

A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.


If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be: ABd1234@1


________________________________________________________________________________________________________________________
Question 19
Level 3

You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. 

The priority of the sort is: name > age > score.

If the following tuples are given as input to the program:

Tom,19,80\
John,20,90\
Jony,17,91\
Jony,17,93\
Json,21,85

Then, the output of the program should be:\
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


________________________________________________________________________________________________________________________
Question 20
Level 3

Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.


________________________________________________________________________________________________________________________
Question 21
Level 3

A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The numbers after the direction are steps. Write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.

Example:
If the following tuples are given as input to the program:\
UP 5\
DOWN 3\
LEFT 3\
RIGHT 2

Then, the output of the program should be: 2


________________________________________________________________________________________________________________________
Question 22
Level 3

Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:\
2:2\
3.:1\
3?:1\
New:1\
Python:5\
Read:1\
and:1\
between:1\
choosing:1\
or:2\
to:1


________________________________________________________________________________________________________________________
Question 23
Level 3

Write a Python program to compute the sum of the digits of the number 2 power n, where n is input by the user.

If the input provided is 2 power 10 then 2^10 = 1024 and the sum of its digits is 1 + 0 + 2 + 4 = 7


________________________________________________________________________________________________________________________
Question 24
Level 3

Define a class, which have a class parameter and have a same instance parameter.


________________________________________________________________________________________________________________________
Question 25
Level 3

Create a Circle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.


