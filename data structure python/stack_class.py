from collections import deque 
class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self , value ):
        self.container.append(value)

    def pop(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self)    :
        return len(self.container)
    
s = Stack()
s.push(24)
print(s)

