#DATOS
acento_sustitucion = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', 'Á':'A', 'É':'E', 'Í':'I', 'Ó':'O', 'Ú':'U'}

def caracteres_alfanumericos(cadena):
    if cadena.isalnum(): # isalnum() devuelve True si la cadena es alfanumérica
        return cadena
    else:
        return "La cadena no es alfanumérica"



def reconocer_palindromos(cadena):
    '''1. FILTRAR EL TEXTO PARA CONSERVAR CARACTERES ALFANUMÉRICOS'''
    caracteres_alfanumericos(cadena)
    '''2. SUSTITUIR LOS CARACTERES ACENTUADOS POR SUS EQUIVALENTES SIN ACENTO'''
    for x in cadena:
        if x in acento_sustitucion:
            cadena = cadena.replace(x, acento_sustitucion[x]) # replace() sustituye un caracter por otro
    '''3. PASAR EL TEXTO A MINÚSCULAS'''
    cadena = cadena.lower()
    '''4. ELIMINAR LOS ESPACIOS EN BLANCO'''
    cadena = cadena.replace(" ", "") # replace() sustituye un caracter por otro
    '''5. COMPROBAR SI LA CADENA ES UN PALÍNDROMO'''
    if cadena == cadena[::-1]: # [::-1] devuelve la cadena al revés
        return "La cadena es un palíndromo:" + cadena
    else:
        return "La cadena no es un palíndromo"

if __name__ == "__main__":
    print(reconocer_palindromos(cadena = 'Logré ver gol')) #True
    print(reconocer_palindromos(cadena = 'OSO')) #True
    print(reconocer_palindromos(cadena = 'Dábale arroz a la zorra el abad')) #True
    print(reconocer_palindromos(cadena = '10000000000000000001')) #True
    print(reconocer_palindromos(cadena = '1754571')) #True
    print(reconocer_palindromos(cadena = 'HOLA')) #False
