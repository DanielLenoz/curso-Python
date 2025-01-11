class Product:
    def __init__(self, product, price):
        self._product = product
        self._price = price
        self._inventario = [{"name": product, "price": price}]

    globalDescount = 15/100

    @property
    def product(self):
        count = len(self._inventario)
        total_price = sum(item["price"] for item in self._inventario)
        # si fuera en js
        # const totalPrice = this._inventario.reduce((sum, item) => sum + item.price, 0); // Suma de los precios
        print(f"el numero de productos son {count}, y los productos son {self._inventario}")
        print(f"el precio total de los productos es de {total_price}")
       
    
    @property
    def price(self):
        return print(f"el producto {self._product} tiene el valor {self._price}")

    @price.setter
    def price(self, new_price):
        if  new_price < 0:
           print("el precio no tiene que ser menor a cero")
        else:
            self._price = new_price
            self._inventario.append({"name":self._product, "price": new_price} )
            return print(f"el nuevo precio del producto {self._product} es de {new_price}")
    
    @staticmethod
    def priceMin (price):
        if price <= 50:
            print("el precio no es valido")
        else: 
            print("el precio si es valido")

    @classmethod
    def update_descount(cls, new_descount):
        cls.globalDescount = new_descount


Banana = Product("banana", 1000)
Banana.price
Banana.price = 15000
Banana.price = -1000 
Banana.price = 600
Banana.price
Banana.product

Product.priceMin(Banana._price)
Product.update_descount(50)
print(Product.globalDescount)