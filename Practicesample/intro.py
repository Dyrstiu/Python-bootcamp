# Author : @Dyrstiu
# Learning Resource : @Networkchuck (Youtube)

#EP1
print(""" Hello World !!! I am Iron Man""" )
print("what the hell!")
# string concatnation
print("No am tony.\n" +"No , I am poppy.")

print( "i am Poppy \n")

# EP2

print("Hello , welcome to Dyrstiu coffee")

name =input("What is your name: ")
print( "Hello " + name + " ,Thanks for comming in today" )
price = 8
menu = "Tea ","Coffee", "Muffins","Buns"
print("Here's today's menu : \n"  )
print (menu)
selection = input("What would you like to have ? ")
quantity = input("How many  "+ selection +" "  )
quatity2=int(quantity)

bill = quatity2 * price
print("Your " +selection + " will be ready in a minute 😊 \n " + "Your total bill is :$  " + str(bill) )



#EP3


name ="Dyrstiu"
age= 7
actual_age = 34.5
print(name , age)
print(type(actual_age))

print( 5 + 7)

math = 5 ** 7 + 6/9 * 6 - 4
print(math)
result = age + actual_age +math 
print(result)

