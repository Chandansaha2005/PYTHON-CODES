#WAP that has two sequences. First which stores some questions and second stores the corresponding answers. Use the zip() function to form a valid question answer series
qns,ans,n=[],[],int(input("Enter the no. of Questions : "))
for i in range(n):
    qns.append(input("Enter the Question : "))
    ans.append(input("Enter the Answer : "))
series = zip(qns,ans)
print()
print('QNA SERIES'.center(20,"-"))
print()
for i in series:
    for j in i:
        print(j)
    print()

