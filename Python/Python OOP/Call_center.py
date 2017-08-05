class Call(object):
	def __init__(self, idd, name, phone, time, reason):
		self.id = idd
		self.name = name
		self.phone = phone
		self.time = time
		self.reason = reason

	def display(self):
		print self.id
		print self.name
		print self.phone
		print self.time
		print self.reason


bob = Call(01, "bob", 2, 6, "ok")
bob.display()

class CallCenter(Call):
	def __init__(self, Call):
		super(CallCenter, self).__init__(name, phone)
		self.call = []
		self.que = len(self.call)

	def add(self):
		self.call.append(Call)


	def remove(self):
		self.call.pop(0)

	def info(self):
		for caller in self.call:
			for i in caller:
				print caller[1]
				print caller[2]

