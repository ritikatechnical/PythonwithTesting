list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def outer_function(list1):
    list1.append(199)
    return list1


print(outer_function(list1))


# lamda function to do the task in one line

def double_salary(salary):
    return salary * 2


new_salary = double_salary(salary=100)
print(new_salary)

# by lamda function
new_salary = lambda salary: salary * 2
print(new_salary(100))
