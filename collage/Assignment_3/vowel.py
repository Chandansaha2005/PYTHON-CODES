ch=input("Enter the Character = ")
if(len(ch)==1)and ch.isalpha():
    if(ch.lower() in "aeiou"):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid Input")