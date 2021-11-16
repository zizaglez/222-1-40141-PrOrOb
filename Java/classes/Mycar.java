package Classes;

public class Mycar {
    public String color;
    public String model;
    public double old_car_value;
    public double discount;
    public double new_price;
    public String new_ride;

    public Mycar(String color, String model, double old_car_value, double discount, int new_price, String new_ride){
        this.color = color;
        this.model = model;
        this.old_car_value = old_car_value;
        this.discount = discount;
        this.new_price = new_price;
        this.new_ride = new_ride;
    }

    public void my_current_car(){
        System.out.println("My Golf");
    }
    public void mycar_4_sale(){
        System.out.println("Car for sale");
    }

    public void my_sold_car(){
        System.out.println("Sold!");
    }

    public void my_new_car(String new_ride, String model, String color){
        System.out.println ("My new vehicle will be: "+new_ride + model + color);
    }
    
    public void new_car_price(double new_price, double discount){
        double precio_total = this.new_price - this.discount;
        System.out.println("price with 5k discount " + precio_total);
    }
    
    public void new_car_with_discount(double new_price, double old_car_value){
        double precio_descuento = this.new_price - this.old_car_value;
        System.out.println("with no discount but old car value: " + precio_descuento);
    }

}


