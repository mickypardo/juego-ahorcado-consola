## Aqui se definen las constantes

# Colores
COLOR_AVISO = "\x1b[1;33m"
COLOR_BLANCO = "\x1b[0;37m"

# Limites juego
LIMITE_JUEGO_NORMAL = 14
LIMITE_JUEGO_DIFICIL = 7

# Se define los elementos usados para la horca
HORCA = ("╩", "║", "╔", "═", "╗", "O", "|", "/", "\\"," ")
# Fases de fallos que dibujará la horca
FASES_FALLO = (
        (HORCA[0], 4, 0),
        (HORCA[1], 3, 0),
        (HORCA[1], 2, 0),
        (HORCA[1], 1, 0),
        (HORCA[2], 0, 0),
        (HORCA[3], 0, 1),
        (HORCA[3], 0, 2),
        (HORCA[4], 0, 3),
        (HORCA[5], 1, 3),
        (HORCA[6], 2, 3),
        (HORCA[7], 2, 2),
        (HORCA[8], 2, 4),
        (HORCA[7], 3, 2),
        (HORCA[8], 3, 4)
    )
# Se prepara un array bidimensional para albergar la horca entera
HORCA_ORIGINAL = (
    (HORCA[2], HORCA[3], HORCA[3], HORCA[4], HORCA[-1]), 
    (HORCA[1], HORCA[-1], HORCA[-1], HORCA[5], HORCA[-1]),
    (HORCA[1], HORCA[-1], HORCA[7], HORCA[6], HORCA[8]),
    (HORCA[1], HORCA[-1], HORCA[7], HORCA[-1], HORCA[8]),
    (HORCA[0], HORCA[-1], HORCA[-1], HORCA[-1], HORCA[-1])
)

HORCA_VACIA = [
    [HORCA[-1], HORCA[-1], HORCA[-1], HORCA[-1], HORCA[-1]],
    [HORCA[-1], HORCA[-1], HORCA[-1], HORCA[-1], HORCA[-1]],
    [HORCA[-1], HORCA[-1], HORCA[-1], HORCA[-1], HORCA[-1]],
    [HORCA[-1], HORCA[-1], HORCA[-1], HORCA[-1], HORCA[-1]],
    [HORCA[-1], HORCA[-1], HORCA[-1], HORCA[-1], HORCA[-1]]
]

TABLA_PUNTOS_NORMAL = {
    0: 1500, 
    1: 1000, 
    2: 720,
    3: 640,
    4: 460,
    5: 370,
    6: 290,
    7: 220,
    8: 160,
    9: 110,
    10: 70,
    11: 40,
    12: 20,
    13: 10
}

TABLA_PUNTOS_DIFICIL = {
    0: 3000, 
    1: 2000, 
    2: 1250,
    3: 900,
    4: 750,
    5: 430,
    6: 340    
}