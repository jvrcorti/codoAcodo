from ejercicio7 import Persona, Cuenta


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)  # llamo a la instancia madre Cuenta
        self.bonificacion = bonificacion  # Agrego la bonificacion a la cuentaJoven

    def get_bonificacion(self):
        return self.bonificacion
    # def set_bonificacion(self, bonificacion):
    #    if 0 <= bonificacion <= 100:
    #        self.bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        return self.cantidad + (self.cantidad * self.bonificacion)

    def es_titular_valido(self):
        edad = int(input('Çuál es tu edad: '))
        self.edad = edad
        return 18 <= edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            return super().retirar(cantidad)
        else:
            print("No puedes realizar retiros")

    def mostrar(self):
        return print('"Cuenta Joven"' '\n' "Bonificacion:", self.get_bonificacion())


# Pruebas del ejercicio
cuenta_joven = Persona('Javier Corti')
cuenta_javier = CuentaJoven(cuenta_joven, 500, 25)
cuenta_javier.mostrar()
cuenta_javier.retirar(200)
