#Write a program to generate calendar of a month given the start_day and the number of days in that month using for loop
months={1:('January',31),2:('February',28,29),3:('March',31),4:('April',30),5:('May',31),6:('June',30),7:('July',31),8:('August',31),9:('September',30),10:('October',31),11:('November',30),12:('December',31)}
weeks={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
n=input("Enter the starting day : ")
m=input("Enter the name of month : ")
s,x=0,0
for k,v in weeks.items():
    if n.lower()==v.lower():
        s=int(k)
        break
print()
for k,v in months.items():
    if m.lower()==v[0].lower():
        x=int(v[1])
        break
print("CALENDER".center(50,"-"))
print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")
day=1
for i in range(s):
    print("\t",end="")
print(day,end="\t")
day+=1
s+=1
for i in range(day,x+1):
    if s==7:
        s=0
        print('\n')
    else:
        print(i,end="\t")
        s+=1
print()
print()