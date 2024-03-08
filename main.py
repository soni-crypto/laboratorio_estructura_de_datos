from arbol import Arbol

arbol = Arbol("Luis")
arbol.agregar("María José")
arbol.agregar("Maggie")
arbol.agregar("Leon")
arbol.agregar("Cuphead")
arbol.agregar("Aloy")
arbol.agregar("Jack")
# nombre = input("Ingresa algo para agregar al árbol: ")
# arbol.agregar(nombre)
# arbol.preorden()
# arbol.inorden()
# arbol.postorden()
# Búsqueda
# busqueda = input("Busca algo en el árbol: ")
# nodo = arbol.buscar(busqueda)
# if nodo is None:
#     print(f"{busqueda} no existe")
# else:
#     print(f"{busqueda} sí existe")
#     # Aquí tienes en "nodo" toda la información del nodo. Tanto su izquierda, derecha, dato y otros atributos que le hayas agregado



arbol_numeros = Arbol(5)
arbol_numeros.agregar(1984)
arbol_numeros.agregar(60)
arbol_numeros.agregar(10)
arbol_numeros.agregar(20)
arbol_numeros.agregar(10)
arbol_numeros.agregar(25)
arbol_numeros.agregar(59)
arbol_numeros.agregar(64)
arbol_numeros.agregar(10)
arbol_numeros.agregar(19)
arbol_numeros.agregar(23)
arbol_numeros.agregar(18)
arbol_numeros.agregar(1)
arbol_numeros.agregar(2013)
# arbol_numeros.preorden()
# arbol_numeros.inorden()
# arbol_numeros.postorden()

# busqueda = int(input("Ingresa un número para buscar en el árbol: "))
# n = arbol_numeros.buscar(busqueda)
# if n is None:
#     print(f"{busqueda} no existe")
# else:
#     print(f"{busqueda} sí existe")




# # Funciones agregadas
cantidad_nodos = arbol.contar_nodos(arbol.raiz)
print(f"La cantidad de nodos en el árbol es: {cantidad_nodos}")

cantidad_nodos_hoja = arbol.contar_nodos_hoja(arbol.raiz)
print(f"La cantidad de nodos hoja en el árbol es: {cantidad_nodos_hoja}")

cantidad_nodos_internos = arbol.contar_nodos_internos(arbol.raiz)
print(f"La cantidad de nodos internos en el árbol es: {cantidad_nodos_internos}")

altura_arbol = arbol.calcular_altura(arbol.raiz)
print(f"La altura del árbol es: {altura_arbol}")

dato_a_buscar = "Maggie"
profundidad_nodo = arbol.calcular_profundidad(arbol.raiz, dato_a_buscar)
if profundidad_nodo != -1:
    print(f"La profundidad del nodo con dato {dato_a_buscar} es: {profundidad_nodo}")
else:
    print(f"No se encontró un nodo con dato {dato_a_buscar} en el árbol.")

nodo_minimo = arbol_numeros.encontrar_minimo()
print(f"El nodo con el valor mínimo es: {nodo_minimo.dato}")

nodo_maximo = arbol_numeros.encontrar_maximo()
print(f"El nodo con el valor máximo es: {nodo_maximo.dato}")
