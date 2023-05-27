#HERENCIA: Subclase (Clase hija) hereda los atributos y metodos de una super clase (Clase padre)

class Persona:
    def __init__(self, Nombre, Edad, DNI):
        self.nombre = Nombre
        self.edad = Edad
        self.dni = DNI

    def presentacion(self):
        print(f"Mucho gusto soy {self.nombre} tengo {self.edad} años")
Persona1 = Persona("Yulieth", 18, "1386308120")
Persona1.presentacion()

class Docente(Persona):
        def __init__(self, Nombre, Edad, DNI, Especialidad, Submodulos, Universidad):
            super().__init__(Nombre, Edad, DNI)
            self.especialidad = Especialidad
            self.submodulos = Submodulos
            self.universidad = Universidad
Docente1 = Docente("Luisa", 25, "1057458958", "Matematicas", "Algebra", "Cesde")
Docente1.presentacion()
print(Docente1.especialidad)

class Estudiante(Persona):
    def __init__(self, Nombre, Edad, DNI, Cursos, Aula, Semestre, Nota):
        super().__init__(Nombre, Edad, DNI)
        self.cursos = Cursos
        self.aula = Aula
        self.semestre = Semestre
        self.nota = Nota
    def Aprobacion(self):
        if self.nota >= 3.0:
            print("Aprobo")
        else:
            print("Reprobo")
Estudiante1 = Estudiante("Karen", 24, "1216444485", "Python", 405, 3, 2.9)
Estudiante1.presentacion()
Estudiante1.Aprobacion()