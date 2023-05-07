class Viajero:
    __num_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self, num_viajero='', dni='', nombre='', apellido='', millas_acum=''):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
    def cantidadTotaldeMillas(self):
        return (self.__millas_acum)
    def acumularMillas(self, cant_recorrida):
        self.__millas_acum = self.__millas_acum + cant_recorrida
        return (self.__millas_acum)
    def canjearMillas (self, cantAcanjear):
        if cantAcanjear <= self.__millas_acum:
            self.__millas_acum = self.__millas_acum - cantAcanjear
        else:
            print("No puede realizarse la operación, las millas a canjear son superiores a las que se encuentran disponibles.")
        return (self.__millas_acum)
    def retornaViajero (self):
        return self.__num_viajero
    
    def getMillasAcum (self):
        return (self.__millas_acum)
    
    def __gt__(self, instancia2):
        return self.__millas_acum > instancia2.getMillasAcum()
    
    def getNombre(self):
        return(self.__nombre)
    
    def getApellido(self):
        return(self.__apellido)
    
    def __add__(self, millas):
        return (self.__millas_acum + millas)
    
    def __radd__ (self, millas):
        return (self.__millas_acum + millas)

    def __sub__ (self, millas):
        return(self.__millas_acum - millas)
    
    def __rsub__ (self, millas):
        return(self.__millas_acum - millas)
        
    def __eq__(self, millas):
        return(self.__millas_acum == millas)