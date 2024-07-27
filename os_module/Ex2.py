import os

file = os.open("foo.txt", os.O_RDONLY)
os.write(file, b"\nAdded new Test")

os.close(file)
