import array as ar
a = ar.array('i' , [1,2,3,4,5,6,7,8,9])
a.remove(2) # Takes the magnitude of the element
print(*a)
a.pop(2) # Takes the index of the element
print(*a)