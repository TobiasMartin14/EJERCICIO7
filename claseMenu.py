from claseViajero import Viajero
from controladorViajeros import Controlador
class Menu:
    __opcion = 0
    def __init__ (self):
        self.__opcion = 0
    def opciones(self, r):
        indice = True
        while indice:
            print ("Opcion 1: Consultar Cantidad de Millas")
            print ("Opcion 2: Acumular Millas")
            print ("Opcion 3: Canjear Millas")
            print ("Opcion 4: Salir")
            self.__opcion = int(input("Seleccione una opcion: "))
            if (self.__opcion == 1):
                print("", r.cantidadTotaldeMillas() )
            elif (self.__opcion == 2):
                cantrecorrida = int(input("Ingrese la cantidad recorrida a acumular: "))
                print("", r.acumularMillas(cantrecorrida))
            elif (self.__opcion == 3):
                cantacanjear = int(input("Ingrese la cantidad de millas a canjear: "))
                print("", r.canjearMillas(cantacanjear))
            elif (self.__opcion == 4):
                indice = False
            else:
                print("La opcion ingresada no es valida.")