"""Crear un programa que calcule e imprima la tabla de multiplicar del 2
restricciones:
1.-Sin estructuras de control
2.-Sin funciones

"""
#Version 1

n = int(input("Ingresa el número para mostrar su tabla de multiplicar: "))

num=int(input("Inserta el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num} x 1 = {multi}")
multi=num*2
num=int(input("Inserta el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num} x 2 = {multi}")
multi=num*2
num=int(input("Inserta el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num} x 3 = {multi}")
multi=num*3
num=int(input("Inserta el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num} x 4 = {multi}")
multi=num*4
num=int(input("Inserta el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num} x 5 = {multi}")
multi=num*5
num=int(input("Inserta el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num} x 6 = {multi}")
multi=num*6
num=int(input("Inserta el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num} x 7 = {multi}")
multi=num*7
num=int(input("Inserta el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num} x 8 = {multi}")
multi=num*8
num=int(input("Inserta el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num} x 9 = {multi}")
multi=num*9
num=int(input("Inserta el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num} x 10 = {multi}")
multi=num*10

#Version 2
"""Crear un programa que calcule e imprima cualquier tabla de multiplicar
Restricciones
1.-Con estrucyuras de control
2.-Sin funciones

"""

n = int(input("Ingresa el número para mostrar su tabla de multiplicar: "))

# Usamos un ciclo for del 1 al 10
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


#Version 3
"""Crear un programa que calcule e imprima cualquier tabla de multiplicar
Restricciones
1.-Con estructuras de control
2.-Con funciones
"""
 
def obterner_tabla(n):
    tabla=[]
    for i in range(1,11):
        tabla.append(n*i)
    return tabla
 
tabla=obterner_tabla(n)
for i in range(len(tabla)):
    print(tabla[i])

    def tabla (numero):
        num=numero
        respuest=""
        for i in range(1,11):
            multi=num*respuesta