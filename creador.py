from jugador import Jugador

class Creador(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)
        self._palabra = ""
    
    def crear_palabra(self, palabra):
        self._palabra = palabra
    
    def ver_palabra(self):
        return self._palabra
    
    def __str__(self):
        return super().__str__()
    
    def trocear_palabra(self):
        palabra_troceada = []
        for letra in self.ver_palabra():
            palabra_troceada.append(letra)
        return palabra_troceada

