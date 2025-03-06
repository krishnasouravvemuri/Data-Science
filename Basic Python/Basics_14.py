from collections import ChainMap

d1 = {1 : 'a' , 2 : 'b' , 3 : 'c'}
d2 = {4 : 'd' , 5 : 'e' , 6 : 'f'}
d3 = {7 : 'g' , 8 : 'h' , 9 : 'i'}
d4 = {10 : "j", 11 : "k", 12 : "l"}

c1 = ChainMap(d3,d2,d1)
print(c1)

c2 = c1.new_child(d4)
print(c2)
