n = int(input("enter the number:"))

def fibo(n):
    a = 0
    b = 1
    count  = 1

    if n <= 0:
        print("enter non zero integer")

    elif n == 0:
        print("enter number greater than zero")

    else:
        for count in range(1,n):
            print(a)
            sum = a + b
            a = b
            b = sum


fibo(n)



