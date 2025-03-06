from collections import deque

dq = deque([10,20,30,40,50,60])
print(dq)

dq.append(70) # Adds the element at the last
print(dq)

dq.appendleft(0) # Adds the element at the beginning
print(dq)