#WAP to print the vowels of a string
x=input("Enter the string = ")
print("Vowels in",x," = ",end="")
for i in x:
    if i in 'AaEeIiOoUu':
        print(i,end = " ")