class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    '''
    Método 'get' y 'set'acceden y modifican los atributos con validaciones. 
    '''
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
            if len(nombre) >= 5:
                self.__nombre = nombre
            else:
                print ('El nombre debe ser mayor a 5 caracteres')
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        if edad <= 0:
            print('Ingresa una edad validad')
        elif edad < 14:
            print('Debes tener una edad mayor')
        else:
            self.__edad = edad 
    def get_dni(self):
        return self.__dni
    def set_dni(self, dni) :
        dni = dni.replace(' ', '').replace('.','')
        if len(dni) != 8:
            print('Debe ingresar un DNI valido')
        else:
            self.__dni = dni
    def mostrar(self):
        return f"{self.__nombre}  {self.__edad}  {self.__dni}"
    def mayor_de_edad(self):
        return self.__edad >= 18 

# Comprobar ejercicio
persona1 = Persona("Javier", 38, "31315000")
print(persona1.mostrar())
print(f"La persona es mayor ? {persona1.mayor_de_edad()}")
print(persona1.set_dni('31 315 000'))
print(persona1.set_edad(5))
print(persona1.set_nombre('Javi'))