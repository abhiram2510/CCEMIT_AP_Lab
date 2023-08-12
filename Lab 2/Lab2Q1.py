str = input("enter the string:")
words = []
words = str.split()
print(words)
strdict = {}
for key in words:
    strdict[key]=words.count(key)
print("The Dictionary is :",strdict)
