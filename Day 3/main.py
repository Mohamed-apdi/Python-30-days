# Arithmetic Operations in Python
# Integers

print("Addition: ", 2 + 4)
print("Subtraction: ", 2 - 4)
print("Multiplication: ", 2 * 4)
print("Division: ", 4 / 2)
print("Modulus: ", 4 % 3)
print("Floor Division: ", 4 // 2)
print("Exponentiation: ", 4 ** 2)

# Floating Number
print("Floating Point Number, PI ", 3.14)
print("Floating Point Number, Gravity ", 9.81)

# Complex Number
print("Complex Number: ", 1 + 1j)
print("Multiplying Complex Number: ", (1 + 1j) * (1 - 1j))


a = 3
b = 4


total = a + b
diff = a - b
product = a * b
divition = a / b
remainder = a % b
floor_devistion = a // b
exponentiation = a ** b

print("a + b =", total)
print("a - b =", diff)
print("a / b =", divition)
print("a * b = ", product)
print('a % b = ', remainder)
print("a // b =", floor_devistion)
print("a ** b =", exponentiation)

# calculate area of circle

radius = 10

area_of_circle = 3.14 * radius ** 2

print("area_of_circle = ", area_of_circle)

# calculate area of rectangle
length = 10
width = 20
area_of_rectangle = length * width
print("area_of_rectangle = ", area_of_rectangle)

# calculate a weigth of an object
mass = 75
gravity = 9.81
weigth = mass * gravity
print("The weight of the object is =", weigth, "N")


# calculate the density of a liquid
mass = 200
volume = 50

density = mass / volume
print("The density of the liquid is =", density, "kg/m³")


# compare operators

print(2 > 4)
print(2 < 5)
print(2 == 3)
print(2 != 3)
print(2 >= 1)
print(2 <= 4)
print("-------------len and operators")
print(len("moha") == len("mahdi"))
print(len("mahdi") != len("mahdi"))
print(len("sadaq") >= len("xasuuni"))
print(len("shuceyb") <= len("xasuuni"))
print(len("sadaq") > len("mahdi"))
print(len("mahdi") < len("moha"))

# Comparing something gives either a True or False

print("True == True", True == True)
print("True == False", True == False)
print("False == False", False == False)

print("1 is 1", 1 is 1)
print("1 is not 2", 1 is not 2)
print("moha in the mohaas", "moha" in "the mohaas")
print("code in coder", "code" in "coder")
print("4 is 2 ** 2", 4 is 2 ** 2)
print("mahdi not in xasuuni", "mahdi" not in "xasuuni")

print(2 > 1 and 3 < 4)
print(2 < 2 and 5 > 3)
print(1 < 0 and 0 == 3)
print("True and True: ", True and True)
print(1 == 1 or 4 > 3)
print(6 > 3 or 9 < 1)
print(2 > 3 or 3 == 2)
print("True or False: ", True or False)
print(not 2 == 2)
print(not True)
print(not False)
print(not not True)
print(not not False)