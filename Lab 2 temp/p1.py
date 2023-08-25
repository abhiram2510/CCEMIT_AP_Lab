str=input("enter the String : ")
words = []
words = str.split()
myDict = {}
for key in words:
    myDict[key] = words.count(key)
print("Dict Items  :  ",  myDict)
print("total unique items count: ",len(myDict))