import sys

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

try:
    div = num1 / num2
    print(div)

except ZeroDivisionError:
    print(f"{num1} cannot be divided by zero")
