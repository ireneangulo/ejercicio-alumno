class Alumno:
    
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumno creado con exito")
 
    def calificacion(self):
        if self.nota < 5:
            print("El alumno {} ha suspendido".format(self.nombre))
        else:
            print("El alumno {} ha aprobado".format(self.nombre))
 

alumno1 = Alumno("Juan", 7)
alumno2 = Alumno("Alfredo", 3)
 

alumno1.calificacion()
alumno2.calificacion()