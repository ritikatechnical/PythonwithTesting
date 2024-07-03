class Dog:
    name = None
    Location = None

    def __init__(self, name, location):
        self.name = name
        self.location = location


    def sleep(self):
        print("I can Sleep")


dog1 = Dog("Rocky",  "Dubai")
print(dog1.name, dog1.location)
print(f"{dog1.name}  is in : {dog1.location}")

# print(dog.name)
# dog.location = "Dubai"
# print(dog.location)
# dog.sleep()

