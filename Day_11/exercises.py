# Exercises: Level 1
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

# 12: Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(items, item):
    items.pop(item)
    return items
items = [1, 2, 4, 5]

print(remove_item(items, 2))

# 13: Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# formula n * (n + 1) / 2 
def sum_of_numbers(num):
    total = 0
    total += num * (num + 1) / 2
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))

# 14: Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# formula ((n + 1) // 2)²
def sum_of_odds(num):
    total = 0
    total += ((num + 1) // 2) ** 2
    return total

print(sum_of_odds(4))

# 15: Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# formula k = n // 2.  k * (k + 1)
def sum_of_even(num):
    k = num // 2
    total = 0
    total += k * (k + 1)
    return total
print(sum_of_even(6))


# Exercises: Level 2

# 1: Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    even = (n + 1) // 2
    odd = (n // 2) + 1 
    return even, odd

even, odd = evens_and_odds(100)
print(f"The number of odds are {odd}.")
print(f"The number of evens are {even}.")

# 2: Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# 
def factorial(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n * factorial(n - 1)
     
print(factorial(5))

# 3: Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(x):
    if x == 0 or x == None or isinstance(x, (str, list, tuple, dict, set)):
        return "empty"
    else:
        return "not"
print(is_empty({}))

# 4: Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

# sorted arr
def sorted_list(n):
    for i in range(len(n)):
        min_index = i
        for j in range(i + 1, len(n)):
            if n[j] < n[min_index]:
                min_index = j
        n[i], n[min_index] = n[min_index] , n[i] # swap
    return n

def calculate_mean(n):
    total = 0
    for i in n:
        total += i
    mean = total / len(n)
    print(mean)
calculate_mean([1, 2])

def calculate_median(n):
    s = sorted_list(n)
    length = len(n)
    
    # find median
    if length % 2 == 1: # odd
        return s[length // 2]
    else:
        mid1, mid2 = length // 2 - 1, length // 2
        return (s[mid1] + s[mid2]) / 2
    
    
    
print(calculate_median([4,1,2,5]))
    
