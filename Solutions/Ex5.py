"""
Question 5
Level 1

Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.

Also please include simple test function to test the class methods.

"""

class get_put:

	def __init__(self):
		pass

	def get_str(self):
		self.input_str = input("Enter a String: ")

	def put_str(self):
		print(f"You entered the string: {self.input_str}")

test = get_put()
test.get_str()
test.put_str()