from Empleado import Empleado

class ArchivoEmpleado:
    def __init__(self, nomA: str):
        self.nomA = nomA
    
    def crearArchivo(self):
        with open(self.nomA, 'w') as f:
            f.write("")
    
    def guardarEmpleado(self, e: 'Empleado'):
        with open(self.nomA, 'a') as f:
            f.write(f"{e.nombre},{e.edad},{e.salario}\n")
    
    def buscaEmpleado(self, n: str):
        with open(self.nomA, 'r') as f:
            for line in f:
                nombre, edad, salario = line.strip().split(',')
                if nombre == n:
                    return Empleado(nombre, int(edad), float(salario))
        return None
    
    def mayorSalario(self, s: float):
        with open(self.nomA, 'r') as f:
            for line in f:
                nombre, edad, salario = line.strip().split(',')
                if float(salario) > s:
                    return Empleado(nombre, int(edad), float(salario))
        return None