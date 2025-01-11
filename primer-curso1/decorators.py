def log_decorator(func):
    def wrapper():
        print(f'Calling function {func.__name__}')
        func()
        print(f'Finished calling function {func.__name__}')
    return wrapper



@log_decorator
def process_payment():
    print('Processing payment...')

process_payment()

#------------------------------------------------------------

def check_access(func):
    def wrapper(employee):
        if employee.get('rol') == 'Admin':
            return func(employee)
        else:
            print(f'Access denied for {employee['name']} from {employee['rol']}')
    return wrapper

@check_access
def delete_employee(employee):
    print(f'Employee {employee['name']} has been deleted')


admin = {'name': 'Juan', 'rol': 'Admin'}
employee = {'name': 'Pedro', 'rol': 'Employee'}

delete_employee(admin)
delete_employee(employee)