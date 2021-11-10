class Course:
    def __init__(self, id, code, name, profesor, price, size):
        self.id = id
        self.code = code
        self.name = name
        self.profesor = profesor
        self.price = price
        self.size = size

    def welcome(self):
        return "Welcome student "

    def goodbye(self):
        return "Good day student "

    def new_profesor(self, new_profesor_name):
        return "This is your new profesor "+new_profesor_name

    def total_price(self, discount):
        total_price = self.size
        total_price = total_price - discount
        return total_price


####out of the class

new_course = Course(1, 1000, "POO", "Cesar g", 5, 10);#aqui estamos instanciando un objecto de la clase curso el cual lleva un constructor
print(new_course.welcome())
print(new_course.goodbye())
print(new_course.new_profesor("Omar"))
print("With 0 discount: ", new_course.total_price(0))
print("With 10 discount: ", new_course.total_price(10))
