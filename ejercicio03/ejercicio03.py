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
    bandera_ordenada = []
    for i in range

if __name__ == '__main__':
    bandera = bandera_dijkstra()
    print(bandera)
    bandera_ordenada = ordenar_dijkstra(bandera)
    print("La bandera ordenada", bandera_ordenada)
