import os
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

limpiar_pantalla()
print("=== Consulta de claves en diccionario ===")
d = {"nombre": "Ana", "edad": 25}
print("Diccionario:", d)
clave = input("¿Qué clave quieres consultar?: ")
try:
    print(f"Valor: {d[clave]}")
except KeyError:
    print("Esa clave no existe en el diccionario.")
