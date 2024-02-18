class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Zoo:
    def __init__(self):
        self.list_animals = []

    def add_animal(self, animal):
        self.list_animals.append(animal)
        print(f"{animal.species} {animal.name} added to list.")

    def remove_animal(self, animal):
        for i in self.list_animals:
            if animal == i:
                self.list_animals.remove(i)


Cat = Animal("Mark", "Cat")
Dog = Animal("John", "Dog")
Bear = Animal("Fred", "Bear")
zoo = Zoo()

zoo.add_animal(Cat)
zoo.add_animal(Dog)
zoo.add_animal(Bear)

zoo.remove_animal(Dog)

print("Animals that are in the zoo:")
for animal in zoo.list_animals:
    print(f"{animal.species} {animal.name}")
