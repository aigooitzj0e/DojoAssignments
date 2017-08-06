class patient(object):
	def __init__(self, idd, name, allergies, bed):
		self.idd = idd
		self.name = name
		self.allergies = allergies
		self.bed_num = bed


class hospital(patient):
	def __init__(self, idd, name, allergies, bed):
		super(hospital, self).__init__(idd, name, allergies, bed)
		self.patient_list = []
		self.hospital_name = "Kaweah"
		self.capacity = 100
		self.count = 0

	def admit(self):
		self.patient_list.append(self.name) #append patient name to patient list
		self.count += 1
		print "Patient added.. Total patients is:", self.count
		print self.patient_list
		return self

	def discharge(self):
		self.search = self.patient_list.index(self.name) #searches to see what index the patient is at in list. returns index #
		self.patient_list.pop(self.search) #removes patient at designated index
		self.count -= 1
		print "Patient released.. Total patients is:", self.count
		return self

# bob = patient("01", "Bob", "Peanuts", "01")

pat1 = ('01', 'bob', 'peanuts', "001")
pat2 = ('02', 'larry', 'milk', "002")
pat3 = ('03', 'tom', 'orange', "003")
pat4 = ('04', 'susan', 'grass', "004")

hos1 = hospital(pat1, pat2, pat3, pat4)


hos1.admit().admit().discharge()
