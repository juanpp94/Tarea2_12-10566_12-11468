from datetime import date
from datetime import datetime

class Persona():
    edad = 0
    semanas = 10
    genero = ""
    fechaNacimiento = 0
    

    #Metodo para asignar la edad a la persona
    def setEdad(self,edad):
        self.edad = edad

    #Metodo para asignar la cantidad de semanas de 
    #rotacion a la persona
    def setSemanasRotacion(self,semanas):
        self.semanas = semanas

    #Metodo para asignar el genero a una persona
    def setGenero(self,genero):
        self.genero = genero

    #Metodo para determinar la edad minima de una persona
    #segun su genero para que pueda optar por pension
    def edadMinimaParaOptarPorPension(self,genero):
        if genero == "Hombre":
            return 60
        else:
            return 55

    #Metodo para determinar si tiene derecho a pension segun la
    #cantidad de semanas de rotacion
    def tieneDerechoPension(self):
        return self.semanas >= 750 
