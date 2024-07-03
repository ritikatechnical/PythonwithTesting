# program for calculation


class Calculation:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b


calci = Calculation()
print(calci.sum(10, 20))
print(calci.sub(10, 20))
print(calci.mul(10, 20))
