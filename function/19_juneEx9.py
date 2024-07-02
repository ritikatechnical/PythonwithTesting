def outer_function():
    a = 30
    def inner_function():
        print(a)

    inner_function()

    def inner_function2():
        print(a)

    inner_function2()


outer_function()
