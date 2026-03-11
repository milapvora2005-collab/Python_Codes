a = [8, 3, 5, 1, 9, 12]

# Initialize "largest" value with first element of list
largest = a[0]

# Iterate through list to find largest element
for val in a:
  
    # If current value is largest than current smallest value
    if val > largest:
      
        # Update the largest value
        largest = val

print(largest)
