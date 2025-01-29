# loops


# white loop

count = 0

while count < 5 :
    print("count: ", count)
    count = count + 1
    
# break

count = 0

while count < 5 :
    print("count: ", count)
    count = count + 1
    if count == 3 :
        break
    
    
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
    
# for loop

num = [10, 20, 30, 40, 50]

for nums in num:
    print(nums)
    
name = "moha"

for i in range(len(name)):
    print(name[i])
    
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}


for key , value in person.items():
    print(key, value)
    
    
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
    
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
    
    numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')


for number in range(11):
    print(number)   # prints 0 to 10, not including 11
    

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
                
                            
                            