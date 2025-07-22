import mysql.connector
from mysql.connector import Error
import os

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("Oprima cualquier tecla para continuar...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a la BD: {e}")
        return None

def menu_principal():
    print("Sistema de Gestión de Contactos :::...\n1. Agregar\n2. Mostrar\n3. Buscar\n4. Modificar\n5. Eliminar\n6. SALIR")
    opcion = input("Elige una opción (1-6): ")
    return opcion

def agregar_contacto():
    borrarPantalla()
    conexion = conectar()
    if conexion != None:
        print("Agregar Contacto")
        nombre = input("Nombre: ").upper().strip()
        telefono = input("Teléfono: ").strip()
        correo = input("Correo: ").strip().lower()
        domicilio = input("Domicilio: ").upper().strip()
        cursor = conexion.cursor()
        sql = "INSERT INTO contactos (nombre, telefono, correo, domicilio) VALUES (%s, %s, %s, %s)"
        val = (nombre, telefono, correo, domicilio)
        cursor.execute(sql, val)
        conexion.commit()
        print("::: Acción realizada con éxito :::")

def mostrar_contactos():
    borrarPantalla()
    conexion = conectar()
    if conexion != None:
        cursor = conexion.cursor()
        sql = "SELECT * FROM contactos"
        cursor.execute(sql)
        registros = cursor.fetchall()
        if registros:
            print(f"{'Nombre':<20}{'Teléfono':<15}{'Correo':<30}{'Domicilio':<30}")
            print("-" * 95)
            for fila in registros:
                print(f"{fila[1]:<20}{fila[2]:<15}{fila[3]:<30}{fila[4]:<30}")
            print("-" * 95)
            print(f"Total de contactos: {len(registros)}")
        else:
            print("No hay contactos en la agenda")

def buscar_contacto():
    borrarPantalla()
    conexion = conectar()
    if conexion != None:
        nombre = input("Nombre del contacto a buscar: ").upper().strip()
        cursor = conexion.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registro = cursor.fetchone()
        if registro:
            print(f"\nNombre: {registro[1]}")
            print(f"Teléfono: {registro[2]}")
            print(f"Correo: {registro[3]}")
            print(f"Domicilio: {registro[4]}")
        else:
            print(f"No se encontró el contacto '{nombre}'")

def modificar_contacto():
    borrarPantalla()
    conexion = conectar()
    if conexion != None:
        nombre = input("Nombre del contacto a modificar: ").upper().strip()
        cursor = conexion.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registro = cursor.fetchone()
        if registro:
            print(f"\nNombre: {registro[1]}")
            print(f"Teléfono: {registro[2]}")
            print(f"Correo: {registro[3]}")
            print(f"Domicilio: {registro[4]}")
            resp = input("¿Deseas modificar este contacto? (Sí/No): ").lower()
            if resp == "si":
                nuevo_tel = input("Nuevo Teléfono: ").strip()
                nuevo_correo = input("Nuevo Correo: ").strip().lower()
                nuevo_dom = input("Nuevo Domicilio: ").strip().upper()
                sql = "UPDATE contactos SET telefono = %s, correo = %s, domicilio = %s WHERE nombre = %s"
                val = (nuevo_tel, nuevo_correo, nuevo_dom, nombre)
                cursor.execute(sql, val)
                conexion.commit()
                print("::: Acción realizada con éxito :::")
        else:
            print(f"No se encontró el contacto '{nombre}'")

def eliminar_contacto():
    borrarPantalla()
    conexion = conectar()
    if conexion != None:
        nombre = input("Nombre del contacto a eliminar: ").upper().strip()
        cursor = conexion.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registro = cursor.fetchone()
        if registro:
            print(f"\nNombre: {registro[1]}")
            print(f"Teléfono: {registro[2]}")
            print(f"Correo: {registro[3]}")
            print(f"Domicilio: {registro[4]}")
            resp = input("¿Deseas eliminar este contacto? (Sí/No): ").lower()
            if resp == "si":
                sql = "DELETE FROM contactos WHERE nombre = %s"
                val = (nombre,)
                cursor.execute(sql, val)
                conexion.commit()
                print("::: Acción realizada con éxito :::")
        else:
            print(f"No se encontró el contacto '{nombre}'")