class Myclass:
    name = None



    def __init__(self, name):
        self.name = name



myobj = Myclass("Rahul")
myobj.__balance = 50000
myobj.sal = 10000
print(f"{myobj.name} has balance {myobj.__balance} and sala {myobj.sal}")
