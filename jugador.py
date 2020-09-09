class Jugador:
    """ La Clase Jugador contiene los elementos principales
        del jugador"""
    def __init__(self, nombre):
        """ Su constructor se inicializa con nombre y puntuacion
        """
        self._nombre = nombre
        self._puntuacion = 0
    
    # Getter de nombre
    def get_nombre(self):
        return self._nombre
    
    # Getter y Setter de puntuación
    def get_puntuacion(self):
        return self._puntuacion
    
    def set_puntuacion(self, puntuacion):
        self._puntuacion = puntuacion
    
    # Método Str
    def __str__(self):
        return self._nombre + " - " + str(self._puntuacion) + " puntos."