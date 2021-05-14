"""
Question 20
Level 3

Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

"""

class gen_num:

	def __init__(self):
		pass

	def gen(self,n):
		self.n = n
		for i in range(self.n):
			if(i%7 == 0):
				yield i

test = gen_num()
print(list(test.gen(100)))