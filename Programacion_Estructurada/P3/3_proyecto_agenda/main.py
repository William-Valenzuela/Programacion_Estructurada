import agenda

def main():
    opcion = True
    while opcion:
        agenda.borrarPantalla()
        opcion = agenda.menu_principal()

        match opcion:
            case "1":
                agenda.agregar_contacto()
                agenda.esperarTecla()
            case "2":
                agenda.mostrar_contactos()
                agenda.esperarTecla()
            case "3":
                agenda.buscar_contacto()
                agenda.esperarTecla()
            case "4":
                agenda.modificar_contacto()
                agenda.esperarTecla()
            case "5":
                agenda.eliminar_contacto()
                agenda.esperarTecla()
            case "6":
                agenda.borrarPantalla()
                print("Terminaste la ejecución del SW")
                opcion = False
            case _:
                input("Opción inválida, vuelva a intentarlo... por favor")

if __name__ == "__main__":
    main()