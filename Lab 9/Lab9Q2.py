class valueLessThanZeroError(Exception):
    pass

class aLessThanBError(Exception):
    pass

def add(a, b):
    c=a+b
    return c

def sub(a, b): 
    c=a-b
    return c

def multi(a, b):
    c=a*b
    return c

def divi(a, b):
    c=a/b
    return c    


flag = 0
while(flag != 1):
       print("1.Addition")
       print("2.Subtraction")
       print("3.Multiplication")
       print("4.Division")
       print("5.Quit Calculator")    
       c=0

       try:
           A = float(input("Enter the first value:"))
           B = float(input("Enter the second value:"))
           
       except ValueError:
           print("Not a valid input")
        
       ch = int(input("Enter the choice!:"))
       
       if ch==1:
           result = add(A,B)
           print("Result :",result)
       elif ch==2:
           try:
               if(A<B):
                   raise aLessThanBError
               else:
                   result = sub(A,B)
                   print("Result is :", result)
           except aLessThanBError:
               print("Value of A is less than Value of B, so this operation cannot be performed!")
        
       elif ch==3:
           result = multi(A,B)
           print("Result is :",result)
       elif ch==4:
           try:
               if B==0:
                   raise ZeroDivisionError
               elif (A<B):
                   raise aLessThanBError
               else:
                   result = divi(A,B)
                   print("Result is :",result)
           except ZeroDivisionError:
               print("Division By 0 is not possible")
           except aLessThanBError:
               print("A is Less than B")


       elif ch==5:
           print("Exiting Calculator!")
           flag = 1
