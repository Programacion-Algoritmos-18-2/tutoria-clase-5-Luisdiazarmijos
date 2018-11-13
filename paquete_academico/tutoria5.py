class Ciudad(object):
 
    def __init__(self):
        self.nombre=" "
        self.poblacion=" "
        
    def agregar_nombre(self,nombre):
        self.nombre=nombre
        pass
    def obtener_nombre(self):
        return nombre 
    def agregar_poblacion(self,poblacion):
        self.poblacion
        pass
    def obtener_poblacion(self)
        return poblacion

class Persona(object):
    def __init__(self):
        self.nombre =" "
        self.apellido=" "
        self.ciudad=" "

    #Agregamos los agregar y presentar 
    def agregar_nombre(self, nombre):
        self.nombre
        pass
    def obtener_nombre(self):
        return self.nombre
        pass

    def agregar_apellido(self, a):  
        self.apellido = a

    def obtener_apellido(self):
        return self.apellido
    def agregar_ciudad(self, c):
        self.ciudad = c
        pass
    def obtener_ciudad(self):
        return self.ciudad
        pass
    
class Estudiante(Persona):
    def __init__(self):
        super(Estudiante, self).__init__()
        self.ID_estudiante=0
    def agregar_ID_estudiante(self,id):
        self.ID_estudiante=id
        pass
    def obtener_ID_estudiante(self):
        return self.ID_estudiante
        pass
   
      

class EstPresencial(Estudiante):
    def __init__(self):
        super(EstPresencial, self).__init__()
        self.ciclo=0
        self.numero_creditos=0
        pass
    def agregar_ciclo(self,ciclo):
        self.ciclo=ciclo
        pass
    def obtener_ciclo(self):
        return ciclo
        pass
    def agregar_numero_creditos(self,numero_creditos):
        self.numero_creditos=numero_creditos
        pass
    def obtener_numero_creditos(self):
        return numero_creditos
        pass
    def presentar_datos(self):
      cadena ="%s%s\n ciclo: %s\n numero_creditos:  %s\nPertenece a la ciudad%s,con una poblacion de %d"%(self.obtener_nombre(),self.obtener_apellido(), self.obtener_ciclo(),self.obtener_numero_creditos(),
        self.obtener_ciudad().obtener_nombre(),self.obtener_ciudad.obtener_poblacion())
class EstDistancia(Estudiante):
    def __init__(self):
        super(EstDistancia, self).__init__()
        self.modulo=0
        self.numero_materias=0
        pass
    def agregar_modulo(self, modulo):
        self.modulo=modulo
        pass
    def obtener_modulo(self):
        return modulo
        pass
    def agregar_numero_materias(self, numero_materias):
        self.numero_materias=numero_materias
        pass
    def obtener_numero_materias(self):
        return numero_materias
        pass
                                                                         