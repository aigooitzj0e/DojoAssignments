class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel 
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    
    def display_all(self):
      print "Price:", self.price
      print "Speed:", self.speed
      print "Fuel:", self.fuel
      print "Mileage:", self.mileage
      print "Tax:", self.tax


car1 = car(2000, "35 MPH", "Full", "15 MPG")
car2 = car(2000, "5 MPH", " Not Full", "105 MPG")
car3 = car(2000, "15 MPH", "Kind of Full", "95 MPG")
car4 = car(2000, "25 MPH", "Full", "25 MPG")
car5 = car(2000, "45 MPH", "Empty", "25 MPG")
car6 = car(20000000, "35 MPH", "Empty", "15 MPG")


print "===== CAR 1 ====="
car1.display_all()
print "===== CAR 2 ====="
car2.display_all()
print "===== CAR 3 ====="
car3.display_all()
print "===== CAR 4 ====="
car4.display_all()
print "===== CAR 5 ====="
car5.display_all()
print "===== CAR 6 ====="
car6.display_all()