# Author : @Dyrstiu
#Description : A program to check whether a yr is a leap yr or not.

year =int(input("Enter year to check: "))
def leap (year):
    if (year % 4) == 0 :
        print("This is a leap year")
        exit()
    elif (year % 400) == 0 :
        print("This is a leap year")
    else:
        print("This is not a leap year")
    
leap(year)
