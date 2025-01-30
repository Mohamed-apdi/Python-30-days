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

# 8: Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(*list):
    
    for i in list:
        print(i)

print_list("jacar", 494, 30, "mahdi", 73, 43, "sadaq")

# 9: Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) -1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
            
print(reverse_list([1,2,3,4,5]))

# 10: Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list):
    capitalized = []
    for i in list:
        capitalized.append(i.capitalize())
    return capitalized
print(capitalize_list_items(["moha","mahdi", "sadaq"]))

# 11: Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(items, item):
    items.append(item)
    return items
items = [1, 2, 4, 5]

print(add_item(items, 4))