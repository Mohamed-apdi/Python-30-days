import math

first_name = "Mohamed"
last_name = "Mohamed"

compare = first_name.__len__ == last_name.__len__
print("Compare: " , compare)

num_one = 5
num_two = 6

total = num_one + num_two
print("Total: ", total)

diff = num_one - num_two
print("Subtract: ", diff)

product = num_one * num_two
print("Product: ", product)

divition = num_one / num_two
print("Divition: ", divition)

remainder = num_two % num_one
print("Remainder: ", remainder)


exp = num_one ** num_two
print("Exponent: ", exp)

floor_division = num_one // num_two
print("floor_division: ", floor_division)

redius = 30
area_of_circle = math.pi * (redius ** 2)
print("Area of circle: ", area_of_circle)


circum_of_circle = 2 * math.pi * redius
print("Circumference: ", circum_of_circle)


input_radius = float(input("Enter a redius value: "))
print(input_radius)
input_value = input_radius
input_result = math.pi * (input_value ** 2)
print("Area of radius: ", input_result)