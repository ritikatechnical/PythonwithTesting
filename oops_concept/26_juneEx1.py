class Person:
    name = None
    age = None
    id = None

    def Walk(self):
        print("I can walk")

    def Eat(self):
        print("I can eat")

    def Talk(self, name):
        print("I can talk:" + name)


person = Person()
person.name = "Rahul"
person.age = 21
person.id = 101
person.Walk()
person.Talk("Rohan")
