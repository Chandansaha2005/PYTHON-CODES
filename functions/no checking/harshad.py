#harshad no
def harshad(n):
    s=0
    for i in str(n):
        s+=int(i)
    if n%s==0:
        return True
    else:
        return False
n=int(input("Enter hte no. = "))
if harshad(n):
    print("Harshad no.")
else:
    print("not Harshad no.")