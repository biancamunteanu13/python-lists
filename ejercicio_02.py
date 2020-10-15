#Nombre: Bianca Munteanu
#Asignatura: Programación para el tratamiento de datos
# Ejercicio 1, ejercicio 2 y ejercicio 3 de la PEC2



# Ejercicio 2: Realizar un programa que guarde los elementos en común que tienen dos listas.

#modulos
def comunes_listas(list1, list2):
    """ list1() + list2() --> list3()
        obj: elemento en comun de ambas listas
        pre: los valores list1 y list 2 son listas de la longitud que queramos"""
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return set(result)  #hacemos set() para que no se repitan los números en una lista infinita en caso de que tengamos muchos datos

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


#código principal
if __name__ == "__main__":
    
    print("----------------------------------------------------------------------------")
    print("\nVamos a sumar dos listas creadas ti. Primero, te pediremos el número de valores que tenddrán las 2 listas")
    print("A continuación, nos indicarás cada valor numérico de las listas, sin decimales")
    print("Por último, en la pantalla nos mostrará los elementos en comun que tienen esas listas.")
    print("\n----------------------------------------------------------------------------")

    lista_prueba = []
    pregunta_1 = pregunta_longitud()
    print("Preparando la lista para introducir valores...")
    creacion_listas(pregunta_1, lista_prueba)
    print("La primera lista es: ", lista_prueba)

    lista_prueba2 = []
    pregunta_2 = pregunta_longitud()
    print("Preparando la lista para introducir valores...")
    creacion_listas(pregunta_2, lista_prueba2)
    print("La segunda lista es: ", lista_prueba2)

    lista_comun = comunes_listas(lista_prueba, lista_prueba2)
    print("Los elementos en común son: ", lista_comun)


