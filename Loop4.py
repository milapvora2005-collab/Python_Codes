#Python Program For Range
#To Print 5 54 543 5432 54321 Using Loop
n=5
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print("\n")    
