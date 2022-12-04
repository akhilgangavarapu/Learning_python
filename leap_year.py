year1 = input("what is the year")
if int(year1) % 400 == 0:
    print("it is a leap year")
if int(year1) % 100 == 0 and int(year1) % 400 != 0:
    print("not a leap year")
if int(year1) % 4 == 0 and int(year1) % 400 != 0 and int(year1) % 100 != 0:
    print("it is a leap year")



