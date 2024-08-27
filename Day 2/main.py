first_name = "Mohamed"
last_name = "Mohamed"
age = 20
country = "Somalia"
city = "Mogadishu"
is_maried = False
skill = ["Next js", "React", "JavaScript", "TypeScript", "Python", "Node"]
person_info = {
    "first_name":"Mohamed",
    "last_name": "Mohamed",
    "Country": "Somalia",
    "City": "kismaayo",
    "Age": 20,
    "is_maried": False,
    "skills": ["Next js", "React", "JavaScript", "TypeScript", "Python", "Node"]
}

print(len(first_name))

fname, lname, coun, cit, age = "moh", "legend", "somalia", "kista", 20

compare = fname.__len__ == lname.__len__
print("Compare: ",compare)

print("First Name: " , fname)
print("LName: " , lname)
print("Country: " , coun)
print("City: " , cit)
print("Age: " , age)

# Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables

name = input("What is your name: ")
age2 = input("What is your age: ")
print(name)
print(age2)

# checking Data types and casting
print(type("hello"))                  # str
print(type(23))
print(type(2.14))
print(type([1, 2, 3, 4]))
print(type(1 + 4j))
print(type(True))
print(type({"name": "hello", "age": 44, "size": "sm"}))
print(type((1,2)))
print(type(zip([1,2],[3,4])))


# int to float conversion
num_nt = 10
print("num_int", num_nt)
numfloat = float(num_nt)
print("numfloat", numfloat)

# float to int conversion
gravity = 9.99
print(int(gravity))


# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']