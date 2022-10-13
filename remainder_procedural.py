print("enter first input")
a = input()
if int(a) < 0:
    print("not valid")
    exit()
else:
    print("first value is " + a)
print("enter second input")
b = input()
if int(b) < 0:
    print("not valid ")
    exit()
else:
    print("second value is " + b)

sum = int(a) % int(b)

print(sum)