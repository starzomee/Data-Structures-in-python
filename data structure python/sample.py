a = [1 , 2, 3, 4]
b = a 
a.append(8)
print(b)
print("=====================||===========================")
z = 1 
print(type(z)) # int 
z = z + 0.1 
print(type(z)) # float 
print("=====================||===========================")
a = 10 ; b = 20 
def my_function():
    global a 
    a =  11 ; b = 21
my_function()
print(a)
print(b)    
print("=====================||===========================")
x = " one"
if x == 0:
    print("yes")
elif x == 1: 
    print("no"
          )
else:
    print("something else")        
print("=====================||===========================")
x = 0 
while x < 5:
    print(x)
    x += 1
print("=====================||===========================")    
name = " Muhammad shayan umar "
print(name[1])
print(name[0:22])
print(name.count)
name[1 + 2]
print(name)
print("=====================||===========================") 
greet = "hello world"
greet[1+2]
print(greet)
for i in enumerate(greet[0:5]):
    print(i)

print(greet[:5] + ' ' +   " wonderful"   +  '  '   + greet[5:])

x = '3' ; y = '2'
print(int(x)+int(y))
x = 3 ; y = 2 
print(x+y)
print("=====================||===========================") 
x = 2 ; y = 3 ; z = 4 
list1 = [ x ,  y , z]
list2 = list1 
list2[2] = 5  
list2.append(9)
list2.insert(2 , 100)
print(list2)
print("=====================||===========================")
items = ["rice" , 2.8 , 8 ] , ["flour" , 1.9 , 5] , ["corn" , 4.7 , 6]
for item in items:
    print("product: %s price: %.2f  Quality: %i" % (item[0] , item[1] , item[2]) )

items[1][1] = items[1][1] * 1.2
print(items[1][1])
print("=====================||===========================")
l = [ 2 , 4 , 8 , 16]
l = [i**3 for i in l]
print(l)
print("=====================||===========================")
def f1(x) : return x*2
def f2(x) : return x*4 
lst = []
for i in range(16):
    lst.append(f1(f2(i)))
print(lst)
print([f1(x)   for x in range (64)     if x in [f2(j) for j in range(16)]])
print("=====================||===========================") 
list = [[1 , 2, 3] , [4, 5, 6]]
list = [i*j for i in list[0]  for j in list[1]]
print(list)
print("=====================||===========================")
words = "Sometimes i fells a devil inside me , who's gonna kill everyone ".split()
lit = [[word , len(word)] for word in words ]
print(lit)
print("=====================||===========================")
def greeting(language):
    if language == 'eng':
        return  "hello world"
    elif language == 'french':
        return "bajour de la mode"
    else:
        return "language not supported"    
l = [greeting('eng') , greeting('french') , greeting('germon')]
print(l[2])
print("=====================||===========================")
def callf(f):
    lang = 'eng'
    return (f(lang))    
print(callf(greeting))
print("=====================||===========================")

