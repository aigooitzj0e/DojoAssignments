#### ODD/EVEN ####
def odd_even():
    for i in range(1, 2001):
        if i%2==1:
            print "Number is: ", i, " This is an ODD number!"
        if i%2==0:
            print "Number is: ", i, " This is an EVEN number!"

# print odd_even()



# #### MULTIPLY ####
def multiply(aList, n):
  for num in range(len(aList)):
    aList[num] *= n
  return aList
  
theeList = [3,4,5]
multiplyResult = multiply(theeList, 3)
print multiplyResult
  

#### HACKER ####


def layered_multiples(multiplyResult): #[6,12,15]
  new_array= []
  temp = []
  for i in multiplyResult: #[6]
    for j in range(i):
      temp.append(1)
    new_array.append(temp)
    temp = []
  return new_array

layered = layered_multiples(multiplyResult)
print layered