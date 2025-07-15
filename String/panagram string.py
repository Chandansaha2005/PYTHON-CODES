'''
panagram
'''
x="the quick brown fox jumps over the lazy dog"
y=input("Enter the String = ")
f=0
x=x.lower()
y=y.lower()
for i in y:
    if i not in x:
        f=1
        break
if f==0:
    print("Panagram String ")
else:
    print("NOT Panagram String ")