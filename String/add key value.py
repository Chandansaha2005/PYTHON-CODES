#WAP to encrypt a string by adding a key value to every character
s=input("Enter the string : ")
k=int(input("Enter the key value : "))
es=''
for i in s:
    if i.isalpha():  
        if i=='z'or i=='Z': 
            es+=chr(ord(i)+k-26)
        else:
            es+=chr(ord(i)+k)
    else:
        es+=i
print(es)