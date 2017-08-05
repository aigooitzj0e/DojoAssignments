names = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
animals = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def nameOfPet(name, favorite_animal):
    combo = zip(name, favorite_animal)
    print combo

print nameOfPet(names, animals)
