#distance of a line
import math
p=input("Enter the 1st Co-ordinate = ")
p=p.split(",")
print(p)
q=input("Enter the 2nd Co-ordinate = ")
q=q.split(",")
print(q)
d=math.sqrt((int(q[0])-int(p[0]))**2 +(int(q[1])-int(p[1]))**2)
print(d)