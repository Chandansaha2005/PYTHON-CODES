#consonant copy from string to list
li=[]
x=input("Enter the String = ")
for i in x:
    if i not in 'AaEeIiOoUu':
        li.append(i)
print(li)