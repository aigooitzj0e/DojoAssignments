#Multiples Pt. 1
for num in range(1, 1001):
    print "Looping from 1-1000", num


#Multiples Pt. 2
for num in range(5, 1001):
    if num%5==0:
        print "Multiples of 5: ", num


#Sum List
a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in a:
    sum += num
print "Sum of list a is: ", sum


#Average List
avg = sum/len(a)
print "Average of list a is: ", avg
