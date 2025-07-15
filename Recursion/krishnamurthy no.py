# Krishnamurthy 145-->5!=120 4!=24 1!=1 tail recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)  #1
def is_krishnamurthy(n,sum):# n=0   sum=145
    if n==0:
        return sum
    else:
        rem=n%10  #rem=1
        sum+=fact(rem)   #sum=145 #calling
        return is_krishnamurthy(n//10,sum)#145
num=int(input("Enter The Number = "))#num=145
if is_krishnamurthy(num,0)==num:
    print(f"{num} is krishnamurthy Number")
else:
    print(f"{num} is Not krishnamurthy Number")