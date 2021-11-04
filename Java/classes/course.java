package classes;

public class Course{
    String nombre;
    String turno;
    String horario;
    String profesor;

    //This is the constructor in java
    public Course(String horario, String turno, String profesor, String nombre){
        this.nombre = nombre;
        this.turno = turno;
        this.horario = horario;
        this.profesor = profesor;


    }
    
}