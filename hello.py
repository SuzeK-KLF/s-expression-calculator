import sys

def add(n1, n2):
    answer = n1+n2
    print(answer)

# def calculate(func, exp1, exp2):
#     result = 0
    


def main():
    if len(sys.argv) <=2:
        print("Please give enough info")
    else:
        function = sys.argv[1]
        print(function)
        print(len(sys.argv))
        if function == "add":
            if len(sys.argv) <4:
                print(sys.argv[2])
            else:
                num1 = int(sys.argv[2])
                num2 = int(sys.argv[3])
                add(num1, num2)

if ( __name__ == "__main__"):
    main()