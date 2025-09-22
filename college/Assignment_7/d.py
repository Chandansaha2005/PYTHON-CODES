leap = lambda y: (y%4==0 and y%100!=0) or (y%400==0)
leaps = list(filter(leap, range(2024, 3011)))

print("Leap years between 2024–3010:")
print(leaps)