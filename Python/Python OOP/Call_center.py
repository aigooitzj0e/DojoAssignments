
class Call():
    def __init__(self,ID,caller_name,time,reason):
        self.ID = ID
        self.caller = caller_name
        self.time = time
        self.reason = reason
    def display(self):
        print "ID: " + self.ID
        print "Caller Name:" + self.caller
        print "Time of call: " + self.time
        print "Reason for call: " + self.reason

Call("01","Christian","9:00 AM","Needs backrub").display()

class callCenter():
    def __init__(self,call):
        self.call = call
        self.queue = len(self.call)
    def add(self):
        self.call.append(self.call[len(self.call)-1]+1)
        return self
    def remove(self):
        self.call.remove(self.call[0])
        return self
    def info(self):
        print str(self.queue) + " in Queue"
        return self

callCenter([1348534,3455222,55488483,932582375,72352525]).remove().info()
