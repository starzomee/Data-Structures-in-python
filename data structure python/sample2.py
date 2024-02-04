from collections import deque 
dq = deque('shayan')
dq.append('abc')
dq.append('d')
dq.appendleft('e')
dq.extend('fgh')
dq.extendleft('xyz')
print(dq.pop())
print(
dq.popleft())
print(dq.rotate(6))
print(list(iter( 3 , 9)))
print(dq)
