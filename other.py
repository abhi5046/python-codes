# info={"emp_id":1,"name":"Abhishek","salary":100001.50,"city":"satara"}
# print(info)
# print(type(info))
# print(info.keys())
# for key in info.keys():
#     print(f"thay key of info is {key} and the value is {info[key]}")


# tech={111:50,112:80,113:90,114:95,115:30}
# bpo={201:40,202:80,203:80,204:95}
# #tech.update(bpo)
# print(tech)
# tech.pop(115)
# print(tech)
# bpo.popitem()
# print(bpo)
# del tech[112]
# print(tech)


# for i in range(5):
#     print(i)

# else:
#     print("sorry we couden't print value")

# for i in []:
#     print(i)
# else:
#     print("their is no i")

# for  i in range(6):
#     print(i)
#     if i==4:
#         break
# else:
#     print("sorry !")

# i=0
# while i<6:
#     print(i)
#     i=i+1
#     if i==4:
#         break
# else:
#     print("sorrry !!")

# for i in range(6):
#     if i==5:
#         break
#     print("the itration no {} in for loop".format(i+1))
    
# else:
#     print("else block in loop")
# print("out of loop")

#try catch in python
# try:
#     print("Multiplication table")
#     num=int(input("Enter the number :"))

#     for i in range(1,11):
#         print(f"the multiplication table is {num}x{i}={num*i}")
# except Exception as value:
#     print("enter numeric data")

# print("some imp code")
# print("more imp code")

# try:
#     a=30
#     b=0
#     print(a/b)
# except Exception as divisionbyzero:
#     print("soory you can't divide by zero")
# try:
#     num=int(input("Enter Number:"))
#     a=[4,5,6]
#     print(a[num])
# except ValueError:
#     print("number enter is not int")
# except IndexError:
#     print("acessing element from out of list")
# except TypeError:
#     print("Somthing went wrong")


# def fun1():
#     try:
#         num=int(input("Enter Number:"))
#         a=[4,5,6]
#         print(a[num])
#         return 1
#     except :
#         print("aacessing element out of the list")
#         return 0
#     # finally:
#         # print(" i always execute")
#     print("i not always execute")

# x=fun1()
# print(x)

def rev(num):
    num
    s=str(num)
    revstr=(s[::-1])
    val=(int(revstr))
    print(val)
    print(type(val))

rev(556)