#Python Program For Range
#To Print 54321 5432 543 54 5 Using For Loop

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print("\n")    
