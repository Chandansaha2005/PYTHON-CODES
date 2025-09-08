#tupple indexing
t=(1,2,3,4,5,6,7,8,'a','n','k','i','t','a','p','a','u','l')
for i in range(0,len(t),1):
    if t[i]=='a':
        print("Ath index = ",i)
print("Ath index = ",t.index('a')) #8       
print("Ath index = ",t.index('a',10))#13
print("Ith index = ",t.index('a',10,16))#13 loop 15