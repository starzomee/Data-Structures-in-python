list1 = [1 ,2 ,3 , "shayan"]
print(list1)
# append() , extend() , insert()
list1.append(2 , )
list1.append((2  , 0 ))
list1.extend((2 ,  0 ))
list1.insert(3 , 5)
print(list1)
print(list1[-3])
print("==================||=====================")
# del() , pop() , remove()
del list1[3]
print(list1)
a = list1.pop(1)
print(a)
list1.remove(2)
print(list1)
print("==================||=====================")
# printing 
print(list1) # whole list printing
print(list1[1]) # index 1 print
print(list1[0:2:2]) # index 0 to 2 and skip 2 elements 
print(list1[::-1]) # print list in backwards 
print("==================||=====================")
# sorting lists 
list2 = [1 , 3, 4, 5, 66 ,7 , 0 , 2383 , 2]
print(sorted(list2))
print(list2)
list2.sort(reverse=True)
print(list2)
print("==================||=====================")
# index and count 
print(list2.index(2))
print(list2.count(1))
print("==================||=====================")
