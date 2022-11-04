# Indexing Operator []

# you are going to learn Indexing now

x=str(input("enter a string value"))
print(x)
print("you entered", x)
if len(x) % 2 ==0:
 #print ("your string is even")
 print("first charecter in", x ,"is...", x[0])
 print("last charecter in ",x, "is...",x[-1] )
 print("length of the string", x,"is",len(x))
 print("middle index is", len(x)/2)
 print("middle character in", x, "is", x[int(len(x) / 2)])
else:
 print("first charecter in", x, "is...", x[0])
 print("last charecter in", x, "is...", x[-1])
 print("length of the string", x, "is", len(x))
 print("middle index is", len(x)//2)
 print("middle character in", x, "is", x[int(len(x) //2)])