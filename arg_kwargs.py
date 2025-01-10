def print_info(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")

#print_info(name="Carlos", age=30, city="bogota")
#print_info(name="Carlos", age=30, city="bogota", country="Colombia")

class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs
    
    def show_employee(self):
        print(f'Employee: {self.name}')
        print('Skills', self.skills)
        print('Details', self.details)

employee = Employee('Carlos', 'Python', 'Java', 'C++', age=30, city = 'Bogotá')
employee.show_employee()