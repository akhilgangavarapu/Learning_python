##For Even Numbers
Num=(input("Enter a Number"))
print("You Entered <"+Num+">")
Num1=input("How many even numbers you wish to print?")

print("Printing "+Num1+" even numbers after "+Num)
count=0
for i in range(int(Num)+1,int(Num1*3)):
    if(i%2==0):
        print(i)
        count=count+1
    if(count>=int(Num1)):
        break;