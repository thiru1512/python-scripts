import sys

def add(value1,value2):
    sum = value1 + value2
    return sum

def sub(num1,num2):
    subtraction = num1 - num2
    return subtraction


def mul(num1,num2):
    multiply = num1 * num2
    return multiply

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

print(sys.argv[0])

if operation == "addition":
    output = add(num1,num2)
    print("The sum of two numbers are :",output)
elif operation == "subtract":
    output = sub(num1,num2)
    print(output)

elif operation == "multiplication":
    #output = mul(num1,num2)
    print(f"The product of two numbers are :{mul(num1,num2)}")
else:
    print("enter correct values")





    