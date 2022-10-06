"""
class Persona:
    pass

pedro = Persona()
print(type(pedro))

paco = Persona()
print(type(paco))

print(pedro==paco)
"""
"""
#CONSTRUCTOR DE LA CLASE
class Persona:
    def __init__(self):
        print("Estoy en el Constructor")

paco = Persona()
"""
"""
class Persona:
    #ATRIBUTO DE LA CLASE
    atributo = 123
    def __init__(self,nombre,edad):
        #ATRIBUTO DE LA INSTANCIA
        self.nombre = nombre
        self.edad = edad

paco = Persona("Paco",20)
print(paco.nombre)
print(paco.edad)
print(paco.atributo)
"""
class Persona:
    #CONSTRUCTOR
    def __init__(self,nombre,edad):
        #ATRIBUTO DE LA INSTANCIA
        self.nombre = nombre
        self.edad = edad
    #METODO DE CLASE -> PRIMER PARAMETRO self
    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños # {self.edad} {self.nombre}")

#HERENCIA
class Empleado(Persona):
    #CONSTRUCTOR
    def __init__(self, nombre, edad,horas_totales):
        super(Empleado,self).__init__(nombre, edad)
        self.horas_totales = horas_totales
    #METODO DE CLASE
    def trabajar(self,horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"Usted ha trabajdo {horas_trabajadas} horas")
        print(f"Horas Totales {self.horas_totales} horas")

laura = Empleado(nombre="Laura",edad=35,horas_totales=30)
laura.trabajar(horas_trabajadas=8)
laura.cumplir_anios()