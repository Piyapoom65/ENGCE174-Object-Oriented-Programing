person = {'name': 'Alice', 'age': 30}

# Using get() method to handle missimg keys
city = person.get('city', 'Unknow')
print("City:", city) # Output: Unknown