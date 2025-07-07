def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t... Oprima cualquier tecla para continuar...")

def menu_principal():
    print("\n\t..::::: 📇 Sistema de Gestión de Agenda de Contactos 📇 :::::...\n")
    print("\t\t1️⃣ --➕ Agregar Contacto")
    print("\t\t2️⃣ --📋 Mostrar Todos los Contactos")
    print("\t\t3️⃣ --🔍 Buscar Contactos por Nombre")
    print("\t\t4️⃣ --🗑️ Eliminar Contacto")
    print("\t\t5️⃣ --✏️ Modificar Contacto")
    print("\t\t6️⃣ --❌ Salir")
    opcion = input("\n\t\t🔹 Elige una opción (1-6): ").upper()
    return opcion

def agregar_contacto(lista):
    borrarPantalla()
    print("\n\t.:: ➕ Agregar Contacto ::.\n")
    nombre = input("Nombre del contacto: ").strip().title()
    telefono = input("Número de teléfono: ").strip()
    correo = input("Correo electrónico: ").strip()
    domicilio = input("Domicilio: ").strip().title()

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo,
        "domicilio": domicilio
    }
    lista.append(contacto)
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")


def buscar_nombre(lista):
    borrarPantalla()
    print("\n\t.:: 🔍 Buscar Contacto por Nombre ::.\n")
    nombre_buscado = input("Ingresa el nombre a buscar: ").strip().title()
    encontrados = [c for c in lista if c["nombre"] == nombre_buscado]
    if encontrados:
        for contacto in encontrados:
            print(f"\n\t📇 {contacto['nombre']} - 📞 {contacto['telefono']}")
    else:
        print("\n\t❗ No se encontró ningún contacto con ese nombre.")

def eliminar_contacto(lista):
    borrarPantalla()
    print("\n\t.:: 🗑️ Eliminar Contacto ::.\n")
    nombre = input("Ingresa el nombre del contacto a eliminar: ").strip().title()
    eliminado = False
    for contacto in lista[:]:
        if contacto["nombre"] == nombre:
            lista.remove(contacto)
            eliminado = True
    if eliminado:
        print("\n\t\t::: ¡Contacto eliminado exitosamente! :::")
    else:
        print("\n\t❗ No se encontró el contacto.")


def mostrar_contacto(lista):
    borrarPantalla()
    print("\n\t.:: 📋 Lista de Contactos ::.\n")
    if not lista:
        print("\tNo hay contactos registrados.")
    else:
        for i, contacto in enumerate(lista, 1):
            print(f"\n\t{i}. 📇 Nombre: {contacto['nombre']}")
            print(f"\t   📞 Teléfono: {contacto['telefono']}")
            print(f"\t   📧 Correo: {contacto['correo']}")
            print(f"\t   🏠 Domicilio: {contacto['domicilio']}")


def modificar_contacto(lista):
    borrarPantalla()
    print("\n\t.:: ✏️ Modificar Contacto ::.\n")
    nombre = input("Ingresa el nombre del contacto que deseas modificar: ").strip().title()
    for contacto in lista:
        if contacto["nombre"] == nombre:
            print(f"\n\t📇 Contacto encontrado:")
            print(f"\t   Nombre actual: {contacto['nombre']}")
            print(f"\t   Teléfono actual: {contacto['telefono']}")
            print(f"\t   Correo actual: {contacto['correo']}")
            print(f"\t   Domicilio actual: {contacto['domicilio']}")
            nuevo_nombre = input("\nNuevo nombre (deja vacío para mantener el actual): ").strip().title()
            nuevo_telefono = input("Nuevo teléfono (deja vacío para mantener el actual): ").strip()
            nuevo_correo = input("Nuevo correo electrónico (deja vacío para mantener el actual): ").strip()
            nuevo_domicilio = input("Nuevo domicilio (deja vacío para mantener el actual): ").strip().title()
            if nuevo_nombre:
                contacto["nombre"] = nuevo_nombre
            if nuevo_telefono:
                contacto["telefono"] = nuevo_telefono
            if nuevo_correo:
                contacto["correo"] = nuevo_correo
            if nuevo_domicilio:
                contacto["domicilio"] = nuevo_domicilio
            print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
            return
    print("\n\t❗ No se encontró el contacto con ese nombre.")

