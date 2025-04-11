from Persona import Persona

if __name__ == "__main__":
    P1= Persona("Fabricio", 20, "La Paz")
    P2= Persona("Steve", 15, "Cochabamba")
    P3= Persona("LuisitoComunica", 33, "Santa Puej")

    print("Saludo")
    
    P1.mostrar_el_saludo()
    P2.mostrar_el_saludo()
    P3.mostrar_el_saludo()

    print("Mayor de edad")

    print (f"{P1.nombre} es mayor de edad? {'Si' if P1.es_mayor_de_edad() else 'No'}")
    print (f"{P2.nombre} es mayor de edad? {'Si' if P2.es_mayor_de_edad() else 'No'}")
    print (f"{P3.nombre} es mayor de edad? {'Si' if P3.es_mayor_de_edad() else 'No'}")