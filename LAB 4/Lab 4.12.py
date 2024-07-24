# Example 5: Using sets for unique operations

# Finding unique elements from multiple lists
lists1 = [1, 2, 3, 4, 5]
lists2 = [3, 4, 5, 6, 7]
lists3 = [5, 6, 7, 8, 9]

unique_elements = set(lists1).union(set(lists2)).difference(set(lists3))
print("Unique elements:", unique_elements) # Output: Unique elements: {1, 2}