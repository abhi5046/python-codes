# find duplicatae number in python
list1=[1,2,3,4,4,5,6,8,2,3]
list2=[]
dup={x for x in list1 if list1.count(x)>1}
list3=[]
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        list3.append(i)
        
        
print(dup)
print(list3)
print(list2)

