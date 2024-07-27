try:
    a = int(input("Enter the integer number"))
    b = int(input("Enter another integer number"))
    result = a / b
    print(result)
except ZeroDivisionError as zero:
    print(zero)
    print("You can't divide by zero")

except  ValueError as ve:
    print(ve)
    print("Please enter integer number only")

finally:

    print("Thanks for using this program")