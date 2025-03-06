from collections import defaultdict # Retunrs the count of each element.

d = defaultdict(int) # Creates a dictionary with default value 0 for missing keys.

L = [5,5,5,5,2,5,6,6,6,6,6,1,0,0,2,8,8,3,4,5,3,6,9,8,7,1,2]

for i in L:
    d[i] = d[i] + 1
print(d) # If there are keys, they will be printed. Else a key is created and is given the value of number of occurances