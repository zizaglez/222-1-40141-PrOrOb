from _typeshed import Self


class Course:

    nombre = "POO"
    profesor = "Luis Guerra"
    horario = 7
    turno = "Impulso"
    salon: 5202
    alumnos: 7

    def __init__(self, clase, profesor, horario, turno, salon, alumnos):#(def __init__ es mi contructor)Un CONSTRUCTOR es Obligarte a inicializar los atributos de un objeto
        self.clase = clase
        self.profesor = profesor
        self.horario = horario
        self.turno = turno
        self.salon = 5202
        self.alumnos = 7        

object_course = Course("La materia de POO", " es dada por el profesor Luis Guerra", "a las 7:00pm", " en el turno matutino")
#print(object_user)
print(str(object_course.clase))
print(object_course.profesor)
print(object_course.horario)
print(object_course.turno)


