import Classes.Mycar;

public class Main2 {

    public static void main(String[] args){

         //System.out.println("Learning Object Oriented Programming with Java");
         Mycar Mi_carro = new Mycar("Gris", " 2005 ", 40000, 5000, 150000, "Hilux");
         
         Mi_carro.my_current_car();
         Mi_carro.mycar_4_sale();
         Mi_carro.my_sold_car();
         Mi_carro.my_new_car(Mi_carro.new_ride, Mi_carro.model, Mi_carro.color);
         Mi_carro.new_car_price(Mi_carro.new_price, Mi_carro.discount);
         Mi_carro.new_car_with_discount(Mi_carro.new_price, Mi_carro.old_car_value);

    }
    
}
