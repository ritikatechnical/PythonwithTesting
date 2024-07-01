# check input field is Leap year or not

# divisible by 4 and not divisible by 100 or divisible by 400


year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("give year is leap year")
else:
    print("given year is not leap year")
