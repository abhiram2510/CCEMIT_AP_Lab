samplelist=[]
duplicate_elements=[]
no_of_elements = int(input("Enter the number of elements in the list:"))
for i in range (0,no_of_elements):
    a=int(input("Enter the element:"))
    samplelist.append(a)

print("The sample list given by user is;",samplelist)

for i in range(0,no_of_elements):
    for j in range(i,no_of_elements):
        if(samplelist[i] == samplelist[j]) and (samplelist[i] not in duplicate_elements):
            duplicate_elements.append(samplelist[i])
        elif(samplelist[i] not in duplicate_elements):
            duplicate_elements.append(samplelist[i])

print("The unique elements are:",duplicate_elements)
