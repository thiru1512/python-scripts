a = int(input("Enter the value for num1:"))
b = int(input("Enter the value for num2:"))

def add():
    addition = a + b
    print(f"The sum of two numbers:{addition}")
    #print("The sum of two numbers:"+ str(addition))
    #print("The sum of two numbers:",addition)

def mul():
    multiply = a * b
    print(f"The Multiplication of two numbers:{multiply}")

def div():
    division = float(a) / float(b) 
    print(f"The Division of two numbers:{division}")

def mod():
    modulo = a % b
    print(f"The Modulo of two numbers:{modulo}")


add()
mul()
div()
mod()



