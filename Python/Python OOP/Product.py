class product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = "Sold"
        return self

    def tax(self):
        tax = 0.15
        self.price = self.price + self.price * tax
        return self
    
    def re_turn(self, reason):
        if reason == "defective":
            self.status = "Defective"
            self.price = 0
        if reason == "unopened":
            self.status = "For Sale"
        if reason == "opened":
            discount = 0.20
            self.status = "Used"
            self.price = self.price - self.price * discount
        return self
    
    def display_all(self):
        print "Price:", self.price
        print "Item Name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        return self
        
product1 = product(199, "headphones", "1lbs", "beats", 50, "for sale")

product1.tax().sell().display_all()
product1.re_turn("opened").display_all()