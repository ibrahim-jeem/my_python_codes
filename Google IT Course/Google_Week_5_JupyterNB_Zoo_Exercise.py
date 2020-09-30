#This code will deside / catogorise which animal belongs to wich catagory

class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category


class Reptiles(Animal):
  name = " "
  category = "reptiles"

class Mamels(Animal):
  name = " "
  category = "mamels"

class Birds(Animal):
  name = " "
  category = "amphibians"

class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()


turtle = Reptiles("Slowee") #create an instance of the Turtle class
snake = Reptiles("Python") #create an instance of the Snake class
tiger = Mamels("Sher Khan")
perrot = Birds("Robin")

zoo.add_animal(turtle)
zoo.add_animal(snake)
zoo.add_animal(tiger)
zoo.add_animal(perrot)

print(zoo.total_of_category("reptiles")) #how many zoo animal types in the reptile category

# print(perrot.category)
# print(perrot.name)

# print(zoo.current_animals)


