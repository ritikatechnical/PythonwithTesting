class Car:
    name = None
    make = None
    model = None

    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model

    def start_engine(self):
        print("My new car with the name " + self.name)
        print("My new car with the name " + self.make)
        print("My new car with the name " + self.model)


lambo = Car("lambo", "V2", "2024")
lambo.start_engine()

xuv = Car("XUV", "V6", "2023")
xuv.start_engine()