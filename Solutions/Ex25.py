"""
Question 25
Level 3

Create a Circle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.

"""

class Circle:

	def __init__(self, radius):
		self.radius = radius

	def get_area(self):
		self.area = 3.14 * (self.radius ** 2)
		print(f"The area of the circle is: {self.area}")

	def get_circumference(self):
		self.circumference = 2 * 3.14 * self.radius
		print(f"The circumference of the circle is: {self.circumference}")

c1 = Circle(5)
c1.get_area()
c1.get_circumference()

c2 = Circle(10)
c2.get_area()
c2.get_circumference()
