public class Producto {
    private String nombre;
    private double precio;
    private String codigo;
    
    public Producto(String nombre, double precio, String codigo) {
        this.nombre = nombre;
        this.precio = precio;
        this.codigo = codigo;
    }
    
    public String getNombre() {
        return nombre;
    }
    
    public double getPrecio() {
        return precio;
    }
    
    public String getCodigo() {
        return codigo;
    }
    
    public String toString() {
        return "Producto: " + nombre + " - Precio: $" + precio + " - Código: " + codigo;
    }
}