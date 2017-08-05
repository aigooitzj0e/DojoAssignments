students = [
  {'first_name':  'Michael', 'last_name' : 'Jordan'},
  {'first_name' : 'John', 'last_name' : 'Rosales'},
  {'first_name' : 'Mark', 'last_name' : 'Guillen'},
  {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def student_function():
  for student in students:
    print student['first_name'], student['last_name']

print student_function()


########################## Part II ############################

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print "Students:"
for i in range(len(users['Students'])):
  sum = 0
  sum = len(users['Students'][i]['first_name']) + len(users['Students'][i]['last_name'])
  # print sum
  print i+1, users['Students'][i]['first_name'], users['Students'][i]['last_name'], sum
  
  
print "Instructors:"
for i in range(len(users['Instructors'])):
  sum = 0
  sum = len(users['Instructors'][i]['first_name']) + len(users['Instructors'][i]['last_name'])
  # print sum
  print i+1, users['Instructors'][i]['first_name'], users['Instructors'][i]['last_name'], sum
'], users['Instructors'][i]['last_name'], sum
