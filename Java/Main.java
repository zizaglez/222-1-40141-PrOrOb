import classes.course;

public class Main {

    public static String main(String[] args) {

        //System.out.println("Learning Object Oriented Programming with Java");
        course object_course = new course("La materia de POO", " es dada por el profesor Luis Guerra", "a las 7:00pm", " en el turno matutino");
        System.out.println("Turno: " + object_course.turno);
        System.out.println("Nombre: " + object_course.nombre);
        System.out.println("Profesor: " + object_course.profesor);
        System.out.println("Horario: " + object_course.horario);

        
    }
}