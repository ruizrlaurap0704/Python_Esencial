"""
EXCEPCION
def validar_x(x):
    if x < 1:
        raise Exception("La variable x debe ser mayor a 1")
    else:
        print("x es mayor a 1")

x = 0.3
validar_x(x=x)

def calcular_promedio(lista):
    assert len(lista)>0,"La lista esta vacía"
    return sum(lista)/len(lista)

try:
    promedio = calcular_promedio(lista=[])
    print(promedio)
#captura el error detectado con el assert
except AssertionError as assert_error:
    print(assert_error)
#captura cualquier otro tipo de error
except Exception as e:
    print("La función no calculó el promedio")
    print(e)
"""

num_list = [1,2,3,4,5]
num_list.remove(2)
print(num_list)


