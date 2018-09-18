def fibo(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    elif x > 2:
        return fibo(x-2) + fibo(x-1)

n = int(input("Input the length of Fibonacci sequence (n>=1): "))

for number in range(1,n+1):
    print(fibo(number),end= " ")
    
