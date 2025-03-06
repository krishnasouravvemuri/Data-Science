from collections import ChainMap

d1 = {1 : 'a' , 2 : 'b' , 3 : 'c'}
d2 = {4 : 'd' , 5 : 'e' , 6 : 'f'}
d3 = {7 : 'g' , 8 : 'h' , 9 : 'i'}

c = ChainMap(d3,d2,d1)

print(*c)