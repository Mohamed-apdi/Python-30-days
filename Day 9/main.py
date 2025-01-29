a = 4

if a > 5 :
    print("a is greater than 5")
else :
    print("a is less than or equal to 5")
    
print("a is greater") if a > 2 else print("a is less")


# Nested Conditions
a = -1

if a > 0 :
    if a % 2 == 0 :
        print("a is even")
    else : 
        print("a is odd")
elif a == 0 :
    print("a is zero")
else : 
    print("a is negative")
    
# If Condition and Logical Operators

a = -3

if a > 0 and a < 4 :
    print("a is positive btwn 0 and 4")
    
elif a == 0 and a < 0 :
    print("a is negative or zero")
    
else : 
    print("a is large enough")
    
age = int(input("Enter your age: "))

if age > 30 :
    print("Your old enough to learn driving")
    
elif age == 15 :
    print("You can learn to drive, but you need 3 year")
    
elif age > 18 :
    print("You can learn to drive")
    
else :
    print("You are not old enough to learn driving")