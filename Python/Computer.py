class Computer:

    def __init__(self, teclado):
        self.teclado = teclado
        #id, computer_name, sistema_operativo, color, numero_serie, ram, tarjeta_video, monitor, mouse
        #self.id = id
        #self.sistema_operativo = sistema_operativo
        #self.color = color
        #self.numero_serie = numero_serie
        #self.computer_name = computer_name
        #self.ram = ram
        #self.tarjeta_video = tarjeta_video
        #self.monitor = monitor
        #self.mouse = mouse

    def id_number(self, id):
        return "ID Computadora: " + str(id)

    def personal_computer(self, computer_name, color):
        return "Computadora " + computer_name + "color " + color 

    def SO(self, sistema_operativo, numero_serie):
        return "SO: " + sistema_operativo + "Numero de serie: " + numero_serie

    def specs_internos(self, ram, tarjeta_video):
        return "Memoria RAM: "+ ram + "Tarjeta de video: " + tarjeta_video

    def perifericos(self, monitor, teclado, mouse):
        return "Monitor: " + monitor + "Teclado: " + teclado + "Mouse: " + mouse
    

    def metodo(self):
        return ("Procesa -> informacion\n")


current_computer = Computer("Logitech\n")#aqui estamos instanciando un objecto de la clase my_car el cual lleva un constructor
#, 1, "Xtreme PC ", "Windows 10 Pro\n", "negro ", "00331-10000-00001-AA510", "16\n", "AMD Radeon R7 Graphics", "Dell\n", "Tecknet Inalambrico"
print(current_computer.id_number(1))
print(current_computer.personal_computer("Xtreme PC ", "negro "))
print(current_computer.SO("Windows 10 Pro\n", "00331-10000-00001-AA510"))
print(current_computer.specs_internos("16\n", "AMD Radeon R7 Graphics"))
print(current_computer.perifericos("Dell\n", current_computer.teclado,  "Tecknet Inalambrico"))
print(current_computer.metodo())



class Gabinete:

    def __init__(self, id_pieza, nombre, modelo, numero_serie, color, ventiladores):
        self.nombre = nombre
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.color = color
        self.ventiladores = ventiladores
        self.id_pieza = id_pieza

    def gabinete_id(self, id_pieza):
        return "ID Gabinete: " + str(id_pieza)

    def marca_modelo_gabinete(self, nombre, modelo, color):
        return "Gabinete: " + nombre + "Modelo: " + modelo + "Color: " +color

    def NS_ventiladores(self, numero_serie, ventiladores):
        return "Numero de serie: " + numero_serie + "No de ventiladores: " + str(ventiladores)

    def metodo(self):
        return "Gabinte -> Arma\n"
    


current_gabinete = Gabinete(2, "Corsair 5000D\n", "CC-9011210-WW\n", "B08M49WW51\n", "Multicolor", 3)
print(current_gabinete.gabinete_id(current_gabinete.id_pieza))
print(current_gabinete.marca_modelo_gabinete(current_gabinete.nombre, current_gabinete.modelo, current_gabinete.color))
print(current_gabinete.NS_ventiladores(current_gabinete.numero_serie, current_gabinete.ventiladores))
print(current_gabinete.metodo())



class Motherboard(Gabinete):
    def __init__(self, id_pieza, nombre, marca, tecnologia_ram, cpu, marca_procesador, capacidad_ram):
        self.nombre = nombre
        self.marca = marca
        self.tecnologia_ram = tecnologia_ram
        self.cpu = cpu
        self.marca_procesador = marca_procesador
        self.capacidad_ram = capacidad_ram
        self.id_pieza = id_pieza


    def Mother_inventario(self, id_pieza):
        return "ID Tarjeta madre: " + str(id_pieza)

    def Mother_info(self, nombre, marca):
        return "Tarjeta madre: " + nombre + "Marca: " + marca

    def Mother_specs(self, tecnologia_ram, cpu, marca_procesador, capacidad_ram):
        return "Tecnología de la memoria RAM: " + tecnologia_ram + "CPU: " + cpu + "Marca del procesador " + marca_procesador + "Capacidad de almacenamiento de la memoria " + str(capacidad_ram)


current_motherboard = Motherboard(3, "MAG X570\n", "MSI ", "DDR4\n", "8 procesadores\n", "AMD\n", "128\n")
print(current_motherboard.Mother_inventario(current_motherboard.id_pieza))
print(current_motherboard.Mother_info(current_motherboard.nombre, current_motherboard.marca))
print(current_motherboard.Mother_specs(current_motherboard.tecnologia_ram, current_motherboard.cpu, current_motherboard.marca_procesador, current_motherboard.capacidad_ram))




class Monitor:

    def __init__(self, marca, modelo, color, numero_serie, peso_producto, dimenciones_producto, id_pieza):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.numero_serie = numero_serie
        self.peso_producto =  peso_producto
        self.dimenciones_producto = dimenciones_producto
        self.id_pieza = id_pieza

    def monitor_general_info(self, marca, modelo, color):
        return "Monitor: "+ marca + "Modelo: "+ modelo + "Color: "+color

    def monitor_specs(self, numero_serie, peso_producto, dimencoines_producto):
        return "Numero de serie: " + numero_serie + "Peso: " + (peso_producto) + "Dimensiones del monitor: "+dimencoines_producto

    def monitor_id(self, id_pieza):
        return "ID monitor: " + str(id_pieza)

current_monitor = Monitor("Dell\n", "P2418HZM\n", "Plateado", "B0787GT54Y\n", "12.25 libras\n", "21.65 x 7.09 x 19.71 pulgadas\n", 4)
print(current_monitor.monitor_general_info(current_monitor.marca, current_monitor.modelo, current_monitor.color))
print(current_monitor.monitor_specs(current_monitor.numero_serie, current_monitor.peso_producto, current_monitor.dimenciones_producto))
print(current_monitor.monitor_id(current_monitor.id_pieza))


class Teclado(Computer):

    def __init__(self, teclado, id, color, modelo, tipo):
        super().__init__(teclado)
        self.id = id
        self.color = color
        self.modelo = modelo
        self.tipo = tipo

    def keyboard(self, id):
        return "ID Teclado: "+ str(id)

    def keyboard_specs(self, modelo, tipo):
        return "Modelo: "+modelo + "Tipo: "+tipo

    def keyboard_general_info(self, color):
        return "Teclado: "+current_keyboard.teclado + "Color: "+ color 

    def metodo(self):
        return "Teclado -> Escribe"

current_keyboard = Teclado ("Logitech\n", 5, "Negro\n", "K120\n", "Alambrico")
print(current_keyboard.keyboard(current_keyboard.id))
print(current_keyboard.keyboard_specs(current_keyboard.modelo, current_keyboard.tipo))
print(current_keyboard.keyboard_general_info(current_keyboard.color))
print(current_keyboard.metodo())