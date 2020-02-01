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

    #Metodo para asignar fecha de nacimiento de una persona
    def setFechaNacimiento(self,fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento


    #Metodo para determinar la edad minima de una persona
    #segun su genero para que pueda optar por pension
    def edadMinimaParaOptarPorPension(self,genero):
        if genero == "Hombre":
            return 60
        else:
            return 55
    
    #Metodo para determinar si una persona tiene la edad minima para 
    #optar por la pension
    def tieneEdadParaOptarPension(self,genero,edad):
        if genero == "hombre":
            if edad >= self.edadMinimaParaOptarPorPension(genero):
                return True
            else:
                return False
        else:
            if edad >= self.edadMinimaParaOptarPorPension(genero):
                return True
            else:
                return False

    
    #Metodo para determinar si tiene derecho a pension segun la
    #cantidad de semanas de rotacion
    def tieneDerechoPension(self):
        tienEdadParaPension = self.tieneEdadParaOptarPension(self.genero,self.edad)
        return self.semanas >= 750 & tienEdadParaPension
