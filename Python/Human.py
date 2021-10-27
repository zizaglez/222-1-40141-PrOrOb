class Human:

    born_year = 1987

    def say_hello(self):
        print("Hello")

    def say_hello_user(self, user_name):
        print("Hello "+ user_name)



human_one = Human()
print(human_one)
print(human_one.born_year)
human_one.say_hello()#aqui estamos invocando
human_one.say_hello_user("Cesar")#aqui estamos invocando


#Abstracion: Cuando separamos los datos de un objeto para luego generar un molde o una clase.
#Encapsulamiento: Para hacer que ciertas metodos o propiedades sean inviolabes o inalterables
#Herencia: Permite crear clases apartir de otras. Si tuvieramos una clase "autos" y quisieramos crear una clase de "Auto deportivo" o "Auto clasico" podriamos
#propiedades y metodos de la clase " autos". Esto nos da una jerarquia de padre e hijo
# Se utiliza para crear "metodos" con el mismo nombre pero con diferente comportamiento