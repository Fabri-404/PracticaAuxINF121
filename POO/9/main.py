


from computadora import Computadora

if __name__ == "__main__":
    #A
    mi_pc = Computadora("Intel i9", "16GB", "SSD 512GB", "ASUS")

    print("Componentes de la computadora")
    mi_pc.componentes()
    #B
    mi_pc.estado()
    print("Encendiendo")
    mi_pc.encender()
    mi_pc.estado()
    #C
    print("Intentando Encender de nuevo")
    mi_pc.encender()
    print("Apagando")
    mi_pc.apagar()
    mi_pc.estado()
    #C
    print("Intentando Apagar de nuevo")
    mi_pc.apagar()
