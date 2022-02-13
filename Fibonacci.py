from ast import Num
from tkinter import N
from tokenize import Number


print('===============================================================')

def fibonacci(number):
    a=0
    b=1

    if number == a or number == b :
        return True
    else:
        while b < number :
            c = a + b
            a = b
            b = c

        if b == number or a == number :
            return True
        else:
            return False 
number =int(input("Enter the number you wish to test:"))
if fibonacci(number):
    print(f"{number} is in the fibonacci sequence.")
else:
    print(f"{number} is not in the fibonnanci sequence.")