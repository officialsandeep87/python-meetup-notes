import sys

def main():

    file_name = sys.argv[1]
    
    with open(file_name,"r") as f:
        array1 = f.readlines()
    
    for line in array1:
        print(line)

if __name__ == "__main__":
    main()
