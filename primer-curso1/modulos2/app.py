from ecommerce.inventario.stock import agregar_producto
from ecommerce.sales.orders import ordes_to_inventario
from ecommerce.inventario.stock import invetario

def agegarOrden(orden, cantidad):
    ordes_to_inventario(orden, cantidad)
    agregar_producto(orden, cantidad)

agegarOrden("camisa", 10)
agegarOrden("pantalon", 5)

print(invetario)