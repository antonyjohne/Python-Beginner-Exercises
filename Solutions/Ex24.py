"""
Question 24
Level 3

Define a class, which have a class parameter and have a same instance parameter.

"""

class same:
	total_inst = 0

	def __init__(self):
		same.total_inst += 1

	def put(self):
		print(self.total_inst)

test = same()
test.put()

test2 = same()
test2.put()