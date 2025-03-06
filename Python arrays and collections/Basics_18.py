from collections import deque

dq = deque([10,20,30,40,50,60])
print(dq)

dq.pop() # pops/removes the element from the last
print(dq)

dq.popleft()
print(dq) # pops/removes the left most element