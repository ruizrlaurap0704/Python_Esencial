"""
a = 2;
b = 2;
if a<b:
    print("A es menor que B")
elif a==b:
    print("A es igual a B")
else:
    print("A es mayor que B")
"""
"""
a=True
if type(a) is bool:
    print("A es booleano")
else:
    print("A es otro tipo de dato")
"""
"""
a=10
b=5
c=1
if a>b and b>c:
    print("Las dos condiciones son verdaderas")
"""
"""
lenguajes = ["Python","Java","Go"]

for elemento in lenguajes:
    print(elemento)
    if elemento == "Java":
        break
"""
"""
lenguajes = ["Python","Java","Go"]
for elemento in lenguajes:
    if elemento == "Java":
        continue
    print(elemento)

for element in range(0,5):
    print(element)

i = 1
while i<=5:
    print(i)
    i+=1
    if i==3:
        break

lenguajes = ["python","java","go"]
for elemento in lenguajes:
    print(elemento)

lenguajes = ["python","java","go"]
for index in range(len(lenguajes)):
    print("indice",index)
    print("elemento",lenguajes[index])

lenguajes = ["python","java","go"]
i = 0
while i<len(lenguajes):
    print(lenguajes[i])
    i += 1

lenguaje = {
    "nombre":"Python",
    "creador":"Guido Van Rossu"
}

for llave in lenguaje:
    print("llave:",llave)
    print("valor:",lenguaje[llave])
lenguaje = {
    "nombre":"Python",
    "creador":"Guido Van Rossu"
}
for elemento in lenguaje.keys():
    print(elemento)

lenguaje = {
    "nombre":"Python",
    "creador":"Guido Van Rossu"
}
for elemento in lenguaje.values():
    print(elemento)
""" 
lenguaje = {
    "nombre":"Python",
    "creador":"Guido Van Rossu"
}
for llave,valor in lenguaje.items():
    print(llave,valor)