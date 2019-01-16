from jugador import Jugador
import shelve
from menu import menu
from tablero import *
from juego import juego
datos=shelve.open("Datos.dat")
opcion=0
while(int(opcion)!=1 and int(opcion)!=2):
    print ("Opcion invalida\nPor favor seleccione una opcion valida:\n"
           
           "1.- Registar Jugador\n"
           "2.-Iniciar Sesion\n")
    opcion = input("==> ")
jugador=menu(opcion,datos)
    


p1=datos[jugador]
sele=0

while(int(sele)<=3):
    print ("Hola\t"+jugador)
    print ("Seleccione una opcion por favor "+jugador)
    print ("1.-Jugar")
    print ("2.-Ver estadisticas")
    print ("3.-Borrar historial")
    print ("4.-Salir")
    sele= input("Escribe tu seleccion: \n")

    if(sele=="1"):
    
        datos[jugador]=juego(p1)
    
    if (sele=="2"):
    #abrir estadisticas

        print ("Partidas jugadas:\t"+str(datos[jugador].getPartidas()))
        print ("Partidas ganadas:\t"+str(datos[jugador].ganadas))
        print ("Partidas perdidas:\t"+str(int(datos[jugador].partidas)-int(datos[jugador].ganadas)))
        print("Maxima puntuacion:\t"+str(datos[jugador].puntuacion))

    if (sele=="3"):
        #reestablecer en 0 las estadisticas
        p1=datos[jugador]
        p1.partidas=0
        p1.ganadas=0
        p1.puntuacion=0
        datos[jugador]=p1
        print("Tus datos se han restablecido a 0")
    if(sele=="4" or sele=="salir"):
        print("Adios "+jugador+" espero tenerte pronto por aqui de nuevo")
        break
    

