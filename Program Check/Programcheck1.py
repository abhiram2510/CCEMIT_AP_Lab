def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print("Factorial of ",i," is ",fact)
    return fact


myDict={"Odd":0,"Even":0}
a=int(input("Enter the limit: "))
answer = fact(a)
if(answer%2 == 0):
    myDict["Even"]=answer
else:
    myDict["Odd"]=answer

for item in myDict.items():
    print(item)


    
