def busqueda_dicotomia(lista, elemento, inicio, fin):
    if inicio > fin:
        return "No hay ningún elemento en la posición seleccionada"
    else: #Dividir la lista en dos partes: Concepto dicotomía
        mitad = (inicio + fin) // 2
        if lista[mitad] == elemento:
            return mitad
        elif lista[mitad] > elemento:
            return busqueda_dicotomia(lista, elemento, inicio, mitad - 1)
        else:
            return busqueda_dicotomia(lista, elemento, mitad + 1, fin)

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(busqueda_dicotomia(lista, 7, 0, len(lista)))
