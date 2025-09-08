#concatenate 2 tupple  & convert it into subtupple
t1=("Ankita","gache","jhule","thak","ankita")
t2=("ankita","lomba","hobi")
print("Tupple 1 = ",t1)
print("Tupple 2 = ",t2)
t3=t1+t2
print("Main Tupple after concatenate = ",t3)
t3=(t1,)+(t2,)
print("After Concatenate = ",t3)