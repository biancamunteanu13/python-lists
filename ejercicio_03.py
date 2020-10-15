#Nombre: Bianca Munteanu
#Asignatura: Programación para el tratamiento de datos
# Ejercicio 1, ejercicio 2 y ejercicio 3 de la PEC2





# Ejercicio 3: Realizar un programa que retorne el número de elementos comunes iniciales de dos listas
#modulo
def numero_comunes_listas(list1, list2):
    """ list1() + list2() --> int()
        obj: nr de elemento en comun de ambas listas
        pre: los valores list1 y list 2 son listas de la longitud que queramos"""
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return len(result)

def pregunta_longitud():
    """int
        obj: preguntar al usuario cuantos valores quiere que tenga su lista
        pre: no tiene valor porque se le asignará una variable"""
    return int(input("¿Cuántos valores quieres que tenga la lista? "))

def creacion_listas(x, y):
    """ int, list --> list
        obj: rellenar una lista vacia
        pre: x: longitud de la lista 
            y: nombre de la lista vacia """
    for i in range(x):
        i = int(input("Escribe el valor de la posicion %i: " %i))
        y.append(i)
    return y

#codigo principal
if __name__ == "__main__":
    
    print("----------------------------------------------------------------------------")
    print("\nVamos a sumar dos listas creadas ti. Primero, te pediremos el número de valores que tenddrán las 2 listas")
    print("A continuación, nos indicarás cada valor numérico de las listas, sin decimales")
    print("Por último, en la pantalla nos mostrará el numero de elementos en comun que tienen esas listas.")
    print("\n----------------------------------------------------------------------------")

    lista_numero = []
    pregunta_3 = pregunta_longitud()
    print("Preparando la lista para introducir valores...")
    creacion_listas(pregunta_3, lista_numero)
    print("La primera lista es: ", lista_numero)

    lista_numero2 = []
    pregunta_4 = pregunta_longitud()
    print("Preparando la lista para introducir valores...")
    creacion_listas(pregunta_4, lista_numero2)
    print("La segunda lista es: ", lista_numero2)

    numero_comunes= numero_comunes_listas(lista_numero, lista_numero2)

    print("Número de elementos comunes en las dos listas:", numero_comunes)