# using nested for loop
# sampale 1
matrix=[]
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
# print(matrix)

# sampale 2 : get odd number from given matrix and remove duplicate value
matrix1=[[1,2,3,4,5,6],[11,1,2,14,15,16,17,15]]
odd_number=[]
for row in matrix1:
    for element in row:
        if element % 2 != 0:
            odd_number.append(element)

odd_number =set(odd_number)
print(odd_number)