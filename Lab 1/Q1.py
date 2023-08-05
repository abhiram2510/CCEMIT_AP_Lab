
lenofarr=int(input("Enter the number of elements in list:"))
arr1=[0]*lenofarr
arr2=[0]*lenofarr
for i in range(lenofarr):
    arr1[i]=int(input("Enter the elements in first list:"))
for i in range(lenofarr):
    arr2[i]=int(input("Enter the elements in seonnd list:"))

print("The first list is: ",arr1)
print("The second list is: ",arr2)


newarr=[]
for i in range(lenofarr):
    if(arr1[i]%2 != 0 ):
        newarr.append(arr1[i])
    if(arr2[i]%2 == 0):
        newarr.append(arr2[i])


print("The new list is: ",newarr)
