n = int(input("enter the number:"))
def fibo(n):
    a = 0
    b = 1
    count = 1

    if n <= 0:
        print("enter number greater than zero")
    else:
        while count <= n: 
            print(a)
            sum = a + b
            a = b
            b = sum
            count+=1


fibo(n)


