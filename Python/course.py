class Course:
    materia = "POO"
    cuatrimestre = 4
    def __init__(self, materia, turno, cuatrimestre, profesor):
        self.materia = materia
        self.turno = turno
        self.cuatrimestre = cuatrimestre
        self.profesor = profesor
      
mi_primer_curso = Course("POO", "turno impulso", 4, "Luis Guerra")
mi_segundo_curso = Course("programacion multimedia", "modelo impulso", 4, "Sinai Bucio")

def cursos_univa(mi_primer_curso, mi_segundo_curso):
    print("Mis cursos son: " + mi_primer_curso.materia + " y " + mi_segundo_curso.materia)

def maestros_univa(mi_primer_curso, mi_segundo_curso):
    print("Mis cursos son: " + mi_primer_curso.profesor + " y " + mi_segundo_curso.profesor)

cursos_univa(mi_primer_curso,mi_segundo_curso)
maestros_univa(mi_primer_curso,mi_segundo_curso)

def materia():
    print("Mi materia actual: " + Course.materia)

def cuatrimestre():
    print("Mis dos materias son de " + str(Course.cuatrimestre) + "to cuatrimestre.")

materia()
cuatrimestre()


