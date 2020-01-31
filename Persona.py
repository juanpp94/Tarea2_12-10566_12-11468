class Persona():
    edad = 0
    semanas = 10
    genero = ""

    #Metodo para asignar la edad a la persona
    def setEdad(self,edad):
        self.edad = edad

    #Metodo para asignar la cantidad de semanas de 
    #rotacion a la persona
    def setSemanasRotacion(self,semanas):
        self.semanas = semanas

    def setGenero(self,genero):
        self.genero = genero
    
    def tieneDerechoPension(self):
        return True