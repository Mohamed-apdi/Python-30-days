# 1: Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def sum_two_num(num1, num2):
    return num1 + num2
print(sum_two_num(5,8))

# 2: Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14
    res =  pi + r ** 2
    return res
print("area of circle: ", area_of_circle(5))

# 3: Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print("added all nums: ",add_all_nums(76,4,23,6,22))

# 4: Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def temperature(c):
    f = (c * 9 / 5) + 32
    return f
print("Temperature °C converted °F: ", temperature(5))

# 5: Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# Months of the Year. January | February | March | April | May | June | July | August | September | October | November | December.
def check_season(month):
    if(month == "January" or month == "February" or month == "March"):
        print("Autumn")
    elif(month == "April"or month == "May" or month == "June"  ):
        print("Winter")
    elif(month == "July" or month == "August" or month == "September"):
        print("Spring")
    else:
        print("Summer")
print(check_season("December"))

# 6: Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m
print("The slope of a linear equation: ", calculate_slope(30, 90, 45, 15))

# 7: Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def calculate_of_quadratic(a,b,c,x):
    eq_sol = (a * x) ** 2 + b * x + c
    return eq_sol
print(calculate_of_quadratic(4, 2, 5, 3))