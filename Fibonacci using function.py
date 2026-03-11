def fib(n):
    a=0
    b=1
    if n==1:
        return 1
    elif n<a:
        return 0
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)

n=int(input("enter a no.: "))
fib(n)
