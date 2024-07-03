# take input from user
class Student:
    name = input("Enter the name")
    age = int(input("Enter the age"))

    def __inti__(self, name, age):
        self.name = name
        self.age = age


stu = Student()
print("Program is done")
print(f"{stu.name} age is {stu.age}")
