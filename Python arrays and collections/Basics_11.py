from collections import defaultdict

d = defaultdict(int)

# Predefined keys with initial values
d[5] = 10
d[2] = 3

L = [5, 5, 2, 6, 6, 1, 5]

for i in L:
    d[i] = d[i] + 1

print(d)
