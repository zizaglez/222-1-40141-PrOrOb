import classes.User;

public class Main {

    public static void main(String[] args) {

        System.out.println("Learning Object Oriented Programming with Java");
        User object_user = new User(0122110655, " Cesar G", "0122110655@alumnos.univa.com.mx");
        System.out.println("User id: " + object_user.id);
        System.out.println("Full name: " + object_user.full_name);
        System.out.println("Personal Email: " + object_user.personal_email);

        
    }
}