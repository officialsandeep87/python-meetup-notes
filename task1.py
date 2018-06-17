import sys

def main():

    file_name = sys.argv[1]
    
    with open(file_name,"r") as f:
        array1 = f.readlines()
    
    for line in array1:
        ##print(line)
        line = line.strip()
        operand_one, operator, operand_two = line.split(" ",3)
        print(operand_one, operator, operand_two)


if __name__ == "__main__":
    main()
