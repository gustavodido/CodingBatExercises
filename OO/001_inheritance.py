class BaseClass:
	def __init__(self):
		print "BaseClass constructor."
		self.my_value = 10

	def my_method(self):
		print "BaseClass.my_method called."

class ChildClass(BaseClass):
	def __init__(self):
		print "ChildClass constructor."
		self.my_value = 20

	def my_method(self):
		print "ChildClass.my_method called"

b = BaseClass()
b.my_method()
print b.my_value

c = ChildClass()
c.my_method()
print c.my_value