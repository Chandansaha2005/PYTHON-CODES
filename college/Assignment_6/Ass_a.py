#A
nums=[10,11,100,200,300,34]
print(sorted(set(nums))[-2],sorted(set(nums))[1])

# B.
# L=[1,5,2]
# nl=[0]*(max(L)+1)
# for x in L:nl[x]=x
# print(nl)
 
# C.
# s1="Here is Python";s2="We are learning Python"
# a=set(s1.split());b=set(s2.split())
# print(a&b);print(a|b);print(a-b)

# D.
# text="Python is inspired by Monty Python"
# f={}
# for w in text.split():f[w]=f.get(w,0)+1
# print(f)

# E.
# print(sorted(['ram','shyam','lakshami'],key=lambda x:x[-1]))
# print(sorted(['ram','sham','lakshami'],key=lambda x:x[-1]))