def ScoresGrades():
  import random
  
  print "Scores and Grades"
  
  for i in range(11):
    x = random.randint(60,101)
    if x >= 90:
      print "Score:", x, "Your grade is an A"
    elif x >= 80 and x < 90:
      print "Score:", x, "Your grade is an B"
    elif x >= 70 and x < 80:
      print "Score:", x, "Your grade is an C"
    else:
      print "Score:", x, "Your grade is an D"

  print "End of program. DUECES!"

print ScoresGrades()
    
