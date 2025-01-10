
emplee = [{"nombre": "Juan", "edad": 22, "salario": 22.22}, 
          {"nombre": "Pedro", "edad": 33, "salario": 33.33}, 
          {"nombre": "Maria", "edad": 44, "salario": 44.44}, 
          {"nombre": "Jose", "edad": 55, "salario": 55.55}] 


def Better_salary2(emplee: list[dict["name": str, "age": int, "salario": float]]) -> list:
    return [x for x in emplee if x["salario"] > 50.00]

print(Better_salary2(emplee)) # [{'nombre': 'Maria', 'edad': 44, 'salario': 44.44}, {'nombre': 'Jose', 'edad': 55, 'salario': 55.55}]