


#type error
print("=== Suma texto + número ===")
texto = input("Ingresa un texto: ")
try:
    numero = int(input("Ingresa un número: "))
    resultado = texto + numero
    print("Resultado:", resultado)
except TypeError:
    print("No puedes sumar texto y número directamente.")
    print(f"Tal vez quisiste hacer: '{texto}' + str({numero})")
    print("Resultado corregido:", texto + str(numero))


#ValueError

print("=== Conversor de texto a número ===")
texto = input("Ingresa algo que debería ser un número: ")
try:
    numero = int(texto)
    print(f"Convertido correctamente: {numero}")
except ValueError:
    print("No se puede convertir ese texto a número.")




#IndexError
print("=== Consulta de posición en la lista ===")
lista = ["manzana", "banana", "cereza"]
print("Lista:", lista)
try:
    index = int(input("¿Qué posición quieres ver? (0, 1, 2, etc.): "))
    print(f"Elemento en posición {index}: {lista[index]}")
except IndexError:
    print("Ese índice no existe en la lista.")
except ValueError:
    print("Debes ingresar un número.")

#KeyError

print("=== Consulta de claves en diccionario ===")
d = {"nombre": "Ana", "edad": 25}
print("Diccionario:", d)
clave = input("¿Qué clave quieres consultar?: ")
try:
    print(f"Valor: {d[clave]}")
except KeyError:
    print("Esa clave no existe en el diccionario.")