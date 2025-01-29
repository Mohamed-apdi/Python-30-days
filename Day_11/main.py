# functions 

def generate_name():
    first = "moha"
    last = "mnx"
    full =  first + " " + last
    print(full)

generate_name()

def add_numbers():
    num1 = 5
    num2 = 9 
    sum = num1 + num2
    print(sum)
    
add_numbers()


def greetings(name):
    message = name + ", welcome to the world of python"
    return message

print(greetings("moha"))

def sum(num) :
    res = num + 99
    return res

print(sum(1))

def multiply(num1, num2):
    res = num1 * num2
    return res
print(multiply(5, 5))

def square(x):
    res = x * x
    return res
print(square(4))

def are_of_circle(r):
    pi = 3.14
    res = pi + r ** 2
    return res
print(are_of_circle(5))

def sum_of_num(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
print(sum_of_num(100))

def calculate_age(current_year, year_birth):
    res = current_year - year_birth
    return res
print("Your age is: ", calculate_age(2025, 2004))


def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + ' N'
    return weight

print("The Weight of an object Newton: ", weight_of_object(100, 9.81))

def weight_of_obj(mass, gravity = 9.81):
    area = str(mass * gravity) + ' N'
    return area

print(weight_of_obj(70))
    
def age_of_birth(yearBirth, currentYear = 2025):
    age = currentYear - yearBirth
    return age

print(age_of_birth(2004))


def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(44, 55, 66, 88, 99))

def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)

print(generate_groups("Team1", "moha","mahdi","sadaq"))

def square_num(n):
    return n * n
def do_something(f, x):
    return f(x)

print(do_something(square_num, 4))