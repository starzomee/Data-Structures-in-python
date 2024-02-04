from collections import deque 
stack = deque()
print(dir(stack))
stack.append(1)
stack.append(2)
stack.append(3)
stack.append("shayan")
stack.append("umar")
while stack != None:
 print(stack.pop())
print(stack)
