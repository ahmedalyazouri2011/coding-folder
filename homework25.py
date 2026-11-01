
class Dog:
    animal = "Dog"  # Class variable

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Max", "German Shepherd")
dog2 = Dog("Buddy", "Golden Retriever")

print("Dog 1 Details:")
print("Animal:", dog1.animal)
print("Name:", dog1.name)
print("Breed:", dog1.breed)

print()

print("Dog 2 Details:")
print("Animal:", dog2.animal)
print("Name:", dog2.name)
print("Breed:", dog2.breed)
