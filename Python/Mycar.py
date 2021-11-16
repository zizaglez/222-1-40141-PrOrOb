class My_car:

    def __init__(self, color, model, old_car_value, discount, new_price, new_ride):
        self.color = color
        self.model = model
        self.old_car_value = old_car_value
        self.discount = discount
        self.new_price = new_price
        self.new_ride = new_ride

    def my_current_car(self):
        return "My Golf"
    
    def mycar_4_sale(self):
        return "for sale"

    def my_sold_car(self):
        return "Sold!"

    def my_new_car(self, new_ride, model, color):
        return "My new vehicle will be a "+ new_ride + model + color

    def new_car_price(self, new_price, discount):
        precio_total = new_price - discount
        return precio_total

    def price_with_discount(self, new_price, old_car_value):
        precio_descuento = new_price - old_car_value
        return precio_descuento

new_car = My_car("Gris", " 2005 ", 40000, 5000, 150000, "Hilux")#aqui estamos instanciando un objecto de la clase my_car el cual lleva un constructor
print(new_car.my_current_car())
print(new_car.mycar_4_sale())
print(new_car.my_sold_car())
print(new_car.my_new_car(new_car.new_ride, new_car.model, new_car.color))
print("price with 5k discount ", new_car.new_car_price(new_car.new_price, new_car.discount))
print("with no discount but old car value: ", new_car.price_with_discount(new_car.new_price, new_car.old_car_value))
