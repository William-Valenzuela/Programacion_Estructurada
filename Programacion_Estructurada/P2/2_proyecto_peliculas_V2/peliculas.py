
#Dict u objeto para almacenar los atributos (Nombre, Categoria, Clasificacion, Genero, Idioma) y sus valores
pelicula={
            "nombre":"",
            "categoria":"",
            "clasificacion":"",
            "genero":"",
            "idioma":""
          }
pelicula={}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t... Oprima cualquier tecla para continuar...")

def crearPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Peliculas ::. \n")
    pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
    #pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip()     OTRA MANERA DE HACERLO MAS SENCILLO
    pelicula.update({"categoría":input("Ingresa la categoría: ").upper().strip()})
    pelicula.update({"clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
    pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
    print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def mostrarPeliculas():
     borrarPantalla()
     print("\n\t.:: Consultar o mostrar la Pelicula ::. \n")
     if len(pelicula)>0:
         for i in pelicula:
             print(f"\t{(i)}: {pelicula[i]}")
     else:
            print("\t .:: No hay peliculas en el sistema ::.")

def borrarPeliculas():
     borrarPantalla()
     print("\n\t.:: Borrar o quitar  las Peliculas ::. \n")
     resp=input("Deseas borrar o quitar todas las peliculas del sitema? (Si/No)").lower().strip()
     if resp =="si":
         pelicula.clear()
         print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def agregarCaracteristicaPeliculas():
     borrarPantalla()
     print("\n\t.:: Agregar caracteristicas a peliculas ::. \n")
     atributo=input("Ingresa la nueva caracteriztica de la pelicula: ").lower().strip()
     valor=input("Ingresa el valor de la caracteriztica de la pelicula: ").upper().strip()
     # pelicula.update({atributo:valor})
     pelicula[atributo]=valor
     print("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")

"""def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar caracteristicas de peliculas ::. \n")
    if len(pelicula) > 0:
        atributo = input("\tIngrese  la caracteristica a modificar: ").lower().strip()
        if atributo in pelicula:
            valor = input("\tIngresa el nuevo valor: ").upper().strip()
            pelicula[atributo] = valor
            print("\n\t\t::: ¡OPERACION EXITOSA! :::")
        else:
            print("\n\t\t::: La caracteristica no fue encontrada :::")
    else:
        print("\t .:: No hay peliculas ::.")"""

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Característica de Películas ::.\n")
    if len(pelicula) > 0:
        for clave in pelicula:
            print(f"\t{clave}: {pelicula[clave]}")

        opcion = input("\n¿Deseas modificar TODAS las características? (s/n): ").lower().strip()

        if opcion == "s":
            pelicula.update({"nombre": input("Ingresa el nombre: ").upper().strip()})
            pelicula.update({"categoria": input("Ingresa la categoría: ").upper().strip()})
            pelicula.update({"clasificacion": input("Ingresa la clasificación: ").upper().strip()})
            pelicula.update({"genero": input("Ingresa el género: ").upper().strip()})
            pelicula.update({"idioma": input("Ingresa el idioma: ").upper().strip()})
            input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
        else:
            atributo = input("\nIngresa el nombre de la característica que deseas modificar: ").lower().strip()
            if atributo in pelicula:
                nuevo_valor = input("Ingresa el nuevo valor: ").upper().strip()
                pelicula[atributo] = nuevo_valor
                print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
            else:
                print("\n\t\t::: La característica no existe :::")
    else:
        print("\t..:: No hay películas en el sistema ::..")
    
    
def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar caracteristicas de peliculas ::. \n")
    if len(pelicula) > 0:
        atributo = input("\tIngresa la caracteristica a eliminar: ").lower().strip()
    if atributo in pelicula:
        del pelicula[atributo]
        print("\n\t\t::: ¡OPERACION EXITOSA! :::")
    else:
        print("\t .:: No hay alguna caracteriztica con dicho nombre ::.")

        import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="",
            password="",
            database="peliculas"
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error que se ha producido: {e}")
    return None

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar características de películas ::.\n")
    if len(pelicula) == 0:
        print("\n\t.:: No hay películas en el sistema ::.")
        input("\n\tPresiona Enter para continuar...")
        return
    opcion = input("\t¿Deseas borrar una característica de la película? (s/n): ").lower().strip()
    if opcion == 's':
        atributo = input("\n\tIngresa la característica a eliminar: ").lower().strip()

        if atributo in pelicula:
            confirmacion = input(f"\n\t¿Estás seguro de que deseas eliminar la característica '{atributo}'? (s/n): ").lower().strip()
            if confirmacion == 's':
                del pelicula[atributo]
                print("\n\t\t::: ¡OPERACIÓN EXITOSA! Característica eliminada. :::")
            else:
                print("\n\t\t::: Operación cancelada por el usuario. :::")
        else:
            print(f"\n\t.:: La característica '{atributo}' no fue encontrada en la película. ::.")
    else:
        print("\n\t.:: Operación cancelada. ::.")
    input("\n\tPresiona Enter para continuar...")



    

    import mysql.connector
import os

# Conexión a la base de datos
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", 
        database="bd_peliculas"
    )

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\tPresiona Enter para continuar...\n")

def crearPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Películas ::.\n")

    nombre = input("Nombre: ").upper().strip()
    categoria = input("Categoría: ").upper().strip()
    clasificacion = input("Clasificación: ").upper().strip()
    genero = input("Género: ").upper().strip()
    idioma = input("Idioma: ").upper().strip()

    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s, %s, %s, %s, %s)"
        datos = (nombre, categoria, clasificacion, genero, idioma)
        cursor.execute(sql, datos)
        conn.commit()
        cursor.close()
        conn.close()
        print("\n✅ Película agregada exitosamente.")
    except Exception as e:
        print("❌ Error al agregar:", e)

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Lista de Películas ::.\n")
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM peliculas")
        resultados = cursor.fetchall()

        if resultados:
            for fila in resultados:
                print(f"\n🎬 ID: {fila[0]}\nNombre: {fila[1]}\nCategoría: {fila[2]}\nClasificación: {fila[3]}\nGénero: {fila[4]}\nIdioma: {fila[5]}")
        else:
            print("\nNo hay películas registradas.")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Error al mostrar:", e)

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar Película por ID ::.\n")
    try:
        id_pelicula = input("Ingrese el ID de la película a eliminar: ")
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM peliculas WHERE id = %s", (id_pelicula,))
        conn.commit()
        if cursor.rowcount > 0:
            print("\n🗑️ Película eliminada con éxito.")
        else:
            print("\n❌ No se encontró ninguna película con ese ID.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Error al eliminar:", e)

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Característica (NO disponible en base de datos fija) ::.\n")
    print("Este sistema usa columnas fijas, no se pueden agregar nuevas características dinámicamente.")
    esperarTecla()

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Película ::.\n")
    try:
        id_pelicula = input("Ingrese el ID de la película a modificar: ")

        nombre = input("Nuevo nombre: ").upper().strip()
        categoria = input("Nueva categoría: ").upper().strip()
        clasificacion = input("Nueva clasificación: ").upper().strip()
        genero = input("Nuevo género: ").upper().strip()
        idioma = input("Nuevo idioma: ").upper().strip()

        conn = conectar()
        cursor = conn.cursor()
        sql = """UPDATE peliculas 
                 SET nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s 
                 WHERE id=%s"""
        datos = (nombre, categoria, clasificacion, genero, idioma, id_pelicula)
        cursor.execute(sql, datos)
        conn.commit()

        if cursor.rowcount > 0:
            print("\n✏️ Película modificada correctamente.")
        else:
            print("\n❌ No se encontró ninguna película con ese ID.")

        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Error al modificar:", e)

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar Característica (NO disponible) ::.\n")
    print("Las columnas de una tabla no pueden borrarse desde Python en este contexto.")
    esperarTecla()