import random
class Patient(object):
	def __init__(self,unID,name, allergies):
		self.unID = unID
		self.name = name
		self.allergies = allergies
		self.bedNumber = 0

	def display(self):
		print 'ID:',self.unID
		print 'Name:',self.name
		print 'Allergies:',self.allergies
		print 'Bed number:',self.bedNumber
Joe = Patient(1,'Joe','intellegence')
Joe.display()
print "____________________"
print "____________________"




class Hospital(object):
	def __init__(self,name,capacity):
		self.patients = []
		self.name = name
		self.capacity = capacity
		self.count = 0
	def admit(self, patient):
		self.patients.append(patient)
		self.count += 1
		if self.count >= self.capacity:
			print 'You are not welcome'
		return self
	def discharge(self,patient):
		self.patients.remove(patient)
		return self
	def info(self):
		for i in self.patients:
			print 'ID:',i.unID
			print 'Name:',i.name
			print 'Allergies:',i.allergies
			for i in range(self.capacity):
				bedNumber = random.randint(1,self.capacity)
			print "bed number:",bedNumber
			print " "
		return self

		
patient1 = Patient(2,"Cristian","losers")
patient2 = Patient(77,"Joe","intaligens")
patient3 = Patient(3,'Will', "air")
hospital = Hospital('Moncler',3)



hospital.admit(patient1).admit(patient2).admit(patient3).discharge(patient2).info()