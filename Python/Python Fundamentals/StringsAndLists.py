print "Find and Replace"
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day", 1)
newStr = words + words.replace("day", "month", 1)
print newStr

print "Min and Max"
numbers = [2,54,-2,7,94,15]
print "Min is: ", min(numbers)
print "Max is: ", max(numbers)

print "First and Last"
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x)-1]

print "New List"
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
first_list = x[:len(x)/2] 
second_list = x[len(x)/2:]
print "first list", first_list
print "second list", second_list
second_list.insert(0,first_list)
print second_list
