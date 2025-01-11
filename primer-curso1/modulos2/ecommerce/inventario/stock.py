
#inventario
invetario = []

def agregar_producto(producto, cantidad):
    invetario.append({producto: cantidad})
    print(f"Se agregaron {cantidad} {producto} al inventario")
