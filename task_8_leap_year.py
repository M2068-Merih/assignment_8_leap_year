number=int(input("put your number to learn if its leap year: "))
if number%4==0:
    if number%100==0 and number%400!=0:
        print(number, "is not a leap year")
    else:
        print(number, "is a leap year")
else: print(number, "is not a leap year")
