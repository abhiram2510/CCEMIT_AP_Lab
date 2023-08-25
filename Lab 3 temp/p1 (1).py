str=input("enter the numbers")
list=[float(i) for i in str.split()]

def mul(lt):
    result=1
    for n in lt:
        if isinstance(n,(int,float)):
            result*=n
    return result
answer=mul(list)
print("answer is",answer)