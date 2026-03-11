#Find 2^n using recursion

def power(base,pw):
    if pw==0:
        return 1
    else:
        return base*power(base,pw-1)

print(power(2,7))    
    
