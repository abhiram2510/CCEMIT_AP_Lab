s=input("enter the string:")
def ul(input):
    uc=0
    lc=0
    for char in input:
        if char.isupper():
            uc+=1
        elif char.islower():
            lc+=1
    return uc,lc
uc,lc = ul(s)
print("NO.OF UPPER CASE:",uc)
print("NO.OF LOWER CASES",lc)
