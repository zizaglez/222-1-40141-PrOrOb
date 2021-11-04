package Classes;

public class Course{
    public String materia;
    public String grupo;
    public String profesor;
    public String siguiente_materia;

    //This is the constructor in java
    public Course(String materia, String profesor, String grupo, String siguiente_materia){
        super();
        this.materia = materia;
        this.grupo = grupo;
        this.profesor = profesor;
        this.siguiente_materia = siguiente_materia;
    }

    public String nombre_profesor(String materia, String profesor, String grupo){
        return materia + "la imparte " + profesor + grupo;
    }

    public String siguiente_asignacion(String materia, String siguiente_materia){
        return siguiente_materia + materia;
    }

    public static void hola_amigos() {
        System.out.println("Hola profesor y compañeros");
    }

    public void course_class(){
        System.out.println("En mi clase de POO somos 7 en el grupo y en la materia que viene Dios dira");
    }
}