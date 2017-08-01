sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


print type(sI)
print type(bI)
print type(eI)
print type(spI)
print type(sS)
print type(mS)
print type(bS)
print type(eS)
print type(aL)
print type(mL)
print type(lL)
print type(eL)
print type(spL)

if isinstance(sI, int) >= 100:
    print "That's a big number!"
if isinstance(sI, int) < 100:
    print "That's a small number!"

if isinstance(sI, str) >= 50:
    print "long sentence!"
if isinstance(sI, str) < 50:
    print "Short Sentence"

if isinstance(sI, list) >= 10:
    print "Big List"
if isinstance(sI, list) < 10:
    print "Short List"






# num = 26

# if num >= 100:
#     print "That's a big number!"
# elif num < 100:
#     print "That's a small number"