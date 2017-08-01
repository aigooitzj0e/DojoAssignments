
1 = ["magical unicorns", 19, "hello", 98.98, "world"]
2 = [2, 3, 1, 7, 4, 12]
3 = ["magical", "unicorns"]

def typeList    
    sum =0
    string =""

    for i in aList:
        if isinstance(i, int) or isinstance(i, float):
        sum+=i
        elif isinstance(i,str):
        string += i

    if sum and string:
        print "MIXED"
        print "Sum: ", sum
        print "String: ", string
    
    elif sum:
        print "Integers only", sum
    
    else:
        print "String: ", string