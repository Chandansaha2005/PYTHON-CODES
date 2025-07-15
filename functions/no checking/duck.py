#duck no
def check(n):
    if n[0]=='0':
        return False
    for i in n:
        if i=='0':
            return True
    return False
n=input("Enter the no. = ")
if check(n):
    print("Duck no.")
else:
    print("not Duck No.")