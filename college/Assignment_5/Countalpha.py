str=input("Enter A Sentence = ")
c_upper=sum(1 for ch in str if ch.isupper())
c_lower=sum(1 for ch in str if ch.islower())
print("Upper = ",c_upper,"Lower = ",c_lower)