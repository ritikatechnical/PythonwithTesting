# function
# block of code - which can executed or reused.


def say_hello1():  # No ReturnType function with no parameter /arguments
    print("Hello")


say_hello1()  # function call


def say_hello2(name):  # NO Return Type function with parameter / arguments
    print("Hello:", name)


say_hello2("Ritika")
say_hello2("Rohan")


def say_hello_arg_default(name="rudra"):  # No return type with deafult argument
    print(f"Hello {name}")


say_hello_arg_default()
say_hello_arg_default("ritika")
say_hello_arg_default(name="prajna")


def sum_arg(a, b):
   return a + b


n1 = sum_arg(2, 3)
print(n1)
