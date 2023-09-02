import checkModule

string1=input("Enter the string: ")
string1=string1.strip()
a = checkModule.checkPalindrome(string1)
if(a == True):
    print("Yes it is a palindrome!")
else:
    print("No its not!")
