#Python Program To Find Min. From Three Numbers.

a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
c=int(input("Enter 3rd Number: "))
if a<=b and a<=c:
    print("a is min.")
elif b<=c and b<=a:
    print("b is min.")
else:
    print("c is min.")

print("Program is over!")    
