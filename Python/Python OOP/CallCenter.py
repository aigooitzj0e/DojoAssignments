class Call(object):
	def __init__(self, unique_id, caller_name, caller_phone_number, time_call, reason_call):
		self.unique_id = unique_id
		self.caller_name = caller_name
		self.caller_phone_number = caller_phone_number
		self.time_call = time_call
		self.reason_call = reason_call

	def display(self):
		print self.unique_id
		print self.caller_name
		print self.caller_phone_number
		print self.time_call
		print self.reason_call

christian = Call("loser", "christian", 555555555, "7:00am", "Diarrhea")
christian.display()

class CallCenter(Call):
	def __init__(self, unique_id, caller_name, caller_phone_number, time_call, reason_call):
		super(CallCenter, self).__init__(unique_id, caller_name, caller_phone_number, time_call, reason_call)
		self.calls = calls
		self.numbers = numbers
		# self.queue_size = len(self.calls)

	def add(self):
		self.calls = []
		self.queue_size = len(self.calls)
		self.calls.append(self.caller_phone_number)
		return self

	def remove(self):
		self.calls.pop(0)
		return self

	def info(self):
		print self.caller_name, self.calls, len(self.calls)
		return self



call1 = CallCenter(1, "christian", 555555555, "7:00am", "Diarrhea")
call2 = CallCenter(2, "mike", 555555555, "7:00am", "Diarrhea")
call3 = CallCenter(3, "will", 555555555, "7:00am", "Diarrhea")

numbers = [call1, call2, call3]

callcntr = CallCenter([call1, call2, call3])
christian1.add().info()

