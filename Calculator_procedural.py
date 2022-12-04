print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")


choice = input("enter your choice")
if int(choice)== 1:
    num1 = input("enter a number:")
    num2 = input('enter second number:')
    result = int(num1 )+int(num2)
    print(result)
elif int(choice) == 2:
    num1 = input("enter a number:")
    num2 = input('enter second number:')
    result = int(num1) - int(num2)
    print(result)

elif int (choice) ==3:
    num1 = input("enter a number:")
    num2 = input('enter second number:')
    result = int(num1) * int(num2)
    print (result)

elif int (choice) ==4:
    num1 = input("enter a number:")
    num2 = input('enter second number:')
    result = int(num1) / int(num2)
    print(result)

else:
    print("result can be 1or2or3or4")
