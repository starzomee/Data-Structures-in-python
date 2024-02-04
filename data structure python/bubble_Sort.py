def bubble_sort(elements ):
    size = len(elements )
    for i in range(size -1):
     swapped = False
     for j in range(size - 1 ):

        if elements[j] > elements[j+1]:
            temp = elements[j]
            elements[j] = elements[j + 1]
            elements[j+ 1] = temp 
            swapped = True 
     if not swapped:
       break        
if __name__ == '__main__':
   elements = [ 12 , 34, 1,34 , 56  ,78, 45 , 2 , 3,5 ]
   bubble_sort(elements)
   print(elements)
   






