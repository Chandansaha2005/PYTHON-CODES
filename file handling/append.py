#WAP to open a previous file and write something into it
n=input("Enter the file name : ")
x=open("C:/Users/User/OneDrive/Desktop/Satyam/Python/file handling/"+n,"a")
x.write("\n",input("Enter the text : "))
x.close()
x=open("C:/Users/User/OneDrive/Desktop/Satyam/Python/file handling/"+n,"r")
for i in x.readlines():
    print(i)
x.close()