#Find sum of first n natural numbers using recursion

def sumofnat(n):
    if n==1:
        return 1
    else:
        return n+sumofnat(n-1)

print(sumofnat(5))    
