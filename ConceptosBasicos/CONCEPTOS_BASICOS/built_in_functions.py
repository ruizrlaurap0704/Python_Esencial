print()

""" LISTAS 
>>> lenguajes = ["python","Java","Go"]
>>> lenguajes
['python', 'Java', 'Go']
>>> lista = [1,2.3,True,"Python",1]
>>> lista
[1, 2.3, True, 'Python', 1]
>>> lenguajes[0]
'python'
>>> len(lenguajes)
3
>>> lenguajes[-1]
'Go'
>>> lenguajes[-3]
'python'
>>> lenguajes[0:2]
['python', 'Java']
>>> programacion = [lenguajes,"dedicacion","practica"]
>>> programacion
[['python', 'Java', 'Go'], 'dedicacion', 'practica']
>>> programacion[0][0]
'python'
>>>
>>> lenguajes[0] = "JavaScript"
>>> lenguajes
['JavaScript', 'Java', 'Go']
>>> lenguajes.append("SQL")
>>> lenguajes
['JavaScript', 'Java', 'Go', 'SQL']
>>> lenguajes.append("Python")
>>> lenguajes
['JavaScript', 'Java', 'Go', 'SQL', 'Python']
>>> otros_lenguajes = ["C","C++"]
>>> lenguajes.extend(otros_lenguajes)
>>> lenguajes
['JavaScript', 'Java', 'Go', 'SQL', 'Python', 'C', 'C++']
>>> lenguajes.extend(otros_lenguajes)
>>> lenguajes
['JavaScript', 'Java', 'Go', 'SQL', 'Python', 'C', 'C++', 'C', 'C++'] 

TUPLAS - A diferencia de las listas son inmutables
>>> lenguajes = ("python","C","C++")
>>> lenguajes
('python', 'C', 'C++')
>>> lenguajes = "python","C","C++"
>>> lenguajes
('python', 'C', 'C++')
>>> lenguajes[0] 
'python'
>>> lenguajes[-1]
'C++'
>>> 

DICCIONARIOS - Almancenan información en pares de datos. Cada valor corresponde a una llave. HashMap ó JASON
Las llaves con inmutables. Las llaves son tipo texto. Las llaves son únicas. Tipo texto. Puede ser anidado
>>> lenguaje ={
... "nombre":"python",
... "creador":"Guido"}
>>> lenguaje
{'nombre': 'python', 'creador': 'Guido'}
>>> lenguaje["nombre"]
'python'
>>> lenguaje["anio"]=19991
>>> lenguaje
{'nombre': 'python', 'creador': 'Guido', 'anio': 19991}
>>> lenguaje["anio"]=1999
>>> lenguaje
{'nombre': 'python', 'creador': 'Guido', 'anio': 1999}
>>> nombre["caracteristicas"]=["sencillo","facil","genial"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'nombre' is not defined
>>> lenguaje["caracteristicas"]=["sencillo","facil","genial"]
>>> lenguaje
{'nombre': 'python', 'creador': 'Guido', 'anio': 1999, 'caracteristicas': ['sencillo', 'facil', 'genial']}
>>> lenguaje.items()
dict_items([('nombre', 'python'), ('creador', 'Guido'), ('anio', 1999), ('caracteristicas', ['sencillo', 'facil', 'genial'])])
>>> lenguaje.keys()
dict_keys(['nombre', 'creador', 'anio', 'caracteristicas'])
>>> lenguaje.values()
dict_values(['python', 'Guido', 1999, ['sencillo', 'facil', 'genial']])

"""
