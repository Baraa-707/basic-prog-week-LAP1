print("Hello, World!")
# Exercise 01
print("Al-Aikari")
print("Baraa")
print("Rashad")

# Exercise 02

print("Lab Basic Programming,\n\tLab week 1\n\t\tIntroduction to \"Python\",\n\t\t\tWorking with variables\nLab Basic Programming,\n\tLab week 2")

# Exercise 03
surname = input("Enter your surname:")
first_name = input("Enter your first name: ")
age = input("Enter your age: ")
print(f"{age} {first_name} {surname}")
#Exercise 04
base = float(input("inter your base of traingle:"))
height = float(input ("inter your height of traingle:"))
area = base * height / 2
print(f"the area is:{area}")

# Exercise 05
days = int(input("enter your days:"))
hours = int(input("enter your hours:"))
minutes = int(input("enter your minutes:"))
seconds = int(input ("enter your seconds:"))
total = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
print(f"the total seconds are:{total}")

# Exercise 06
total= int(input("enter the number of seconds:"))
days = total // 86400
hours = total % 86400 //3600
minutes = total % 3600 //60 
seconds = total % 60
print(f"d:h:m:s-> {days} : {hours} : {minutes} : {seconds} ")



# Exercise 07
n = (input ("enter an integer number:"))
nn = n+n 
nnn= nn+n
total = int((n)+(nn)+(nnn))
print (total)

#Exercise 08
x = int(input("Enter a number :"))
y= int (input("Enter a number"))
results = (x+y)*(x+y)
print (results)

# Exercise 09
celsius = float(input("enter a temperature in Celsius: "))
Fahrenheit = round(celsius*9/5+32,1)
Kelvin = round(celsius+273.15,1)
print(f"Fahrenheit: {Fahrenheit}")
print(f"Kelvin: {Kelvin}")

# Exercise 10

a = 5
b = 10 
a,b = b,a
print(a)
print(b)
# Exercise 11
help(input)
help(int)
help(print)
# Homework 1

land = float(input("Price of the land?: "))
building = float(input("Price of the building?: "))
subtotal = land + building
vat = subtotal * 0.21
total = subtotal + vat
print(f"The total cost of the project is: {total}")

# Homework 2
t = 70.5
s = 20.89
v = 100.3
print("*** Welcome to the checkout system. ***")
trousers = int(input("How many trousers have been bought? "))
Tshirts = int(input("How many T-shirts have been bought? "))
vests = int(input("How many vests have been bought? "))
total = trousers * t + Tshirts * s + vests * v
print(f"Total amount to pay: {total}")

# Homework 3 
t = 70.5
s = 20.89
v = 100.3
print("*** Welcome to the checkout system. ***")
trousers = int(input("How many trousers have been bought? "))
Tshirts = int(input("How many T-shirts have been bought? "))
vests = int(input("How many vests have been bought? "))
total = trousers * t + Tshirts * s + vests * v
print(f"You have bought\n\tTrousers: {trousers} pair(s)\n\tT-shirts: {Tshirts} piece(s)\n\tVests: {vests} piece(s)")
print(f"Total: {total}")
