class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        print ("Walking...")
        return self

    def run(self):
        self.health -= 5
        print ("Running...")
        return self

    def displayhealth(self):
        print self.health
        return self



class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150




class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self 

    def displayhealth(self):
        super(Dragon, self).displayhealth()
        print self.health, "I am a dragon"
        return self




print "===== ANIMAL ====="
animal1 = Animal("christian", 100)
animal1.walk().walk().walk().run().run().displayhealth()

print "===== DOG ====="
dog1 = Dog("christian", 100)
dog1.walk().walk().walk().displayhealth()

print "===== DRAGON ====="
dragon1 = Dragon("dragomire", 100)
dragon1.fly().displayhealth()