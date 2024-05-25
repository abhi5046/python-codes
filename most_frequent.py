def frequent_num(list):
    counter=0
    num=list[0]
    
    for i in list:
        current_fre=list.count(i)
        if (current_fre>counter):
            counter=current_fre
            num=i
            
    return num
        
list=[1,2,3,4,5,2,4,4,8,9,4,5,4]
print("The most frequent number is :",frequent_num(list))


# Program to find most frequent 
def most_frequent(list):
    return max(set(list1), key=list1.count)


list1=[1,2,3,4,5,2,4,4,8,9,4,5,4]
print(most_frequent(list1))