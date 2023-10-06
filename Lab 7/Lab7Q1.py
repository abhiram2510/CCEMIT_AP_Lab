fileObj = open("file1.txt","r")
Lines  = fileObj.readlines()
print("Number of lines =", len(Lines))
wordCount = 0
characterCount = 0
for line in Lines:
    words = line.split()
    for word in words:
        wordCount=wordCount+1
        characterCount= characterCount+ len(word)

print("Number of words:",wordCount)
print("Number of characters:",characterCount)