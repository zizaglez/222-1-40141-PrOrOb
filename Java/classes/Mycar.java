package Classes;

public class Mycar {
    public String color;
    public String modelo;
    public double precio;
    public double descuento;
    public double new_price;
    public String new_car;

    public Mycar(String color, String modelo, double precio, double descuento, int new_price, String new_car){
        this.color = color;
        this.modelo = modelo;
        this.precio = precio;
        this.descuento = descuento;
        this.new_price = new_price;
        this.new_car = new_car;
    }

    public String my_current_car(){
        return "Car for sale";
    }

    public String my_sold_car(){
        return "Sold!";
    }

    public String my_new_car(String new_car){
        return "My new vehicle will be: "+new_car;
    }
    
    public double new_car_price(double new_price){
        double precio_total = this.new_price - this.descuento;
        return precio_total;
    }
    
    public double new_car_with_discount(double new_price){
        double precio_descuento = this.new_price;
        return precio_descuento;
    }

}


