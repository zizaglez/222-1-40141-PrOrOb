package Classes;


public class Course {
    
    public int id;
    public String name;
    public double score;
    public double price;
    public String materia;
    public String professor;
    public double descuento;

    public Course(int id, String name, double score, double price, String materia, String professor, double descuento){
        this.id = id;
        this.name = name;
        this.score = score;
        this.price = price;
        this.materia = materia;
        this.professor = professor;
    }

    public String welcome_course(){
        return "Welcome to POO";
    }

    public String ratings(){
        return "You final score is: ";
    }

    public void goodbye_course(){
        System.out.println("Thank you for taking POO");
    }

    public double get_price_per_materia(double price, double descuento){
        double result = this.price - descuento;
        return result;
    }

    public String new_teacher(String professor, double price){
        return "This is the new teacher " + professor + price;
    }
    public String new_semester(String profesor, String name){
        return "This is my new materia: " + name + profesor;

    }
}
