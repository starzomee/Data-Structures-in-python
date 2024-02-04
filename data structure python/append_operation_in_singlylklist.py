# create a class named as node 
class Node:
    def __init__(self) -> None:
        self.tail = None 
    def append(self , data):
        # encapsulate data in node 
        node = Node(data)
        if self.tail == None:
            self.tail = node 
        else:
            current = self.tail 
            while current.next:
                current = current.next 
                current.next = node        
x = Node()
x.append('abc')
x.append('zyx')      

current = x.tail 
while current:
    print(current.data)
    current = current.next
    