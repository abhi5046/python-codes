def factorial(n):
    if(n<=1):
        return 1
    else:
        return n * factorial(n-1)

n=int(input("Enter the number:"))
result=factorial(n)
print(f'factorial of number {n} is {result}')