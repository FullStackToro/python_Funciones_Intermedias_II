#Obtén valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave,
#la función imprima el valor almacenado en esa clave para cada diccionario.
#Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:

def iterarDiccionarios2(x,lista):
    for i in range (len(lista)):
        print(lista[i][x])

students = [
         {'first_name':  'Michael', 'last_name': 'Jordan'},
         {'first_name': 'John', 'last_name': 'Rosales'},
         {'first_name': 'Mark', 'last_name': 'Guillen'},
         {'first_name': 'KB', 'last_name': 'Tonel'}]

iterarDiccionarios2('first_name',students)


