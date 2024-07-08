def add(a,b):
    return a+b

res = lambda a,b:a+b
#print(res(1,2),add(10,20))


# Given a list and each value should get multiplied by 2
def func(a1):
    for i in range(len(a1)):
        a1[i] *= 2
    return a1

a1 = [1,2,3,4]
print(func(a1))

print("Unsing map & lambda")
a2 = [2,4,6,8]
a2 = list(map(lambda x:x*2,a2))
print(a2)

# Map(arg1,arg2)  --> arg1 = funtion(), arg2 = colletion(list,tuple etc)
l = ["1","2","3"]
print("List: ",l)
l = list(map(int,l))
print("List after using map: ",l)


#Reduce
from functools import * 

li = [1,2,3,4,5]
res = reduce(lambda x,y:x+y,li)
print(res)

# Filter
li = [1,2,3,4,5]
res = list(filter(lambda x: x%2==0,li))
ans = filter(lambda x:x<3,li)

print(res)

# Zip
l1 = [1,2,3]
l2 = ['a','b','c']
print(list(zip(l1,l2)))
print(dict(zip(l1,l2)))