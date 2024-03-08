# from nodo import Nodo
class Nodo:
    def __init__(self, dato):
        # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
    
    # Funciones agregadas
    def contar_nodos(self, nodo):
        if nodo is None:
            return 0
        else:
            return 1 + self.contar_nodos(nodo.izquierda) + self.contar_nodos(nodo.derecha)

    def contar_nodos_hoja(self, nodo):
        if nodo is None:
            return 0
        elif nodo.izquierda is None and nodo.derecha is None:
            return 1
        else:
            return self.contar_nodos_hoja(nodo.izquierda) + self.contar_nodos_hoja(nodo.derecha)
    
    def contar_nodos_internos(self, nodo):
        if nodo is None or (nodo.izquierda is None and nodo.derecha is None):
            return 0
        else:
            return 1 + self.contar_nodos_internos(nodo.izquierda) + self.contar_nodos_internos(nodo.derecha)

    def calcular_altura(self, nodo):
        if nodo is None:
            return 0
        else:
            altura_izquierda = self.calcular_altura(nodo.izquierda)
            altura_derecha = self.calcular_altura(nodo.derecha)
            return 1 + max(altura_izquierda, altura_derecha)

    def calcular_profundidad(self, nodo, dato):
        return self._calcular_profundidad_recursivo(self.raiz, dato, 0)

    def _calcular_profundidad_recursivo(self, nodo, dato, nivel):
        if nodo is None:
            return -1  # Valor indicando que el nodo no fue encontrado
        if nodo.dato == dato:
            return nivel
        elif dato < nodo.dato:
            return self._calcular_profundidad_recursivo(nodo.izquierda, dato, nivel + 1)
        else:
            return self._calcular_profundidad_recursivo(nodo.derecha, dato, nivel + 1)

    def encontrar_minimo(self, nodo=None):
        nodo_actual = nodo if nodo is not None else self.raiz

        while nodo_actual is not None and nodo_actual.izquierda is not None:
            nodo_actual = nodo_actual.izquierda

        return nodo_actual

    def encontrar_maximo(self, nodo=None):
        nodo_actual = nodo if nodo is not None else self.raiz

        while nodo_actual is not None and nodo_actual.derecha is not None:
            nodo_actual = nodo_actual.derecha

        return nodo_actual


    

