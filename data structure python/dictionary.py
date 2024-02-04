print("==================||=====================") 
# create a dictionary 
dict1 = {1 : "java " , 2: "python " , 3: "machine learning"}
print(dict1)
print("==================||=====================")
# modification 
dict1[1]  = "HTML"
print(dict1)
print("==================||=====================")
# adding values to dictionary
dict1[4] = "deep learning"
print(dict1)
print("==================||=====================")
# pop usage 
dict1.pop(1)
print(dict1)
print("==================||=====================")
# pop and return value 
print(dict1.pop(3))
print(dict1)
print("==================||=====================")
# pop the end item 
print(dict1.popitem())
print(dict1)
print("==================||=====================")
# item , values and keys printing 
print(dict1.items())
print(dict1.keys())
print(dict1.values())