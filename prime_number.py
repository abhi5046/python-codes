num=int(input("enter the number:"))
flag=False
#check for 1 
if num==1:
    print(f'tne {num} is not a prime number')
elif num>1:
    # check for rest of number
    for i in range(2,num):
        if(num % i)==0:
            flag=True
            break

if flag:
    print(num,"is not a prime number")
else:
     print(num,"is a prime number")

