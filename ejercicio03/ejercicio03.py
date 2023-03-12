def bandera_dijkstra():
    import random
    bandera = []
    for i in range(18):
        color = random.randint(0, 2)
        if color == 0:
            bandera.append('R') #R es rojo
        elif color == 1:
            bandera.append('V') #V es verde
        else:
            bandera.append('A') #A es azul
    return bandera

def ordenar_dijkstra(bandera): #Orden es: R, V, A
    colores = {'R': 0, 'V': 0, 'A': 0}
    i = 0
    for color in bandera:
        colores[color] += 1 #Cuenta la cantidad de veces que aparece cada color
    for i in range(colores['R']): #Rellena con la R
        bandera[i] = 'R'
    for i in range(colores['V']):
        bandera[i + colores['R']] = 'V' #Suma el total de R y V para rellenar con V
    for i in range(colores['A']):
        bandera[i + colores['R'] + colores['V']] = 'A' #Suma el total de R, V y A para rellenar con A
    return bandera


if __name__ == '__main__':
    bandera = bandera_dijkstra()
    print(bandera)
    bandera_ordenada = ordenar_dijkstra(bandera)
    print("La bandera ordenada", bandera_ordenada)
