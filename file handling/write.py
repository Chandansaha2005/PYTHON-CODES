#WAP to create a new file and write something into it
n=input("Enter the file name : ")
x=open("C:/Users/User/OneDrive/Desktop/Satyam/Python/file handling/"+n,"w")
x.write(input("Enter the text : "))
x.close()
x=open("C:/Users/User/OneDrive/Desktop/Satyam/Python/file handling/"+n,"r")
print(x.read())
x.close()