n=int(input("enter no.of rows"))
for i in range(n):
    coeff=1
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(0,i+1):
        if j>0:
            coeff=coeff*(i-j+1)//j
        print(coeff,end=" ")
    print()