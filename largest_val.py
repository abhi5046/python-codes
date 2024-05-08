# list1=[1,2,3,4,5,6,7,90,45,60,100,5,6,4,8]
# print(max(list1))

def largest_number(numbers):
    largest=numbers[0]
    for num in numbers:
        if num > largest:
            largest=num
    return largest

# num=[10,20,30,40,100,56,312,111,54,221]
num=[]
# for i in range(5):
#     num.append(i)
print("enter -1 to stop")
while True:
    n=int(input("Enter the number:"))
    num.append(n)
    if n== -1:
        break

num.pop()


print(num)
largest_num=largest_number(num)
print(f'the largest number from list is {largest_num}')
