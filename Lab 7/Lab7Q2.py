fileObj = open("file2.txt","r")
myDict = {}
Lines = fileObj.readlines()
for line in Lines:
    words= line.split()
    for word in words:
        if word not in myDict:
            myDict[word] = 1
        else:
            myDict[word] = myDict[word]+1


print(myDict)