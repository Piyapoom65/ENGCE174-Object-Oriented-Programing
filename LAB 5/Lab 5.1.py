class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary # เงินเดือนรายเดือน

    def annual_salary(self):
        return self.salary * 12 # คืนค่าเงินเดือนรายปีโดยคูณเงินเดือนรายเดือนด้วย 12

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def annual_salary(self):
        return (self.salary * 12) + self.bonus

class Developer(Employee):
    def __init__(self, name, salary, projects):
        super().__init__(name, salary)
        self.projects = projects

    def annual_salary(self):
        base_salary = self.salary * 12
        return base_salary + (self.projects * 1000) # รวมค่าตอบแทนจากโปรเจกต์ (โปรเจกต์ละ 1000)

manager = Manager("Alice", 6000, 5000) # เดือนรายเดือนเป็น 6000 และโบนัส 5000
developer = Developer("Bob", 5000, 3) # เงินเดือนรายเดือนเป็น 5000 และจำนวนโปรเจกต์ 3

total_annual_salary = manager.annual_salary() + developer.annual_salary()
print(total_annual_salary)

#ผลลัพธ์ที่ได้จะเป็นผลรวมของ

# เงินเดือนรายปีของ Alice: (6000 * 12) + 5000 = 77,000
# เงินเดือนรายปีของ Bob: (5000 * 12) + (3 * 1000) = 63,000

# รวมทั้งหมดเป็น 77,000 + 63,000 = 140,000