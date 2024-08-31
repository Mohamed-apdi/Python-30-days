# # 1
# age = 20
# # 2
# height = 1.77
# # 3
# complext_number = 1 - 1j
# # 4
# base = float(input('Enter a base of trangle: '))
# height = float(input("Enter a height of trangle: "))

# area = 0.5 * base * height
# print("The area of trangle is: ", area)

# # 5
# a = float(input("Enter side a of the trangle: "))
# b = float(input("Enter side b of the trangle: "))
# c = float(input("Enter side c of the trangle: "))

# perimiter = a + b + c
# print(perimiter)
# # 6
# height = float(input("Enter height of the regtangle: "))
# weight = float(input("Enter weight of the regtangle: "))

# area = height * weight
# perimiter_regtangle = 2 * (height + weight)
# print("Area of the regtangle is: ", area)
# print("Perimiter regtangle is: ", perimiter_regtangle)

# # 7
# radius = float(input("Enter the radius: "))

# area_of_circle = 3.14 * radius ** 2
# circumference = 2 * 3.14 * radius

# print("area_of_circle is: ", area_of_circle)
# print("Circumference is: ", circumference)


# # 8

# # Given equetion parameters

# m = 2 # slope
# b = -2 # y-intercept


# # calculate the slope
# slope = m
# # calculate the y-intercept
# y_intercept = b

# # calculate the x-intercept by setting y = 0 and solving for x

# x_intercept = -b / m

# print(f"Slope (m): {slope}")
# print(f"y-intercept: {0, y_intercept}")
# print(f"x-intercept: {x_intercept, 0}")

# # 9
# # fine the slope you have p1 and p2

# p1 = (1, 1)
# p2 = (6, 10)

# x1, y1 = p1
# x2, y2 = p2

# m = (y2 - y1) / (x2 - x1)

# print("The slope is: ", m)

# # 10

# # Calculate the value of y (y = x^2 + 6x + 9). 

# x = 4

# y = x ** 2 + 6*x + 9

# print("The value of y is: ", y)

# str1 = "python"
# str2 = "dragon"

# compare_strs = len(str1) == len(str2)

# print("The comare_strs is: ", compare_strs)

# # 14

# statement = "i hope this course is not full of jargon"

# print("check jargon in statement", "jargon" in statement)

# # 15
# word1 = "python"
# word2 = "jordan"

# print("check on both statements", word1 in "on", word2 in "on")

# # 16

# word = "python"
# len_word = len(word)

# convert_to_float = float(len_word)

 
# print("convert_to_string", str(convert_to_float))

# # 17

num = 4
event = num % 2 == 0 

if (event) :
    print("The number is even")
else :
    print("The number is odd")
    
# 18
    
floor_division = 7 // 3

int_conversion = int(2.7)

# Check if they are equal
is_equal = floor_division == int_conversion

print(is_equal)

# 19

v1 = '10'
v2 = 10

check_equal = v1 == v2

print(check_equal)


v_1 = int('10')

v_2 = 10

check = v_1 == v_2

print(check) 


# 20

num_1 = float(input("Enter hours: "))
num_2 = float(input("Enter rate per hour: "))

res = num_1 * num_2

print(res)


# 21

num_year = int(input("Enter year: "))

calculate_person_live_rate = num_year * 360 * 24 * 60 * 60

print(f"you have lived for {calculate_person_live_rate} seconds.")

# Loop to generate each row
for a in range(1, 6):
    b = 1
    ab = a ** b
    ab2 = a ** (b + 1)
    ab3 = a ** ( b + 2)
    print(f"{a} {b} {ab} {ab2} {ab3}")
    
