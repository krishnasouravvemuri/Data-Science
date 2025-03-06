import array as ar
a = ar.array('i' , [1,2,3,4,5,6,7,8,9])

print(*a[:]) # Slicing. since nothing is mentioned , prints the array as usual.
print(*a[5:]) # Prints from the 5th element to the end of the array.
print(*a[::2]) # Takes a step of 2 in between the elements when printing.