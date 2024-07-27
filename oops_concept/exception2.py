try:
    with open('input.txt') as f:
        lines = f.readlines()
        print(lines)

except FileNotFoundError as fnfe:
    print("i am not exixt")

finally:
    print("I am closing this file")
    f.close()
