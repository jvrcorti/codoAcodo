#Escribir una función que calcule el máximo común dividor
import math

numero_1 = 14
numero_2 = 107

def calcular_mcd(a, b):
    return math.gcd(a, b)

mcd = calcular_mcd(numero_1, numero_2)
print(f'El MCD entre {numero_1} y {numero_2} es {mcd}')

# Escribir una función que calcule el mínimo común múltiplo
def calcular_mcm(a, b):
    return math.lcm(a, b)

mcm = calcular_mcm(numero_1, numero_2)
print(f'El mcm entre el #: {numero_1} y {numero_2} es: {mcm}')
    
