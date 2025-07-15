#head recursion 
def factorial(x):#x=-5
    if x == 1 or x==0:
        return 1
    #elif x<0:
      #  return -1
    else:
        return (x * factorial(x-1))#  5*4*3*2*1=120
num = int(input("Enter the Number = "))#num=5
if num>=0:
    print("The factorial of", num, "is", factorial(num))#calling
else:
    #x=factorial(num)#x=-1
    print("-ve no. fact. not possible")