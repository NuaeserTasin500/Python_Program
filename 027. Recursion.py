## Recursion

#factorial function returning recursion 
def fact(n):
    if (n==0):
        return 1
    else:
        return n * fact(n-1) #recursive return

a = int(input("Enter a number for factorial = "))
print(f'{a}! = {fact(a)}') 


# Fibonacci number <AI>
def fib(n):
    if (n == 0):
        return n
    elif(n == 1):
        return n
    else:
        return fib(n-1) + fib(n-2) #recursive return
def fib_seq(x):
    for i in range(0, x):
        if(i==x-1):
            print(f'{fib(i)}' )
        else:
            print(f'{fib(i)}, ', end="\0")

a = int(input("Enter a number for fibonacci sequence = "))
print(f'{a}fbnc = ', end='\0') 
fib_seq(a) 
