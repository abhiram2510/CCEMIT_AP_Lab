list1=[]

def multiplylist(list1):
    val=1
    for element in list1:
        val=val*element

    return val





no_of_elements = int(input("Enter the number of elements in the list:"))
for i in range(0,no_of_elements):
    element = int(input("Enter the elements:"))
    list1.append(element)


finalanswer = multiplylist(list1)
print("The given list is ", list1)
print("The final value after multiplication is:",finalanswer)
    
