# def find_common_elements(list1, list2):
#     common_elements = []
#     for item in list1:
#         if item in list2:
#             common_elements.append(item)
#     return common_elements

def comman(l1,l2):
    coman_ele=[]
    for i in l1:
        for j in l2:
            if i==j:
                coman_ele.append(i)
    return coman_ele
# Test the function
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
# common = find_common_elements(list_a, list_b)
common=comman(list_a,list_b)
print(common)