# Escribir programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra y la  frecuencia

cadena = 'Django es un software para desarrollar aplicaciones web. Es una app de fácil implementación'
def contar_palabras(cadena):
    # split() es un delimitador, el espacio, para serapar los caracteres y contar las frecuencias
    palabras = cadena.split()
    diccionario = {}
    for palabra in palabras:
        # Convertir a minúsculas las palabras
        palabra = palabra.lower()
        if palabra in diccionario :
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

resultado = contar_palabras(cadena)
# items() devuelve una vista de objetos clave, valor del diccionario
for palabra, frec in resultado.items():
    print(f'La palabra: "{palabra}", Aparece {frec} veces')