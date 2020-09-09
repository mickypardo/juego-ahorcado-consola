from jugador import Jugador

class Adivinador(Jugador):
    """ La Clase Adivinador es una clase hija
        de Jugador, recibe sus atributos,
        y además contiene el atributo intentos
    """
    def __init__(self, nombre):
        """ El constructor inicializa intentos
        """
        super().__init__(nombre)
        self._intentos = 0
        self._logrado = False
    
    # Métodos Getter y Setter de intentos
    def set_intentos(self):
        self._intentos += 1
        
    def get_intentos(self):
        return self._intentos
    
    def set_logrado(self, logrado):
        self.logrado = logrado
    
    def get_logrado(self):
        return self.logrado
    ## Comportamientos Adivinador
    # Método que formula letras
    def formular_letra(self):
        letra = input().upper()
        return letra
