#Python Program For Range
#To Print 11111 2222 333 44 5 Using Loop

n=5
for i in range(n):
    for j in range(n-i):
        print(i+1,end=" ")
    print("\n")    
