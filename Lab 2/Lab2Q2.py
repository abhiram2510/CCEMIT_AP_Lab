#Taking the total number of rows and columns for each matrix--------
row1=int(input("Enter the number of rows in the first matrix:"))
column1=int(input("Enter the number of columns in the first matrix:"))
row2=int(input("Enter the number of rows in the second matrix:"))
column2=int(input("Enter the number of columns in the second matrix:"))
mat1=[]
mat2=[]

#Taking input for both matrices

for i in range(row1):
    rows=[]
    for j in range(column1):
        element= int(input("Enter the elements row wise:"))
        rows.append(element)
    mat1.append(rows)

for i in range(row2):
    rows=[]
    for j in range(column2):
        element= int(input("Enter the elements row wise:"))
        rows.append(element)
    mat2.append(rows)



#Putting the values into a dictionary
dict1={}
dict2={}
matrix1=[]
matrix2=[]
for i in range(row1):
    for j in range(column1):
        if mat1[i][j] != 0:
            dict1[i,j] = mat1[i][j]

for i in range(row2):
    for j in range(column2):
        if mat2[i][j] != 0:
            dict2[i,j]=mat2[i][j]

print(dict1)
print(dict2)
#adding the values whose keys are the same

arr=[];

for key1 in dict1:
    for key2 in dict2:
        if key1 == key2:
            arr.append(dict1[key1]+dict2[key2])
            break
        elif key1 in dict1:
            arr.append(dict1[key1])
            break
        else:
            arr.append(dict2[key2])
            break

print(arr)

