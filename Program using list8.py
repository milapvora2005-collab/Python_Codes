#Removing element from the list
a=[10,20,30,40,50]

#Remove the first occurance of 30
a.remove(30)
print("After remove(30): ",a)

#Remove element at index 1(20)
popped_val=a.pop(1)
print("popped element: ",popped_val)
print("After pop(1): ",a)

#Delete the first element(10)
del a[0]
print("After del_a[0]: ",a)
