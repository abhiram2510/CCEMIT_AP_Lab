fileObj  = open('file3.txt','r+')
Lines =  fileObj.readlines()
Lines.reverse()
fileObj.seek(0)
for line in Lines:
    fileObj.write(line)
    fileObj.write("\n")