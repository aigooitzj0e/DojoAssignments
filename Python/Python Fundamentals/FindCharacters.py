aList = ['hello','world','my','name','is','Anna']
char = 'o'
def findCharacters(aList, char):
    new_list = []
  
    for i in aList:
    # print i
      for j in range(len(i)):
          # print j
          if i[j] == char:
            new_list.append(i)
    return new_list

print findCharacters(aList, char)


################ VERSION 2 ##################

def findCharactersv2(aList, char)
    bList = []
    for ele in aList:
        if ele.find(char) >= 0:
            bList.append(ele)

print findCharactersv2(aList, Char)


################ VERSION 3 ###################

def findCharactersv3(aList, char):
    cList=[]
    for ele in aList:
        if ele.count(char) != 0:
            cList.append(ele)
    return cList
    
print findCharactersv3(aList, char)