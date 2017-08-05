

####################### PART I #############################

class MathDojo(object):
	def __init__(self):
		self.result = 0  #result is keeping count

	def add(self, *numbers):  # *numbers (splat operator) allows you to add as much variables you need without actually adding extra parameters
		for val in numbers:  # iterates through numbers and sets self.result to the sum.
			self.result += val 
		return self

	def subtract(self, *numbers):
		for val in numbers:  #iterates through numbers and subtracts all the values
			self.result -= val
		return self

md = MathDojo()
print md.add(2).add(2, 5, 4, 7, 8, 5, 9, 9).subtract(3, 2).result


######################## PART II//III #############################

class MathDojo2(object):
	def __init__(self):
		self.result = 0

	def add(self, *args):
		for x in args:  #iterates through args
			if type(x) is list or type(x) is tuple: #if the elements type is a list or tuple. add sum of element.
				for i in x:
					self.result += i
			elif type(x) is int or type(x) is float: #else if element type is an integer or a decimal. add sum
				self.result += x
		return self

	def subtract(self, *args): 
		for x in args:
			if type(x) is list or type(x) is tuple:
				for i in x:
					self.result -= i
			elif type(x) is int:
				self. result -= x
		return self

md2 = MathDojo2()
print md2.add([1],3,4).add([3, 5, 7, 8], (2, 4.3, 1.25)).subtract(2, [2,3], [1.1, 2.3]).result

