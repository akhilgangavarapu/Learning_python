print("Welcome to the Angry Goblin Hunt")
print("An award-winning game full of adventure and excitement (!)")

name = input("Type in your name: ")

print(name + ", do you think you can find the goblin hiding in the kitchen cupboards?")
print("|| || || || |_|")

found = False

while not found:
    choice = input("Which cupboard do you think the goblin is in [type in number]: ")
    if choice == "1":
        found = True
        print("Well done!! You have found the goblin. He was so scared he ran away.")
    else:
        print("Sorry! The goblin is still lurking somewhere else.")