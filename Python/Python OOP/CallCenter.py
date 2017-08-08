class call(object):
    def __init__(self,unId,name,number, time, reason):
        self.unId = unId
        self.name = name
        self.number = number 
        self.time = time
        self.reason = reason

        #print the information out ::
    def display(self):
        print self.unId
        print self.name
        print self.number
        print self.time
        print self.reason
        return self

Cristian = call(1,"Cristian", 9094206969,"4:20", "re-up")
Cristian.display()

class callCenter(object):
    def __init__(self):
        self.calls = [] #so that i can append and push information from caller
        self.queue = 0 # count the amount of callers I add

    def add(self,caller):
        self.calls.append(caller) #add the argument caller w/ call class into array of calls
        self.queue += 1 # add to the queue 
        return self

    def remove(self):
        self.calls.pop(len(self.calls)-1) #removes the last caller from the calls list
        self.queue -= 1 # remove 1 from the queue
        return self

    def info(self):
        print "______________________" #add a border between the queue
        print "amount of calls:",self.queue
        print "______________________"
        for i in self.calls: #print all the info from each element from the calls list..
            print " " #add spacing for the info..
            print "caller:", i.name
            print "number:", i.number
            print "time:", i.time
            print "reason:", i.reason
        return self

caller1 = call(1,'Joe', '8054209919','3:11','ping pong lessons') #gets information from the class for the caller.
caller2 = call(1,'Will', '6263111313','5:13','bang monte flores x3')
caller3 = call(1,'Mike', '2813308004','3:11','hit em on the low')
callcenter1 = callCenter()
callcenter1.add(caller1).add(caller2).add(caller3).info().remove().remove().info() #add caller argument to the add so i can get in the info from each caller..
