from os import system
from constantes import *
from textos_predefinidos import *

def carga_motor_juego(adivinador, creador):
    # Defino una lista vacia de letras,
    # al que dotaremos de una longitud similar
    # a la palabra del creador,
    # que rellenaremos con letras acertadas
    palabra_enigma = []
    palabra_letras = creador.trocear_palabra()    

    for i in range(len(palabra_letras)):
        palabra_enigma.append("_")

    # Inicializa el contenedor de la figura de la horca
    horca_juego = HORCA_VACIA
    limite_intentos = LIMITE_JUEGO_NORMAL
    while True:
        
        system("clear")
        print("================================")
        print("== INTENTE ACERTAR LA PALABRA ==")
        print("================================")
                
        visualiza_horca(horca_juego)
        visualiza_palabra_enigma(palabra_enigma)
        
        if palabra_letras == palabra_enigma:
            #completada
            adivinador.set_logrado(True)
            break
        
        if adivinador.get_intentos() == limite_intentos:
            #ahorcado
            adivinador.set_logrado(False)
            break
            
        print()
        print("Proporcione una letra: ", end="")
        letra = adivinador.formular_letra()
            
        indices_letras_iguales = []
        i = 0
        for i in range(len(palabra_letras)):
            if palabra_letras[i] == letra:
                indices_letras_iguales.append(i)
        
        if indices_letras_iguales:
            i = 0
            for i in indices_letras_iguales:
                palabra_enigma[i] = letra
        else:
            adivinador.set_intentos()
            lista_fallo = list(pinta_horca(adivinador.get_intentos()))
            figura_ = lista_fallo[0]
            fila_ = lista_fallo[1]
            columna_ = lista_fallo[2]
            horca_juego[fila_][columna_] = figura_
            
        
