from Model.jugador import Jugador
import shelve
from View.menu import menu
from View.tablero import *

#Funcion que ejecuta el juego memorama, usa las funciones de tablero apra crear tablero y modificarlo conforme avanza el juego
def juego(p1):

    print("Muy bien, hora de jugar\nDiviertete\n "+u"\U0001F60A"+"\t"+u"\U0001F60A"+"\t"+u"\U0001F60A"+"\t"+u"\U0001F60A"+"\t"+u"\U0001F60A"+"\t"+u"\U0001F60A"+"\t"+u"\U0001F60A"+"\t"+u"\U0001F60A")

    numeros = creaTablero()#Se crea un nuevo tablero
    ver = ""
    nuevaTabla = visualizaTablero()
    error = 0
    puntuacion = 0
    print (creaSaltos(visualizaTablero()))#Se imprime el tablero

    while(error<3):
        num1 = 17
        num2 = 17
        salir = ""

        print ("Hora de jugar, escribe salir, para regresar al menu principal")

        while(int(num1)>16 or int(num2)>16):
            #input que recibe los numeros del tablero a revelar
            nums=input("Dame dos numeros:\n")
            if(nums=="salir"):
                salir = "salir"

                break

            nums = nums.split()
            num1 = nums[0]
            num2 = nums[1]
            num1 = num1.strip()
            num2 = num2.strip()

        if(salir=="salir"):

            break
        #Si las figuras son iguales, cambia el tablero y muestra las figuras siempre
        if (numeros[int(num1)-1] is numeros[int(num2)-1]):

            ver = sobreescribeTablero(numeros[int(num1)-1],numeros[int(num2)-1],int(num1),int(num2),nuevaTabla)
            nuevaTabla = ver
            ver = creaSaltos(ver)
            print (ver)
            puntuacion+=100
            print ("Tu puntuacion actual: "+str(puntuacion))
        #Si las figuras de los numeros son diferentes, solo muestra los simbolos y en el siguiente movimento los oculta
        else:

            ver = sobreescribeTablero(numeros[int(num1)-1],numeros[int(num2)-1],int(num1),int(num2),nuevaTabla)
            print (creaSaltos(ver))
            print ("Lo siento, no son iguales llevas: "+str(error+1)+" errores")
            error+=1
        #juega con la puntuacion
        if(puntuacion==800):

            print ("Felicidades has ganado")
            p1.ganadas+=1
            break

        if(puntuacion>300):
            puntuacion = puntuacion-(error * 100)

        if(puntuacion==800 and error==0):
            puntuacion = 1000

    #muestra puntuacion
    print("Tu puntuacion final fue: "+str(puntuacion)+"\n")
    if(p1.puntuacion<puntuacion):
        p1.puntuacion = puntuacion

    p1.partidas+=1

    return p1
