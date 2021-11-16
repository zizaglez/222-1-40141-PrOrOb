import Classes.Mycar;

public class Main2 {

    public static void Mycar(String[] args){

         //System.out.println("Learning Object Oriented Programming with Java");
         Mycar Mi_carro = new Mycar("Red", "CL", 35000, 5000, 150000, "Hilux");
         System.out.println(Mi_carro.modelo);
         System.out.println(Mi_carro.color);
         System.out.println(Mi_carro.my_current_car());
         System.out.println(Mi_carro.my_sold_car());
         Mi_carro.my_new_car("Toyota");
         System.out.println(Mi_carro.new_car_price(15000));
         System.out.println(Mi_carro.new_car_with_discount(14500));

    }
    
}
