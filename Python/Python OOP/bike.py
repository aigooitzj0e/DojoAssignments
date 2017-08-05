class bike(object):
  def __init__(self, price, max_speed, miles):  #these are attributes
    self.price = price
    self.max_speed = max_speed
    self.miles = miles
  
  def displayinfo(self):    #these are methods (functions that DO something)
    if self.miles < 0:
      print "Cannot reverse negative"
      return False
    print self.price
    print self.max_speed
    print self.miles
    return self
    
    
  def ride(self):     #these are methods (functions that DO something)
    print "Riding.."
    self.miles += 10
    return self
    
  def reverse(self):      #these are methods (functions that DO something)
    print "Reversing..."
    self.miles -= 5
    return self
    
bike1 = bike(200, "25mph", 0)  #these are instances
bike2 = bike(200, "25mph", 0)
bike3 = bike(200, "25mph", 0)

print "==== Bike 1 ===="
bike1.displayinfo().ride().ride().displayinfo().reverse().displayinfo()

print "==== Bike 2 ===="
bike2.ride().ride().displayinfo().reverse().reverse().displayinfo()

print "==== Bike 3 ===="
bike3.displayinfo().reverse().reverse().reverse().displayinfo()