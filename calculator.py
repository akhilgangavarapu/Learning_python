# Program make a simple calculator

# 1 This function adds two numbers
def add(x, y):
    return x + y



# 2 This function subtracts two numbers
def subtract(x, y):
    return x - y


# 3This function multiplies two numbers
def multiply(x, y):
    return x * y


# 4 This function divides two numbers
def divide(x, y):
    return x / y

# 5 This is Remainder
def remainder(x, y):
    return x % y


# 6 This is Quotient(//)
def quotient(x, y):
    return x // y

# 7 this is square
def square(x,y):
    return (x ** y)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Remainder")
print("6.Quotient")
print("7.Square of a number")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5','6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", remainder(num1, num2))

        elif choice == '6':
            print(num1, "//", num2, "=", remainder(num1, num2))

        elif choice == '7':
            print(num1, "**", num2, "=", remainder(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else: print("Invalid Input")