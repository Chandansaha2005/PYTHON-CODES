print("Leap year" if(yr:=int(input("Enter the year = ")))%4==0 and (yr%100!=0 or yr%400==0) else "Not Leap Year")


