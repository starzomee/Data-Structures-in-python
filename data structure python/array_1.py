# Question store apple stock prices  for 5 days 
# what is the price on day 1 and on day 5 
Apples_stock = [200 , 240 , 340 , 400 , 500]
print(Apples_stock[1])
print(Apples_stock[4])
print(print("=================='SCENARIOS'====================="))
print("==================SCENARIO NO: 1=====================")
# WHAT WAS THE PRICE ON DAY : 3 
print(Apples_stock[2])
# ORDER OF COMPLEXITY IS O(1) , CONSTANT TIME COMPLEXITY 
print("==================SCENARIO NO: 2=====================")
# ON WHAT DAY THE PRICE WAS 340 
for i in range(len(Apples_stock)):
    if Apples_stock[i] == 340:
        print(i) 
# the loop will iterate n times so therefore complixety is o(n)
print("==================SCENARIO NO: 3=====================")
# print all the prices
print(Apples_stock)
#for price in range(len(Apples_stock)):
#    print(price)
# o(n) complixety 
print("==================SCENARIO NO: 4=====================")
#insert 284 at index 1 
#Apples_stock.index(1 , 284)   
#print(Apples_stock)
print("==================SCENARIO NO: 5====================")
#Delete elements at index 1
Apples_stock.remove[1]
print(Apples_stock)