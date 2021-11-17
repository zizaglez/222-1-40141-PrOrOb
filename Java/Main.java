import Classes.Course;

public class Main {

    public static void main(String[] args) {
    
        //System.out.println("Learning Object Oriented Programming with Java");
        Course course_one = new Course(1000, "POO", 100, 1200, "Redes", "Roberto Gomez Bolaños", 120);

        course_one.welcome_course();
        course_one.ratings();
        course_one.goodbye_course();
        course_one.get_price_per_materia(course_one.price, course_one.descuento);
        course_one.new_teacher(course_one.professor, course_one.price);
        course_one.new_semester(course_one.name, course_one.professor);

    }
}