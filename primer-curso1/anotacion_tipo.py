def add_employee_ids(id:int, id2:int)->int:
    
    return id + id2

print(add_employee_ids(1, 2)) # 3

class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name:str, age:int, salary:float):
        self.name = name
        self.age = age
        self.salary = salary
    
    def introduce(self) -> str:
        return f'Hello, my name is {self.name}, I am {self.age} years old and I earn {self.salary} dollars'

juan = Employee('Juan', 30, 80000)
print(juan.introduce()) # Hello, my name is Juan, I am 30 years old and I earn 80000 dollars