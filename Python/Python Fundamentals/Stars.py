############# PART I ################
def starsv1(aList):
  aString = ""
  for i in aList: #[2,3,4]
      for j in range(i): #Loop 
          aString += "*"
      print aString
      aString = ""

aList = [2,3,4,5]
print starsv1(aList)

############# PART II ###############
def starsv2(bList):
  bString = ""
  
  for i in bList:
    if type(i)==int:
      for j in range(i):
          bString += "*"
      print bString
      bString = ""
  
    else:
      for j in i:
        bString += i[0].upper()
      print bString
      bString = ""
      
bList = [2, "world", 3, 4, "hello", 12, "Joe Yu"]
print starsv2(bList)