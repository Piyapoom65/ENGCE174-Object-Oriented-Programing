def generate_patterns(n):
    # Type 1
    result1 = '\n'.join('*' * i for i in range(1, n + 1)) + '\n'

    # Type 2
    result2 = '\n'.join('*' * i for i in range(n, 0, -1)) + '\n'

    # Type 3
    result3 = '\n'.join(' ' * (n - i) + '*' * (2 * i - 1) for i in range(1, n + 1)) + '\n'

    # Type 4
    result4 = '\n'.join(' ' * (n - i) + '*' * (2 * i - 1) for i in range(n, 0, -1)) + '\n'

    # Type 5
    result5 = '\n'.join(' ' * (n - i) + '*' * i for i in range(1, n + 1)) + '\n'

    # แสดงผลลัพธ์
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

# รับค่า n จากผู้ใช้
n = int(input("Enter the number of rows: "))

# ตรวจสอบว่า n มีค่าที่มากกว่า 0
if n > 0:
    generate_patterns(n)
else:
    print("Enter a positive integer.")