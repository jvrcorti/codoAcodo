# Implementación iterativa
def get_int():
    while True:
        try:
            numero = int(input('Ingrese un número: '))
            return numero
        except ValueError:
            print('Número invalido! Ingrese solo números enteros')
            #break
numero = get_int()
print ('El número ingresado es: ', numero)

# Implementación recursiva
def get_init():
    try:
        numero = int(input('Ingrese un número: '))
        return numero
    except ValueError:
        print('Valor invalido Vuelva a intentarlo.')
        return get_int()

recursiva = get_init()
print (f'Ha ingresado el siguiente número: {recursiva}')