def with_argument(*args):
    for arg in args:
        print(arg)


with_argument("abc", 45, 67, "hello")


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    for topping in toppings:
        print(topping, end='\n')


make_pizza("tomato", "Olive", "Cheese")
