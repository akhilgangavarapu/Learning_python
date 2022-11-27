import random

print("Welcome to the Angry Goblin Hunt")
print("An award-winning game full of adventure and excitement (!)")
gamer_name = input("type in your name")
print(f"{gamer_name}, do you think you can find the goblin hiding in the kitchen cupboards?")
print("|_| |_| |_| |_| |_|" )
goblin_cupboard = random.randint(1,5)
for i in range (5):
    cupboard_number = input("Which cupboard do you think the goblin is in [type in number]")
    cupboard_number = int(cupboard_number)
    if cupboard_number == goblin_cupboard :
        print("Well done!! You have found the goblin. He was so scared he ran away.")
        break
    else:
        print("Sorry! The goblin is still lurking somewhere else.")

