import math

def luckynumber(n):
    if(n<=55 and n>0):
        final=0
        for i in range(1,n+1):
            a=pow(2,i)
            final =final + a
        return final
    else:
        return 0
    
    
n= int(input())
a=luckynumber(n)
print(a)