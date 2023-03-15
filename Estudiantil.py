from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self,nombre,edad,carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
    
    @abstractmethod
    def saludar(self):
        pass

class Estudiante(Persona):
    def __init__(self,nombre, edad, carrera,genero):
        super().__init__(nombre,edad,carrera)
        self.genero = genero
    
    def saludar(self):
        return "El estudiante {} con la edad de {} de la carrera  de {} pertenece al genero {}".format(self.nombre,self.edad,self.carrera,self.genero)

class Profesor(Persona):
    def __init__(self,nombre,edad,carrera,materia):
        super().__init__(nombre,edad,carrera)
        self.materia = materia
    
    def saludar(self):
        return "El profesor {} con la edad de {} de la carrera {}, imparte la materia de {}".format(self.nombre,self.edad,self.carrera,self.materia)
    
class Empleado(Persona):
    def __init__(self,nombre,edad,carrera,puesto):
        super().__init__(nombre,edad,carrera)
        self.puesto = puesto
    
    def saludar(self):
        return "El empleado {} de {} de edad, con la carrera de {} , esta en el puesto de {}".format(self.nombre,self.edad,self.carrera,self.puesto)

 
estudiante = Estudiante("Roberto","19","ing en sistemas","masculino")
print(estudiante.saludar())
profesor = Profesor("Eliseo","32","Ing. civil","Redes Informaticas")
print(profesor.saludar())
empleado = Empleado("Oscar","23","Lic en comunicaciones","Auditora Interna")
print(empleado.saludar())
