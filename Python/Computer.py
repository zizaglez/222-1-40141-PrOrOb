class Computer:

    def __init__(self, computer_name, sistema_operativo, color, numero_serie, id):
        self.id = id
        self.sistema_operativo = sistema_operativo
        self.color = color
        self.numero_serie = numero_serie
        self.computer_name = computer_name

    def personal_computer(self, computer_name, color):
        return "Computadora " + computer_name + "color " + color 

    def SO(self, sistema_operativo, numero_serie):
        return "SO: " + sistema_operativo + "Numero de serie: " + numero_serie
    
    def model_numer(self, id):
        return "ID de inventario: " + str(id)


current_computer = Computer("Xtreme PC ", "Windows 10 Pro. ", "negro ", "00331-10000-00001-AA510", 1)#aqui estamos instanciando un objecto de la clase my_car el cual lleva un constructor
print(current_computer.personal_computer(current_computer.computer_name, current_computer.color))
print(current_computer.SO(current_computer.sistema_operativo, current_computer. numero_serie))
print(current_computer.model_numer(current_computer.id))

class Gabinete:

    def __init__(self, nombre, modelo, numero_serie, color, ventiladores, id_pieza):
        self.nombre = nombre
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.color = color
        self.ventiladores = ventiladores
        self.id_pieza = id_pieza

    def marca_modelo_gabinete(self, nombre, modelo, color):
        return "Gabinete: " + nombre + "Modelo " + modelo + color

    def info_gabinete_NS_ID(self, numero_serie, ventiladores):
        return "Numero de serie: " + numero_serie + " No de ventiladores: " + str(ventiladores)
    
    def info_gabinete_ventiladores(self, id_pieza):
        return "ID de la computadora: " + str(id_pieza)

current_gabinete = Gabinete("Corsair 5000D. ", "CC-9011210-WW. ", "B08M49WW51.", "Multicolor", 3, 2)
print(current_gabinete.marca_modelo_gabinete(current_gabinete.nombre, current_gabinete.modelo, current_gabinete.color))
print(current_gabinete.info_gabinete_NS_ID(current_gabinete.numero_serie, current_gabinete.ventiladores))
print(current_gabinete.info_gabinete_ventiladores(current_gabinete.id_pieza))

class Motherboard(Gabinete):
    def __init__(self, nombre, marca, tecnologia_ram, cpu, marca_procesador, capacidad_ram, id_pieza):
        self.nombre = nombre
        self.marca = marca
        self.tecnologia_ram = tecnologia_ram
        self.cpu = cpu
        self.marca_procesador = marca_procesador
        self.capacidad_ram = capacidad_ram
        self.id_pieza = id_pieza

    def Mother_info(self, nombre, marca):
        return "Tarjeta madre: " + nombre + "Marca " + marca

    def Mother_specs(self, tecnologia_ram, cpu, marca_procesador, capacidad_ram):
        return "Tecnología de la memoria RAM: " + tecnologia_ram + "CPU: " + cpu + ", Marca del procesador " + marca_procesador + "Capacidad de almacenamiento de la memoria " + str(capacidad_ram)

    def Mother_inventario(self, id_pieza):
        return "ID de tarjeta madre: " + str(id_pieza)


current_motherboard = Motherboard("MAG X570. ", "MSI ", "DDR4. ", "8 procesadores.", "AMD, ", 128, 3)
print(current_motherboard.Mother_info(current_motherboard.nombre, current_motherboard.marca))
print(current_motherboard.Mother_specs(current_motherboard.tecnologia_ram, current_motherboard.cpu, current_motherboard.marca_procesador, current_motherboard.capacidad_ram))
print(current_motherboard.Mother_inventario(current_motherboard.id_pieza))

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
        return "Monitor: "+ marca + "Modelo: "+ modelo + color

    def monitor_specs(self, numero_serie, peso_producto, dimencoines_producto):
        return "Numero de serie: " + numero_serie + "Peso: " + (peso_producto) + " Dimensiones del monitor: "+dimencoines_producto

    def monitor_id(self, id_pieza):
        return "ID del monitor: " + str(id_pieza)

current_monitor = Monitor("Dell. ", "P2418HZM. ", "Negro/Plateado", "B0787GT54Y. ", "12.25 libras.", "21.65 x 7.09 x 19.71 pulgadas", 4)
print(current_monitor.monitor_general_info(current_monitor.marca, current_monitor.modelo, current_monitor.color))
print(current_monitor.monitor_specs(current_monitor.numero_serie, current_monitor.peso_producto, current_monitor.dimenciones_producto))
print(current_monitor.monitor_id(current_monitor.id_pieza))
