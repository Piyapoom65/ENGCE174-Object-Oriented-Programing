# Example 1: Working with dictionaties

# Creating a dictionary of student grades
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 88, 'David': 95}

# Accessing values using keys
print("Bob's grade:", grades['Bob'])

# Adding a new enty
grades['Eve'] = 90

# Iterating through keys and values
for student, grade in grades.items():
    print(f"{student}: {grade}")
    
# Using get () metho to avoid KeyError
print("Frank's grade:", grades.get('Frank', 'Grade not found')) # Output: Frank's grade: Grade