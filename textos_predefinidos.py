from os import system
from constantes import *
import time

def cabecera_juego():
    system("clear")
    print("============================================================================")
    print("                              EL AHORCADO                                   ")
    print("                              -----------                                   ")
    print(" El juego del ahorcado es un juego entretenido en el que hay dos jugadores. ")
    print(" Un jugador propone que se adivine un palabra, y el otro ha de adivinarla.  ")
    print(" Al final ganará aquel jugador que obtenga más puntos.                      ")
    print("============================================================================")
    
def reglas_juego():
    system("clear")
    print("============================================================================")
    print("                            REGLAS DE JUEGO                                 ")
    print("                            ---------------                                 ")
    print(" - El juego comienza definiendo el nombre de los jugadores a participar.    ")
    print(" - De manera aleatoria se escogerá entre dos roles (DIRECTOR O ADIVINADOR). ")
    print(" - El DIRECTOR propone una palabra a adivinar.                              ")
    print(" - El ADIVINADOR deberá proponer letras que crea que están en la palabra.   ")
    print(" - Por cada fallo, El sistema dibujara una horca, finalizando en una figura.")
    print(" - Cuando se acierte la palabra, se ganará los puntos correspondiente,      ")
    print(" - según los fallos cometidos.")
    print(" - Al final se intercambiarán los roles.")
    
def menu_juego():
    """Función que presenta varias opciones del menu principal, y que retorna una opción"""
    while True:
        system("clear")
        print("\t=======================")
        print("           MENU PRINCIPAL         ")
        print("           --------------         ")
        print("\t1)...... Comenzar juego")
        print("\t2)...... Puntuaciones")
        print("\t3)...... Reglas de juego")
        print("\t-----------------------")
        print("\t0)...... Salir")
        print("\t=======================")
    
        try:
            opcion = int(input("\tEscoja una opción: "))
            if opcion < 0 or opcion > 3:
                error_rango()
            else:
                return opcion            
        except Exception:
            error_dato()

def textos_creacion_palabra(adivinador, creador):
    while True:
        system("clear")
        print(
            COLOR_AVISO +
            creador.get_nombre() + 
            COLOR_BLANCO +
            ", formule la palabra que " + 
            COLOR_AVISO +
            adivinador.get_nombre() + 
            COLOR_BLANCO +
            " debe adivinar: ", end="")
        creador.crear_palabra(input().upper())
        print("La palabra es " + creador.ver_palabra() + ". ¿Estás de acuerdo?(S/N)", end="")
        ok_palabra = input().upper()
        if ok_palabra == "S":
            print(
                COLOR_AVISO +
                creador.get_nombre() + 
                COLOR_BLANCO +
                " puede decirle a " + 
                COLOR_AVISO +
                adivinador.get_nombre() + 
                COLOR_BLANCO +
                " que ya puede mirar.")
            input("PULSE CUALQUIER TECLA PARA CONTINUAR")
            break

def textos_tipo_jugador(adivinador, creador):
    system("clear")    
    print(
        COLOR_AVISO +
        adivinador.get_nombre() + 
        COLOR_BLANCO +
        ", será quien que adivinar la palabra y " + 
        COLOR_AVISO +
        "\n" + creador.get_nombre() + 
        COLOR_BLANCO +
        " será quien cree la palabra")
    input("PULSE CUALQUIER TECLA PARA CONTINUAR")
        
def textos_tapar_ojos(adivinador, creador):
    system("clear")
    print(
        COLOR_AVISO +
        adivinador.get_nombre() + 
        COLOR_BLANCO +
        ", tápese los ojos o dese la vuelta hasta que le avisen.")
    input("PULSE CUALQUIER TECLA PARA CONTINUAR")


def pinta_horca(intento):
    return FASES_FALLO[intento-1]

def visualiza_horca(figura_horca):
    for fila in figura_horca:
        print()
        for elemento in fila:
            print(elemento, end="")
    print()

def visualiza_palabra_enigma(palabra_enigma):
    for elemento in palabra_enigma:
        print(elemento, end="  ")
    print()

def error_dato():
    print(COLOR_AVISO + "Tipo de dato incorrecto. Elija nuevamente.")
    print(COLOR_BLANCO)
    time.sleep(1)
    
def error_rango():
    print(COLOR_AVISO + "Fuera de rango. Elija nuevamente.")
    print(COLOR_BLANCO)
    time.sleep(1)
