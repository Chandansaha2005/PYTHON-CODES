def recursive_factorial(n):#n=1
  if n == 1:
      return n
  else:
      return n * recursive_factorial(n-1)#120
num = int(input("Enter the No. = "))
if num < 0:
  print("Invalid input ! Please enter a positive number.")
elif num == 0:
  print("Factorial of number 0 is 1")
else:
  print("Factorial of number", num, "=", recursive_factorial(num))#num=5