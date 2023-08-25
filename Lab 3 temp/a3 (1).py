n=int(input("enter a num"))
def outer(x):
    def inner(y):
        return y*2
    result=inner(x)
    return result
output=outer(n)
print("result is",output)