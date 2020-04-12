#clase constructor para crear un jugador nuevo, crea metodos para obtener sus atributos
class Jugador:
    def __init__(self,usuario,contrasena,confirmacion,puntuacion,partidas,ganadas):
        self.usuario=usuario
        self.contrasena=contrasena
        self.confirmacion=confirmacion
        self.puntuacion=puntuacion
        self.partidas=partidas
        self.ganadas=ganadas

    def __str__(self):
        return (self.usuario+"\t"+self.contrasena+"\t"+str(self.puntuacion)+"\t"+str(self.partidas)+"\t"+str(self.ganadas))

    def getUsuario(self):
        return self.usuario

    def getContrasena(self):
        return self.contrasena

    def getPuntuacion(self):
        return self.puntuacion

    def serPuntuacion(self, puntuacion):
        self.puntuacion=puntuacion

    def getPartidas(self):
        return self.partidas

    def setPartidas(self,partidas):
        self.partidas=partidas

    def getGanadas(self):
        return self.ganadas
