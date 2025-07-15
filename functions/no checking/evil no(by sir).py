def to_binary(n):#n=12
        s = ""
        dig = ['0', '1']
        while n > 0:
            r = n % 2
            s = dig[r] + s
            n //= 2
        return s
def count_one(s):
        c = 0
        for ch in s:
            if ch == '1':
                c += 1
        return c
n = int(input("Enter a positive number: "))#n=12
bin_str = to_binary(n)#12
print("Binary Equivalent = ",bin_str)
ones_count = count_one(bin_str)
print("Number of Ones = ",ones_count)
if ones_count % 2 == 0:
    print(n," is an Evil Number.")
else:
    print(n," is Not an Evil Number.")