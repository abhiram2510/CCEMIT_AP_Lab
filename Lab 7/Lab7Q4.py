fileObj = open("input.txt","r")
fileObj1 = open("vaild.txt","w")
domains = ["abhiram@gmail.com","@yahoo.com","@manipal.edu","@reddit.com"]
lines = fileObj.readlines()
print(lines)
for line in lines:
    if line in domains:
        print(line)



fileObj1.close()
fileObj.close()

