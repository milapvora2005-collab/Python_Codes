#Write a python script for CGST and SGST

a=input("Enter the item of a:- ")
b=150
c=2
d=b*c #total price of sandwich
print("total price:- ",d)
gst=float(input("Enter gst_rate:- "))
cgst=gst/2
print("value of cgst:- ",cgst)
sgst=gst/2
print("value of sgst:- ",sgst)
e=d+(d*(cgst)/100)+(d*(sgst)/100)
print("total amount:- ",e)
