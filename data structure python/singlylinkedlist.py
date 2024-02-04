# create a node class 
class Node:
    def __init__(self , data = None) -> None:
        self.data = data 
        self.next = None
    def __str__(self , data) -> str:
        return str(data)   

# singly linked list 
n1 = Node("eggs")
n2 = Node("abc")
n3 = Node("xyz")

n1.next = n2 
n2.next = n3 

current= n1
while current:
    print(current.data)
    current = current.next