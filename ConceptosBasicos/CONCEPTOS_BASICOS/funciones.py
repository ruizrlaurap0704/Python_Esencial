
APELLIDO = "Ruiz"
def funcion ():
    print("Mi primera función")
    nombre="Laura"
    print(nombre,APELLIDO)

funcion()

def perimetro_cuadrado(lado,unidades):
    perimetro = lado*4
    print(f"El perimetro es {perimetro} {unidades}")

perimetro_cuadrado(2,"metros")
perimetro_cuadrado(lado=2,unidades="metros")

def perimetro_cuadrado(lado):
    perimetro = lado*4
    return perimetro

def area_cuadrado(lado):
    area = lado*lado
    return area

perimetro = perimetro_cuadrado(2)
area = area_cuadrado(2)

print(f"Area: {area}, perimetro:{perimetro}")

def calcular_cuadrado(lado):
    perimetro = lado*4
    return perimetro

perimetro=calcular_cuadrado(2)
print(f"perimetro:{perimetro}")


