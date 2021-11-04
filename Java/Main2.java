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
