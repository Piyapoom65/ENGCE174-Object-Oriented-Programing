def generate_pattern_type1(n, i=1):
    if i > n:
        return ''
    return '*' * i + '\n' + generate_pattern_type1(n, i + 1)

def generate_pattern_type2(n, i):
    if i == 0:
        return ''
    return '*' * i + '\n' + generate_pattern_type2(n, i - 1)

def generate_pattern_type3(n, i=1):
    if i > n:
        return ''
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    return spaces + stars + '\n' + generate_pattern_type3(n, i + 1)

def generate_pattern_type4(n, i):
    if i == 0:
        return ''
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    return spaces + stars + '\n' + generate_pattern_type4(n, i - 1)

def generate_pattern_type5(n, i=1):
    if i > n:
        return ''
    spaces = ' ' * (n - i)
    stars = '*' * i
    return spaces + stars + '\n' + generate_pattern_type5(n, i + 1)

def generate_patterns(n):
    result1 = generate_pattern_type1(n)
    result2 = generate_pattern_type2(n, n)
    result3 = generate_pattern_type3(n)
    result4 = generate_pattern_type4(n, n)
    result5 = generate_pattern_type5(n)
    
    print("Type 1:\n")
    print(result1)
    print("\n--------------------------------")
    
    print("Type 2:\n")
    print(result2)
    print("\n--------------------------------")
    
    print("Type 3:\n")
    print(result3)
    print("\n--------------------------------")
    
    print("Type 4:\n")
    print(result4)
    print("\n--------------------------------")
    
    print("Type 5:\n")
    print(result5)
    print("\n--------------------------------")

# Taking input n from the user
n = int(input("Enter the number of rows: "))

# Checking if n is a positive integer
if n > 0:
    generate_patterns(n)
else:
    print("Enter a positive integer for the number of rows.")