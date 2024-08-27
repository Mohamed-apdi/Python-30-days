# 1
age = 20
# 2
height = 1.77
# 3
complext_number = 1 - 1j
# 4
base = float(input('Enter a base of trangle: '))
height = float(input("Enter a height of trangle: "))

area = 0.5 * base * height
print("The area of trangle is: ", area)

# 5
a = float(input("Enter side a of the trangle: "))
b = float(input("Enter side b of the trangle: "))
c = float(input("Enter side c of the trangle: "))

perimiter = a + b + c
print(perimiter)
# 6
height = float(input("Enter height of the regtangle: "))
weight = float(input("Enter weight of the regtangle: "))

area = height * weight
perimiter_regtangle = 2 * (height + weight)
print("Area of the regtangle is: ", area)
print("Perimiter regtangle is: ", perimiter_regtangle)

# 7
radius = float(input("Enter the radius: "))

area_of_circle = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius

print("area_of_circle is: ", area_of_circle)
print("Circumference is: ", circumference)


# 8

# Given equetion parameters

m = 2 # slope
b = -2 # y-intercept


# calculate the slope
slope = m
# calculate the y-intercept
y_intercept = b

# calculate the x-intercept by setting y = 0 and solving for x

x_intercept = -b / m

print(f"Slope (m): {slope}")
print(f"y-intercept: {0, y_intercept}")
print(f"x-intercept: {x_intercept, 0}")

# 9
# fine the slope you have p1 and p2

p1 = (1, 1)
p2 = (6, 10)

x1, y1 = p1
x2, y2 = p2

m = (y2 - y1) / (x2 - x1)

print("The slope is: ", m)

# 10

# Calculate the value of y (y = x^2 + 6x + 9). 

x = -5

y = x ** 2 + 6*x + 9

print("The value of y is: ", y)

