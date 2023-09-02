import math


def func1(a):
    rad= (math.pi/180)*a
    sina=math.sin(rad)
    sqrta= math.sqrt(a)
    loga=math.log(a)
    print("The sin value of the number is:",sina,", The square root of the number is:",sqrta,", The log of the number is:",loga)



a=int(input("Enter the number:"))
func1(a)

    
