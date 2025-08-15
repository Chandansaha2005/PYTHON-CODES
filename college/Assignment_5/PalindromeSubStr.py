line= input("Enter A String = ")
srt,end= map(int , input("Enter the Starting and ending of Substring = ").split())
sub=line[srt:end+1]
print("Substring = ",sub)
if sub.lower()== sub[::-1].lower():
    print("Palindrome Substring")
else :
    print("Not Palindrome")