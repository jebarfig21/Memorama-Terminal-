#Archivo que maneja funciones para crear y alterar el tablero de juego
import random

#Funcion que crea un tablero sobr el cual se va jugar

def creaTablero():
    juego = [u'\u2603',u"\U0001F4A9",u'\u2602',u'\u262F',u'\u2660',u'\u260E',u'\u2744',u'\u26BD']
    juego = juego+juego
    random.shuffle(juego)

    return juego


#Funcion que dibujo un tablero con numeros

def visualizaTablero():
    tablero = ""
    for i in range(1,17):
        tablero = tablero+str(i)+"\t"
          
    return tablero


#Funcion que va mostrando las figuras seleccionadas en el input

def sobreescribeTablero(elem1,elem2,num1,num2,tablero):
    tablero = tablero.split("\t")
    tablero[num1-1] = elem1
    tablero[num2-1] = elem2
    cadena = ""
    for elem in tablero:
    
        if(type(elem)=='unicode'):
            cadena = cadena+unicode(elem)+"\t"
            
        else:
            cadena = cadena+str(elem)+"\t"
        
    return cadena


#Funcion que le añade los saltos de linea y la forma al tablero.

def creaSaltos(tablero):
    cadena = ""
    tablero = tablero.split("\t")
    for i in range(len(tablero)-1):
        if(i==0):
            cadena = "--------|---------------|---------------|---------------|"+"\n"
        cadena = cadena+tablero[i]+"\t"+"|"+"\t"
    
        if(i%4==3):
            cadena = cadena+"\n"+"--------|---------------|---------------|---------------|"+"\n"

    return cadena

