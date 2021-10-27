package classes;

public class Human{

        //Attributes / Properties. en java los atributos y los metodos hay que definir el tipo
        int born_year = 1987;

        public void say_hello(){ //Estos son mis metodos
            System.out.println(" Hello ");

        }

        public String Say_hello_user(String user_name){
            return "Hello " + user_name;

        }

        public int born_year(int year){
            return year;

        }
        
    }
