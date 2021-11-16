import Classes.Course;

public class Main {

    public static void main(String[] args) {
    
        //System.out.println("Learning Object Oriented Programming with Java");
        Course course_one = new Course(1000, "POO", "Programacion Orientada a Objetos", 499.99, 5202, "Luis Guerra");
        System.out.println(course_one.id);
        System.out.println(course_one.welcome_course());
        course_one.goodbye_course();
        System.out.println(course_one.get_price_per_user(5, 0));
        System.out.println(course_one.get_price_per_user(5, 2499.95));

    }
}