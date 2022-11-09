A=int(input("Enter a number"))
print(" You entered  '",A,"'")
B=int(input("How many odd numbers you want to print"))
print("printing", B, "odd numbers after", A)

for i in range(A,B+1):
 if i % 2 != 0:
  print(i)