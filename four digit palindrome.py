#Python Program For 4-digit Palindrome Number

num=int(input("Enter any 4-digit Number: "))
fd=num//1000
ld=num%10

if fd==ld:
    print("Number is palindrome")

else:
    print("Number is not palindrome")

print("Program is over!!")    
