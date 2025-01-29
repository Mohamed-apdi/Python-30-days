# today 30/11/2024

# Creating a dictionary

empty_dict = {}

dct = {"key1":"value1", "key2":"value2", "key3":"value3"}


# example dictionary

person = {
    "firstname":"Mohamed",
    "lastname":"Abdifitah",
    "age":20,
    "country":"Somaliya",
    "state":"Banadir",
    "is_marred": False,
    "skills": ["Javascript", "Typescript", "Python", "React js", "Next js", "Node js", "Express js", "MongoDB", "Postgresql", "Linux"],
    "address": {
        "street":"KM4",
        "zipcode":'00252'
    }
}

print("Person: ", person)
print("Person length: ", len(person)) # length of person

print("Person name: ", person["firstname"] + " " + person["lastname"]) # name of person
print("Person name using get:", person.get("firstname"))

person["job_title"] = "Software Developer Engineer"
person["skills"].append("Software Developer")

print("person added new item: ", person)

dct = {"key1":"value1", "key2":"value2", "key3":"value3"}

dct.pop("key1") # remove key1
print(dct)

dct.popitem() # remove last item
print(dct)

del person["is_marred"]
print(person)