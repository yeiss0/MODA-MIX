
# Integrantes: Fredy fandiño y jeison Rodriguez

class Persona:
    total_ingresados=0
    
    def __init__(self,nombre,edad): #atributos
        self.nombre =nombre
        self.edad= edad
        Persona.total_ingresados +=1 #aumenta el contador dependiendo el numero de personas ingresadas
        
    def saludar(self): #metodo
        print ( f" Bienvenido al sistema Ingreso a la U, tu nombre es: {self.nombre} y tu edad es: {self.edad} años")
    
class Estudiante(Persona):
    
    total_est_ingresados = 0
    
    def __init__(self, nombre, edad,carrera,semestre):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.semestre = semestre
        Estudiante.total_est_ingresados +=1
    
    def mostrar__informacion(self):
        print( f" El nombre ingresado es {self.nombre}, la edad registrada es {self.edad} y esta matriculado en la carrera {self.carrera} con ubicacion semestral {self.semestre}")
    
class Admin(Persona):
    
    total_admin__ingresados=0
    
    def __init__(self, nombre, edad,areaTrabajo,horario):
        super().__init__(nombre, edad)
        self.areaTrabajo = areaTrabajo
        self.horario = horario
        Admin.total_admin__ingresados +=1
    
    def  mostrar__informacion(self):
        print (f" nombre admin: {self.nombre}, edad {self.edad} , área {self.areaTrabajo} horario  {self.horario}")
        
# Personas ingresadas 
persona1 = Persona("antonella",26)
persona1.saludar()


# Estudiantes Ingresados 
estudidante1 = Estudiante("Julian torres",18,"contaduria",5)
estudidante1.mostrar__informacion()

#Admin 
admin1 = Admin("juana pineda",38,"Secretaria","diurno")
admin1.mostrar__informacion()

print(f"Total de personas: {Persona.total_ingresados}")
print(f"Total de estudiantes: {Estudiante.total_est_ingresados}")
print(f"Total de administrativos: {Admin.total_admin__ingresados}")
        
    
    
    
    