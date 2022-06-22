
class Nodo:
    def __init__(self, etiqueta, dirigido=False):  # Constructor de la clase
        self.__etiqueta = etiqueta  # identificador del nodo
        self.__dirigido = dirigido  # parametro dirigido se usa para saber si el grafo es dirigido
        self.__aristas = set()  
        
# Sobrescritura del metodo str
    def __str__(self):  
        cadena_retorno = ""
        for arista in self.__aristas:
            cadena_retorno += str(arista)

        return cadena_retorno

# Regresa una arista especifica en el nodo
    def get_aristas(self):  
        return self.__aristas

#Regresa la etiqueta que identifica al nodo
    def get_etiqueta(self):  
        return self.__etiqueta

# Obtiene el valor de las aristas salientes, si el grafo es dirigido regresa las aristas que salen del nodo
    def get_aristas_salientes(self):
        if not self.__dirigido:
            return self.__aristas

        aristas_salientes = []
        for arista in self.__aristas:
            if arista.get_nodo_fuente() == self:
                aristas_salientes.append(arista)

        return aristas_salientes

# Obtiene el valor de las aristas entrantes, si el grafo es dirigido regresa las aristas que entran al nodo
    def get_aristas_entrantes(self):
        if not self.__dirigido:
            return self.__aristas

        aristas_entrantes = []
        for arista in self.__aristas:
            if arista.get_nodo_destino() == self:
                aristas_entrantes.append(arista)

        return aristas_entrantes

# Metodo para agregar una arista
    def add_arista(self, arista):
        self.__aristas.add(arista)  # se agrega una arista al conjunto que guarda las aristas del nodo

    def remove_arista(self, arista):
        if arista in self.__aristas:  # si se encuentra la arista en el nodo se remueve la arista
            self.__aristas.remove(arista)  # se remueve una arista del set que guarda las aristas
        else:  # si no se encuentra la arista en el nodo lanza el sigueinte error
            raise ValueError(
                "No se pudo encontrar la arista {0} en el  nodo {1}".format(str(arista), str(self)))

 # Método para obtener todas las aristas
    def set_aristas(self, aristas): 
        self.__aristas = aristas
        
    def __str__(self):
        return self.__etiqueta