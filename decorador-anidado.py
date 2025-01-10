def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f'Access denied for {employee["name"]} from {employee["role"]}')
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f'registrando acción para {employee["name"]}')
        return func(employee)
    return wrapper


@check_access('Admin')
@log_action
def delete_employee(employee):
    print(f'Employee {employee["name"]} has been deleted')

admin = {'name': 'Juan', 'role': 'Admin'}
employee = {'name': 'Pedro', 'role': 'Employee'}

delete_employee(admin)
delete_employee(employee)
