# Representa al títular de la cuenta
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        # Atributo no se puede modificar <cantidad> es privado
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad

    def mostrar(self):
        print(f'"TITULAR", {self.__titular.nombre}')
        print("CANTIDAD", self.cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad


# Crear la Persona, titular
titular_persona = Persona('Javier Corti')

# Crear la cuenta
cuenta_javier = Cuenta(titular_persona, 512)

# Ingresar y retirar de la cuenta
print(cuenta_javier.ingresar(-50))
print(cuenta_javier.retirar(1))
print(cuenta_javier.mostrar())
