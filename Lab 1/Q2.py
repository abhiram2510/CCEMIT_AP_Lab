n=int(input("Enter the number of rows:"))
count=1
for i in range(0,n):
    for j in range(0,i+1):
        print(count,end=" ")
        count=count+1
    print("\r")

    
