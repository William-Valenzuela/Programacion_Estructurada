import os
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

limpiar_pantalla()
a = 10
b = 5

print(a > b)      # True
print(a == b)     # False
print(a != b)     # True

print((a > b) and (b > 2))   # True
print((a < b) or (b > 2))    # True
print(not (a > b))          # False