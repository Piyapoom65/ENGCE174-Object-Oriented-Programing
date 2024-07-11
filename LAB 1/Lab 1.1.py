# List comprehension
squares = [x**x for x in range(10)]
print(squares)

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)

# et comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)