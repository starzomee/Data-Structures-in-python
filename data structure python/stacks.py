# create a node class 
class Node:
    def __init__(self ,  data = None ) -> None:
        self.data = data 
        self.next = None
        # create a stack class
class Stack:
      # create a constructor function __init_ (self)
    def __init__(self) -> None:
        self.top = None 
        self.size = 0    
    # PUSH OPERATION 
    # create a function name as push pass self and data 
    def push(self  , data): 
        # create a node & pass data to that node use the Node class 
        node = Node(data)         
        if self.top:
            # node next == top so set top to node 
            node.next = self.top
            self.top = node 
        else:
            # else just incease size by one if node == top 
            self.top = node 
        self.size += 1 

    # POP OPERATION 
    def pop( self , data ):
        if self.top:
            data = self.top.data 
            self.size -= 1 
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None 
                return data 
        else: 
            return None              
    def peek(self):
        if self.top:
         return self.top.data 
        else:
            return None 
        
s = Stack()
print(s.push(12))
print(s.push(23))
print(s.push(45))



