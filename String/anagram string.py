'''
 Anangram String
 1st string --> baba
 2nd string ---> abba
'''
x=input("Enter the 1st String = ")
y=input("Enter the 2nd String = ")
f=0
g=0
if len(x)==len(y):
    x=x.lower()
    y=y.lower()
    for i in x:
        if i not in y:
            f=1
            break
    for i in y:
        if i not in x:
            g=1
            break
    if f==0 and g==0:
        print("Anamgram String")
    else:
        print("NOT Anamgram String")      
else:
    print("NOT Anagram String")