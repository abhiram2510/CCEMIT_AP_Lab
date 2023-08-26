n=input("Enter a string:")
for char in n:
    if(char>='0' and char<='9') or (char>='A' and char<='F'):
        continue
    else:
        print("not hexadecimal number")
        break
else:
    print("hexadecimal number")
