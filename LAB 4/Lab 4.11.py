# Example 4: Set opperations and methods

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Adding elements to a set
set1.add(5)

# Removing elements from a set
set2.add(6)

# Checking subset and supperset
print("Is set1 a subset of set2?", set1.issubset(set2)) # Output: Is set1 a subset of set2? False
print("Is set2 a  superset of set1?", set2.issuperset(set1)) # Output: Is set2 a superset of set1? True