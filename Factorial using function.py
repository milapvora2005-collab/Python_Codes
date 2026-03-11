#To Print Factorial Of A Number Using Function

def fact(n):
    if n<=1:
        return 1
    else:
        n=n*fact(n-1)
        return n

n=int(input("enter any number: "))
print("Factorial of",n,"is",fact(n))
