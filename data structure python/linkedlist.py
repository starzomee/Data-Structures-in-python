class Node:
    def __init__(self , data=None , next = None)-> None:
        self.data = data 
        self.next = next 

class LinkedList:
    def __init__(self  ) -> None:
        self.head = None 

    def insert_at_beg(self , data):
        node = Node(data , self.head)
        self.head = node 
        
        itr = self.head 
        while  itr.next:
            itr = itr.next 

        itr.next = Node(data , None)        

    def print(self):
        if self.head is  None:
            print("My linkedlst is empty")
            return 
        
        itr = self.head 
        llist = ''
        while itr:
            llist += str(itr.data) + '-->'
            itr = itr.next
            print(llist)

    def insert_at_end(self , data):
        if self.head is None:
            self.head = Node(data , None)
            return 
        
    def insert_values(self , data_list):
        self.head = None 
        for data in data_list:
            self.insert_at_end(data)   
    def get_length(self):
        count = 0 
        itr = self.head 
        while itr:
            itr = itr.next    
            count +=1    

    def remove_at(self , index):
        if index<=0 and index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0 :
            self.head = self.head.next 
            return 
        count = 0 
        itr = self.head 
        while itr:
            if count == index -1:
                itr.next = itr.next
                break
            itr.next 
            count += 1 




if __name__=='__main__':
    ll = LinkedList()
    ll.insert_at_beg(20)
    ll.insert_at_beg(30)
    ll.insert_at_end(23)
    ll.remove_at(2)
    # ll.insert_values("shayan")
    ll.print()            
         