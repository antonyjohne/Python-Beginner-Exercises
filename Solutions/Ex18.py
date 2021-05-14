"""
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

"""

input_pwlist = input("Enter a list of passwords: ").split(",")
checkstring1 = "abcdefghijklmnopqrstuvwxyz"
checkstring2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
checkstring3 = "0123456789"
checkstring4 = "$#@"
output_pwlist = []

for i in input_pwlist:
	key1, key2, key3, key4 = False, False, False, False

	if(6 <= len(i) <= 12):
		for j in i:
			if(j in checkstring1):
				key1 = True
				continue

			elif(j in checkstring2):
				key2 = True
				continue

			elif(j in checkstring3):
				key3 = True
				continue

			elif(j in checkstring4):
				key4 = True
				continue

		if (key1==True and key2==True and key3==True and key4==True):
			output_pwlist.append(i)

print(f"The eligible passwords are: {','.join(output_pwlist)}")