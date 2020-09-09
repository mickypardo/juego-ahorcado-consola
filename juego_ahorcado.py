from constantes import *
from textos_predefinidos import *
from motor_juego import carga_motor_juego
from random import randint
from adivinador import Adivinador
from creador import Creador

def main():
    # Inicializamos listas que contienen los nombre de los jugadores,
    # y sus correspondientes puntuaciones totales.
    nombres_jugadores = []
    puntuaciones_totales = []
    ranking = [nombres_jugadores, puntuaciones_totales]
    
    # Cargamos cabecera del juego y menu de opciones
    cabecera_juego()    
    opcion = menu_juego()
    if opcion == 1:
        # Comienza la partida
        system("clear")
        nombre_j1 = input("Jugador 1. Escriba su nombre: ")
        system("clear")
        nombre_j2 = input("Jugador 2. Escriba su nombre: ")
        
        # Elección aleatoria de quien será Creador 
        # y quien el Adivinador
        tipo_jugador_int = randint(0, 1)
        if tipo_jugador_int == 0:   # 0 -> Adivinador
            jugador1 = Adivinador(nombre_j1)
            jugador2 = Creador(nombre_j2)
        else:                       # 1 -> Creador
            jugador1 = Creador(nombre_j1)
            jugador2 = Adivinador(nombre_j2)
        
        # Asignamos el objeto jugador1 o jugador2 a adivinador    
        # Asignamos el objeto jugador1 o jugador2 a creador
        if type(jugador1) == Adivinador and type(jugador2) == Creador:
            adivinador = jugador1
            creador = jugador2
        else:
            adivinador = jugador2
            creador = jugador1
        
        textos_tipo_jugador(adivinador, creador)
        textos_tapar_ojos(adivinador, creador)                
        textos_creacion_palabra(adivinador, creador)
        
        carga_motor_juego(adivinador, creador)
        if adivinador.get_logrado():
            print(
                COLOR_AVISO + 
                "¡HAS GANADO!" +
                COLOR_BLANCO
            )
            adivinador.set_puntuacion(
                adivinador.get_puntuacion() +
                TABLA_PUNTOS_NORMAL[adivinador.get_intentos()]
            )
        else:
            print(
                COLOR_AVISO +
                "¡HAS PERDIDO!" +
                COLOR_BLANCO
            )
        print(
            COLOR_AVISO +
            adivinador.get_nombre() +
            COLOR_BLANCO +
            " ha obtenido " +
            str(adivinador.get_puntuacion()) +
            " puntos."
        )
    elif opcion == 2:
        # Puntuaciones
        pass
    elif opcion == 3:
        # Reglas de juego
        pass
    else:
        # Salir    
        pass

if __name__ == "__main__":
    main()
