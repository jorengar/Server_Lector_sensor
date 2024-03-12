from servidor import myServer
from menu import Menu
import constantes as cts

menu = Menu()

if __name__ == "__main__":
    miServidor = myServer()
    if menu.seleccionar_menu(cts.opcion_uno,True) == 1:   
        miServidor.ejecutar_servidor()