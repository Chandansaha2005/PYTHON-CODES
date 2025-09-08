#WAP to illustrate the use of zip() function on variable-length sequences
li1=['apple','mango','orange','kola']#3
li2=[1,2,3,4,5]#5
li3=['a','b']#4
x=zip(li1,li2,li3)
for i in x:
    print(i)