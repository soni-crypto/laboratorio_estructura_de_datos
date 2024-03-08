from collections import deque

def es_palindromo(palabra):
    # Convertir la palabra a minúsculas para hacer la comparación insensible a mayúsculas
    palabra = palabra.lower()

    # Crear una cola para los caracteres de la palabra en orden original
    cola_original = deque(palabra)

    # Crear una cola para los caracteres de la palabra en orden reverso
    cola_reverso = deque(reversed(palabra))

    # Comparar los caracteres de ambas colas
    while len(cola_original) > 0 and len(cola_reverso) > 0:
        if cola_original.popleft() != cola_reverso.popleft():
            return False

    # Si ambas colas están vacías, la palabra es un palíndromo
    return len(cola_original) == len(cola_reverso) == 0

# Ejemplo de uso
palabra_ejemplo = "reconocer"
resultado = es_palindromo(palabra_ejemplo)

if resultado:
    print(f"{palabra_ejemplo} es un palíndromo.")
else:
    print(f"{palabra_ejemplo} no es un palíndromo.")
