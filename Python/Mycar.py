class My_car:

    def __init__(self, color, modelo, precio, descuento, new_price, new_car):
        self.color = color
        self.modelo = modelo
        self.precio = precio
        self.descuento = descuento
        self.new_price = new_price
        self.new_car = new_car
    
    def mycar(self):
        return "Car for sale"

    def my_sold_car(self):
        return "Sold!"

    def my_new_car(self, new_car):
        return "My new vehicle will be: "+new_car

    def new_car_price(self,new_price):
        precio_total = self.new_price - self.descuento
        return precio_total

    def price_with_discount(self, new_price):
        precio_descuento = self.new_price
        return precio_descuento

new_car = My_car("Red", "CL", 35000, 5000, 150000, "Hilux")#aqui estamos instanciando un objecto de la clase my_car el cual lleva un constructor
print(new_car.mycar())
print(new_car.my_sold_car())
print(new_car.my_new_car("Toyota"))
print("price with 5k discount ", new_car.new_car_price(145000))
print("with no discount: ", new_car.price_with_discount(150000))

