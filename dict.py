#Dictionary
#key-value pairs
#my_dictionary = {"key": "value"}

human = {"name": "Marat", "surname": "Yavrumyan", "age": 40, "is_married": True}
print(human)

#change a value
human["age"] = 30

#add a new value
human["have_pet"] = True

#delete a value
del human["surname"]

print(human)

#print as a list
print(human["name"], human["age"], human["is_married"])