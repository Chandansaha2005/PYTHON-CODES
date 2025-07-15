#WAP to check single key in a dictionary.
x={1:10,2:20,3:30,4:40,5:50,6:60,7:22}
n=int(input("Enter the key to check :"))
if n in x.keys():    
    print(n,"key is present")
else:
    print(n,"key is not present")