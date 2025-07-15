#tail recursion
def Recur_facto(n, a = 1):#n=0,a=1 
   
    if (n == 0): 
        return a 
   
    return Recur_facto(n - 1, n * a)#0,(5*1)(4*1)(3*1)(2*1)(1*1)*1
   
# print the result
num=int(input("Enter the No. = "))#num=5
if num>=0:
    print(Recur_facto(num))
else:
    print("-ve no. factorial can't be possible")