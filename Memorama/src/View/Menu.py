import sys
from Model.jugador import Jugador
#funcion que llama al menu para meter usuario

class Menu:
    def __init__(self,datos):
        self.datos = datos


    def registrarUsuario(self):#recibe como parametros la opcion deseada y el archivo donde vienen las llaves

        nombreUsuario= input("Dame el usuario\n")
        while(nombreUsuario in self.datos):#Siempre que ya este el juegador inscrito te pedira que ingreses otro
            print ("El username ya existe, por favor intenta con otro:\n")
            nombreUsuario = input("Dame el usuario\n")

        contrasena = input("Dame la clave\n")
        confirmacion = input("Repite la clave\n")

        while(contrasena!=confirmacion):

            print("Lo siento pero la contraseña y la confirmacion no son iguales, intenta de nuevo\n")

            contrasena = input("Dame la clave\n")
            confirmacion = input("Repite la clave\n")
        '''
        Obvio un usario simepre va a inicar así...crear otro constructor para usuario
        donde esto se consedere...desṕues cambiar el constructor de abajo apra quitar estos parametros

        puntuacion = 0
        partidas = 0
        ganadas = 0
        '''

        jugador = Jugador(nombreUsuario,contrasena,confirmacion,0,0,0)#Recuerda cambiar este constructor
        usuario = jugador.getUsuario()
        self.datos[usuario] = jugador

        if usuario in self.datos :
            print ('Usuario agregado con exito\n\n'+u"\U0001F60A")
        else :
            print('Error Fatal, usuario no agregado')
            sys.exit()

        return jugador.getUsuario()

    def ingresar(self):

        jugador = input("Dame el usuario\n")

        while(jugador not in self.datos):

            print("Revisa el usuario")
            jugador=input("Dame de nuevo el usuario, revisalo por favor:\n")

        clave=input("Dame la clave\n")

        while(clave!=self.datos[jugador].getContrasena()):

            print("Revisa la contraseña")
            clave=input("Dame la clave de nuevo, revisala bien")


        print("Bienvenido :"+jugador+"\n")#El jugador es bienvenido

        p1=self.datos[jugador]

        return p1.getUsuario()
