#fetch specific element from the list by using slice()
li=["Shriza","is","a","good","studious","girl","I","must","say","that"]
x=slice(3)# 0:2
print(li[x])
for i in li[x]:
    print(i,end=' ')
print()
x=slice(2,6)
print(li[x])
x=slice(2,9,2)
print(li[x])