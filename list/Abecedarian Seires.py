#WAP to genarate an Abecedarian Seires
series=[]
n='a'
while n<='z':
    word=input(f"Enter a word that starts with {n} : ")
    if word.lower().startswith(n):
        series.append(word)
        n=chr(ord(n)+1)
    else:
        print("The word must start with",n,"\nTry again...")    
print("Abecedarian Series = ",series)