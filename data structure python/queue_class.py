from collections import deque
class Queue:
    def __init__(self) -> None:
        self.buffer = deque()

    def enqueue(self , val):
        return self.buffer.appendleft(val)
    def dequeue(self ):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0 
    def size(self):
        return len(self.buffer)
    
q = Queue()
q.enqueue({
    1 : "java " , 2: "python " , 3: "machine learning"
})   
print(q.buffer)
