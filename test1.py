import os

file_name = "wrong"

print(os.path.exists(file_name))

try:
    with open("test2.txt","r") as f:
        data = f.readlines()



except FileNotFoundError:
    print("file specified not found")

