empleados = [{"name": 'Juan', "age": 30, "salary": 80000}, {"name": 'Pedro', "age": 45, "salary": 120000}, {"name": 'Maria', "age": 60, "salary": 150000}]

better_employees = list(filter(lambda x: x['salary'] > 100000, empleados))
money = [x for x in empleados if x['salary'] > 140000]
print(better_employees)
print(money)