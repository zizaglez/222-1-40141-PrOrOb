package Classes;

public class Course {
    
    public int id;
    public String name;
    public String description;
    public double price;
    public int class_room;
    public String professor;

    public Course(int id, String name, String description, double price, int class_room, String professor){
        this.id = id;
        this.name = name;
        this.description = description;
        this.price = price;
        this.class_room = class_room;
        this.professor = professor;
    }

    public String welcome_course(){
        return "Welcome to this course";
    }

    public void goodbye_course(){
        System.out.println("Good bye, please comeback soon");
    }

    public double get_price_per_user(int users, double discount){
        double result = this.price * users;
        result = result - discount;
        return result; 
    }

    public String new_teacher(String first_name, String last_name){
        String full_name = first_name + " " + last_name;
        return "This is the new teacher " + full_name;
    }
}
