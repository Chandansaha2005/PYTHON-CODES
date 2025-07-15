#WAP to createa list of first 20 odd numbers using the shortcut method(list comprehension)
li=list(x for x in range(1,41) if x%2==1)
print(li)