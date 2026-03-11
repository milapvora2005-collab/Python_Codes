#Write a python script to print simple interest using float and find compound interest half yearly.

p=int(input("Enter the value of p:- "))
r=float(input("Enter the value of r:- "))
t=int(input("Enter the value of t:- "))

I=(p*r*t)/100 
print("Simple interest is:- ",I)

#calculate compound interest
tmp=1+r/100
Amount=(p*(pow(tmp,t)))
print("Amount is: ",Amount)
CI=Amount-p
print("compound interest is: ",CI)

#calculate compound interest half yearly
tmp=1+r/200
Amount=(p*(pow(tmp,2*t)))
print("Amount is: ",Amount)
CI=Amount-p
print("compound interest half yearly: ",CI)

