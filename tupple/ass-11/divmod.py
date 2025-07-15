#WAP to write the use of divmod()
t=[(49,3),(253,5),(103,2),(129,11)]
for i in t:
    x=divmod(i[0],i[1])#x=(16,1),(50,3),(50,3)
    print("Quotient = ",x[0])
    print("Reminder = ",x[1])