n=int(input("Maximum number:"))
count=1
count1=0
for i in range(1,n+1):
    print(i,end=" ")
    count1=count1+1
    if(count1 == count):
        count=count+1
        count1=0
        print("\r")
