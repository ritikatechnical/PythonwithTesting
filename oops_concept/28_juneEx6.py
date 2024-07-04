# Web Automation - Selenium


class FbLoginPage:
    email = input("Enter the email----")
    password = input("Enter the password----")

    def __init__(self, email_id, password_arg):
        self.email = email_id
        self.password = password_arg

    def submit_login(self):
        if self.email == "ritika@gmail.com" and self.password == "Pass123":
            print("you can login")
        else:
            print("Not allowed to login")

obj1 = FbLoginPage("ritika@gmail.com", "Pass123")
obj1.submit_login()

obj2 = FbLoginPage("pramod@gmail.com", "123")
obj2.submit_login()