from claseViajero import Viajero
import csv

class Controlador:
    __listaviajeros=[]
    def __init__(self):
        self.__listaviajeros = []

    def cargarDatos(self):
        archivo=open("LISTAEJ2.csv")
        reader= csv.reader (archivo, delimiter=",")
        for fila in reader:
            num_viajero=int(fila[0])
            dni=str(fila[1])
            nombre=str(fila[2])
            apellido=str(fila[3])
            millas_acum=int(fila[4])
            viajero=Viajero(num_viajero, dni, nombre, apellido, millas_acum)
            self.__listaviajeros.append(viajero)
        archivo.close()
    def buscar_viajero(self, n):
        i=0
        viajero = None
        while (i < len(self.__listaviajeros) and (self.__listaviajeros[i].retornaViajero() != n)):
            i += 1

        if (i < len(self.__listaviajeros)):
            viajero = self.__listaviajeros[i]
            print ("n: =  ", n)
            print ("lista", self.__listaviajeros[i].retornaViajero())
        return viajero
    
    def buscarMayor (self):
        # i=0
       # mayor = self.__listaviajeros[i].getMillasAcum
        for i in range (len(self.__listaviajeros)-1):
            via = self.__listaviajeros[i+1]
            if self.__listaviajeros[i] > via:
                mayor = self.__listaviajeros[i]
            else:
                mayor = self.__listaviajeros[i+1].getMillasAcum
        print("MAYOR: ", mayor)
        return mayor
    
    def mostrarViajerosMayMillasAcum (self, may):
        print("El/los viajero/s que posee/n mayor cantidad de millas acumuladas es/son:")
        for i in range (len(self.__listaviajeros)):
            if (self.__listaviajeros[i].getMillasAcum == may):
                print("{}{}" .format(self.__listaviajeros[i].getNombre(), self.__listaviajeros[i].getApellido()))
