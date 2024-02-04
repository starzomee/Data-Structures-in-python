class Node:
    def __init__(self , data = None  , next = None) -> None:
        self.data = data 
        self.next = next 

class linkedlist:
    def __init__(self , head) -> None:
        self.head = None  

    def insert_at_beg(self , data):
        node = Node(data , next)
        self.head = node 

        itr = self.head 
        while itr:
            itr  = itr.next 

        itr.next = node(data , next)  
    def insert_at_end(self , data ):
        if self.head is None:
            self.head = (data , None)
            return 
        
    def insert_values(self , data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data , None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1         
   
    def print(self):
        if self.head is None:
            print("LinkedList is empty")

        itr = self.head
        lnkedlst = ''
        while itr:
            lnkedlst += str(itr.data)
            itr.next 

if __name__=='__main__':
    ll = linkedlist()
    ll.insert_at_beg(28)
    ll.insert_at_beg(56)
    ll.print()

