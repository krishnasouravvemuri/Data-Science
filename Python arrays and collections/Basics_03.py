import array as ar
a = ar.array('i' , [1,2,3,4,5,6,7,8,9])
a.append(10) # Takes only element as the attribute
a.insert(10 , 11) # Takes the index as well as the element
print(*a)
