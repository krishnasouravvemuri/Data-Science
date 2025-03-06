import array as ar
a = ar.array('i' , [1,2,3,4,5,6,7,8,9])

reverse1 = a[::-1] # Creates a new array , reverse1 and takes the reverse of a as the input.
a.reverse() # Doesnt create a new array. Simply reverses the array.

print(*reverse1)
print(*a)