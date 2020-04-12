from Model.jugador import Jugador
import shelve
from View.Menu import Menu
from View.tablero import *
from Controller.juego import juego
datos=shelve.open("Datos.dat")

opcion=0

while(int(opcion)!=1 and int(opcion)!=2):
    print ("Opcion invalida\nPor favor seleccione una opcion valida:\n"

           "1.- Registar Jugador\n"
           "2.-Iniciar Sesion\n")
    opcion = input("==> ")

menu = Menu(datos)
jugadorActual=" HOLA"
if opcion == "1":
    jugadorActual = menu.registrarUsuario()

if opcion == "2":
    jugadorActual = menu.ingresar()



sele=0

while(int(sele)<=3):
    print ("Hola\t"+jugadorActual)
    print ("Seleccione una opcion por favor "+jugadorActual)
    print ("1.-Jugar")
    print ("2.-Ver estadisticas")
    print ("3.-Borrar historial")
    print ("4.-Salir")
    sele= input("Escribe tu seleccion: \n")

    if(sele=="1"):

        datos[jugadorActual]=juego(datos[jugadorActual])

    if (sele=="2"):
    #abrir estadisticas

        print ("Partidas jugadas:\t"+str(datos[jugadorActual].getPartidas()))
        print ("Partidas ganadas:\t"+str(datos[jugadorActual].ganadas))
        print ("Partidas perdidas:\t"+str(int(datos[jugadorActual].partidas)-int(datos[jugadorActual].ganadas)))
        print("Maxima puntuacion:\t"+str(datos[jugadorActual].puntuacion))

    if (sele=="3"):
        #reestablecer en 0 las estadisticas
        p1=datos[jugadorActual]
        p1.partidas=0
        p1.ganadas=0
        p1.puntuacion=0
        datos[jugador]=p1
        print("Tus datos se han restablecido a 0")
    if(sele=="4" or sele=="salir"):
        print("Adios "+jugadorActual+" espero tenerte pronto por aqui de nuevo")
        break
