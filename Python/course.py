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


import Classes.Course;

public class Main2{

    public static void main(String[] args){

        //System.out.println("Learning Object Oriented Programming with Java");
        Course course_in_progress = new Course("POO ","Luis Guerra a las ", "7 pm ", " somos el grupo 204");
        Course my_next_course = new Course("Programación multimedia", "Sinai Bucio ", "8" ," grupo 256");

        System.out.println(course_in_progress.nombre_profesor(course_in_progress.materia, course_in_progress.profesor ,course_in_progress.grupo));
        System.out.println("Mi siguiente materia es "+ my_next_course.materia + " la imparte " + my_next_course.profesor +" los jueves a las " + my_next_course.grupo);

        Course.hola_amigos();
        course_in_progress.course_class();
    }
}


