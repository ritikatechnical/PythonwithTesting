class MyNewClass:
    def __init__(self):
        self.name = "Ritika"
        self._email = "ritika@gmail.com"

    def public_func(self):
        print("Public Func()")

    def __private_func(self):
        print("i can access by only inner method,i am private")

    def public_fn_private(self):
        self.__private_func()
        print(self._email)


# Security -> Not everyone can access your variables/methods, f(n)
a = MyNewClass()
a.public_func()
a.public_fn_private()
