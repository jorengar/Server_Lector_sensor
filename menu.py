
import constantes as cts

class Menu:
    def __init__(_) -> None:
        pass

    def menu_init(_):
        print("1. Iniciar Host")
        print("2. Salir")

    def menu_action(_):
        print("1. Ingresar nueva acción")
        print("2. Guardar como cvs")


    def get_user_choice(_):
        """Obtener la selección del usuario para un menú específico."""
        while True:
            try:
                choice = int(input(cts.msj_select_option))
                return choice
            except ValueError:
                print(cts.error_validation)

    def seleccionar_menu(_,menu_number:int, init:bool = False):
        if menu_number == cts.opcion_uno and init == True:
            _.menu_init()
        elif menu_number == cts.opcion_uno and init == False:
            _.menu_action()
        elif menu_number ==  cts.opcion_dos and init == False:
            print("Guardando...")
        return _.get_user_choice()
    
    def datos_ingresar(_):
        try: 
            nuevo_voltaje = float(input("Ingresa el nuevo Voltaje: "))
            nueva_corriente = float(input("Ingresa la nueva corriente: "))
            nueva_potencia = float(input("Ingresa nueva potencia: "))
            return [nuevo_voltaje,nueva_corriente,nueva_potencia]
        except ValueError:
            print(cts.error_validation)
            return [0,0,0]