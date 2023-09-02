import math


def func1(a):
    b=a.real()
    rad= (math.pi/180)*b
    sina=math.sin(rad)
    sqrta= math.sqrt(b)
    loga=math.log(b)
    print("The sin value of the number is:",sina,", The square root of the number is:",sqrta,", The log of the number is:",loga)



a=complex(input("Enter the number:"))
func1(a)

    
