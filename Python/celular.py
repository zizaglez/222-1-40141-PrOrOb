class Celular:

    color = "negro"#estos son mis atributos
    marca = "Iphone"
    modelo = 7

    def celular_color(self, color):#estos son metodos
        return("El color de mi celular es"+color)

    def celular_marca(self, marca):
        return("La marca de mi celular es "+marca )

    def celular_modelo(self, color, marca, modelo):
        print("Mi celular es un " +marca+ " color " +color+ " del modelo " +modelo)

mi_celular = Celular()
mi_celular.celular_modelo("negro","iphone","7")
mi_celular.celular_marca("iphone")
mi_celular.celular_color("negro")



celular_madre = Celular()
celular_madre.celular_modelo("Samsung","galaxy","s7")
