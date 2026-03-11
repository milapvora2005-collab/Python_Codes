#Program For Fibonacci Series

a=0
b=1
print(a,b,end=" ")
for i in range(1,6):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
