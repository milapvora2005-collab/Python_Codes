#Adding elements into list

#Initialize an empty list
a=[]

#adding 10 to an end of list
a.append(10)
print("After append(10):  ",a)

#Inserting 5 at index 0
a.insert(0,5)
print("After insert(0,5): ",a)

#Adding multiple element [15,20,25] at end.
a.extend ([15,20,25])
print("After extend ([15,20,25]): ",a)
