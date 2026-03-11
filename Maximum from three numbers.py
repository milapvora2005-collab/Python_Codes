#Python Program To Find Max. From Three Numbers.

a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
c=int(input("Enter 3rd Number: "))
if a>=b and a>=c:
    print("a is max.")
elif b>=c and b>=a:
    print("b is max.")
else:
    print("c is max.")

print("Program is over!")    
