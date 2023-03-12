'''
1. Búsqueda por dicotomía en una tabla ordenada
El capítulo «Iteración» ha resuelto el problema definiendo una función iterativa.

Ejercicio resuelto 5: Búsqueda recursiva por dicotomía en una tabla ordenada





Se pide resolver el mismo problema definiendo una función recursiva.

Puede encontrar una solución estudiada de este ejercicio en los complementos disponibles para descargar desde la página Información.
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = lista.sort()  # Ordenar la lista
valor = 5
def busqueda_dicotomia(lista, valor):
    if len(lista) == 0:
        return False
    else:
        medio = len(lista) // 2 # Dividir la lista en dos
        if lista[medio] == valor: # Si el valor está en la mitad
            return medio
        elif lista[medio] > valor: # Si el valor está en la primera mitad
            return busqueda_dicotomia(lista[:medio], valor) #LISTA[0,valor medio]
        else: # Si el valor está en la segunda mitad
            return busqueda_dicotomia(lista[medio+1:], valor) #LISTA[valor medio + 1,longitud lista]
