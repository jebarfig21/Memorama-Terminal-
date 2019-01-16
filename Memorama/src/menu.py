from jugador import Jugador
#funcion que llama al menu para meter usuario

def menu(opcion,datos):#recibe como parametros la opcion deseada y el archivo donde vienen las llaves
    
    if opcion == "1":
        jugador= input("Dame el usuario\n")
        while(jugador in datos):#Siempre que ya este el juegador inscrito te pedira que ingreses otro
            print ("El username ya existe, por favor intenta con otro:\n")
            jugador = input("Dame el usuario\n")

        contrasena = input("Dame la clave\n")
        confirmacion = input("Repite la clave\n")

        while(contrasena!=confirmacion):

            print("Lo siento pero la contraseña y la cofirmacion no son iguales, intenta de nuevo\n")

            contrasena = input("Dame la clave\n")
            confirmacion = input("Repite la clave\n")
    
        puntuacion = 0
        partidas = 0
        ganadas = 0
        p1 = Jugador(jugador,contrasena,confirmacion,puntuacion,partidas,ganadas)
        llave = p1.getUsuario()    
        datos[llave] = p1
        
        print ('Usuario agregado con exito\n\n'+u"\U0001F60A")

        return p1.getUsuario()
      
    elif(opcion == "2"):#opcion para hacer login

        jugador = input("Dame el usuario\n")

        while(jugador not in datos):

            print("Revisa el usuario")
            jugador=input("Dame de nuevo el usuario, revisalo por favor:\n")

        clave=input("Dame la clave\n")

        while(clave!=datos[jugador].getContrasena()):

            print("Revisa la contraseña")
            clave=input("Dame la clave de nuevo, revisala bien")


        print("Bienvenido :"+jugador+"\n")#El jugador es bienvenido
        
        p1=datos[jugador]
        
        return p1.getUsuario()

    return jugador
