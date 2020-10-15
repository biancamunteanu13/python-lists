#Nombre: Bianca Munteanu
#Asignatura: Programación para el tratamiento de datos
# Ejercicio 1, ejercicio 2 y ejercicio 3 de la PEC2




# Ejercicio 1: Realizar un programa que sume dos listas de diferente longitud 
# y retorne otra lista que contenga la suma de las originales elemento a elemento más los elementos sobrantes de la lista más larga.


# Definimos los módulos
def pregunta_longitud():
    """int
        obj: preguntar al usuario cuantos valores quiere que tenga su lista
        pre: no tiene valor porque se le asignará una variable"""
    return int(input("¿Cuántos valores quieres que tenga la lista? "))


# x: longitud de la lista
# y: nombre de la lista vacía creada
def creacion_listas(x, y):
    """ int, list --> list
        obj: rellenar una lista vacia
        pre: x: longitud de la lista 
            y: nombre de la lista vacia """
    for i in range(x):
        i = int(input("Escribe el valor de la posicion %i: " %i))
        y.append(i)
    return y


# Código principal
if __name__ == "__main__":
    
    print("----------------------------------------------------------------------------")
    print("\nVamos a sumar dos listas creadas ti. Primero, te pediremos el número de valores que tenddrán las 2 listas")
    print("A continuación, nos indicarás cada valor numérico de las listas, sin decimales")
    print("Por último, sumaremos esas dos listas para crear una más grande.")
    print("\n----------------------------------------------------------------------------")

    lista1 = []
    longitud_1 = pregunta_longitud()
    print("Preparando la lista para introducir valores...")

    creacion_listas(longitud_1, lista1)
    print("La primera lista es: ", lista1)

    print("\nVamos con la segunda lista: ")

    lista2 = []
    longitud_2 = pregunta_longitud()
    print("Preparando la lista para introducir valores...")

    creacion_listas(longitud_2, lista2)
    print("La segunda lista es: ", lista2)

    print("\nSumando las dos listas...")
    from itertools import zip_longest
    lista3 = list(map(sum, zip_longest(lista1, lista2, fillvalue=0)))
    print("La lista final es: ", lista3)

