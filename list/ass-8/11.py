#WAP to define a list of countries that are a member of BRICS. Check whether a country member of BRICS or not
BRICS=['Brazil','Russia','India','China','South Africa']
n=input("Enter the country = ")
for i in BRICS:
    if i.lower()==n.lower():
        print(n + " is in BRICS")
        exit()
print(n + " is not in BRICS")