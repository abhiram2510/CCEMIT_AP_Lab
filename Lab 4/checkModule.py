def checkPalindrome(string1):
    string1=string1.lower()
    print("Original string:",string1)
    n=len(string1)
    string2=string1[::-1]
    print("Reversed String",string2)
    if(string1 == string2):
        return True
    else:
        return False
    
    
