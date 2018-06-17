try:
    with open("test2.txt","r") as f:
        data = f.readlines()
except FileNotFoundError:
    print("file specified not found")

