class Fblogin:
    __username = None
    __password = None
    name = None
    __email = None

    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email
        print("Constructor is called")


    def submit_login(self):
        if self.__username == "python" and self.__password == "pass123" and self.__email == "abc1@gmail.com":
            print("you can login")
        else:
            print("Not allowed to login")


fbobj = Fblogin("python", "pass123", "abc@gmail.com")
fbobj.submit_login()
fbobj.name = "Rohan"
print(fbobj.name)
