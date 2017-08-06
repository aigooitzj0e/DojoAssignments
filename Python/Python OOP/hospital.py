class patient():
	def __init__(self, idd, name, allergies, bed):
		self.idd = idd
		self.name = name
		self.allergies = allergies
		self.bed_num = bed


class hospital(object):
	def __init__(self,hospital_name, capactiy):
		self.patient_list = []
		self.hospital_name = hospital_name
		self.capacity = capacity
		self.bed_num = self.count
		self.count = 0

	def admit(self):
		self.patient_list.append(self.name) #append patient name to patient list
		self.count += 1
		print bed_num
		
	def discharge(self):
		self.search = patient_list.index(self.name) #searches to see what index the patient is at in list. returns index #
		self.patient_list.pop(self.search) #removes patient at designated index


bob = patient("01", "Bob", "Peanuts", "01")

hospital1 = hospital("Kahwea", 100)
hospital1.admit()