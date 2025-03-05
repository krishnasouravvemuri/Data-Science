import array as ar
list = [10,20,30,40,50,60]
a = ar.array('i' , list) # made the list into a array.

for i in a :
    print(i , end = ",")

print("")
print(*a)
