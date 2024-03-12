
from flask import Flask, request,jsonify
from menu import Menu
import constantes as cts
from datos import myDatos
import threading
import logging
import time

app =Flask(__name__)
data = myDatos()
menu = Menu()

class myServer:
    
    def __init__(self):
        self.hilo_esperar_accion = threading.Thread(target=self.esperar_accion)
    
    @app.route('/')
    def index(self):
        return '¡Hola, mundo! Esta es la página de inicio.'

    @app.route(cts.ruta_data, methods=['GET'])
    def get_data():
        return 'Esta es una ruta para métodos GET.'

    @app.route(cts.ruta_data, methods=['POST'])
    def put_data():
        try:
            if not data.is_waiting(): 
                data.append_data(request.get_json())
                print(data.get_data())
                return jsonify({"mensaje": "Datos recibidos y guardados correctamente"}), 200
            else:
                return jsonify({"mensaje": "Esperando datos"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def iniciar_hilo(self):
        self.hilo_esperar_accion.start()

    def ejecutar_servidor(self):
        self.iniciar_hilo()
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)
        app.logger.disabled = True
        log.disabled = True
        app.run(debug=False)

        

    def esperar_accion(self):
        time.sleep(1)
        while True:
            option = menu.seleccionar_menu(cts.opcion_uno)
            if option == cts.opcion_uno:
                data.wait_data(True)
                datos = menu.datos_ingresar()
                data.actualizar_data(datos)
                data.wait_data(False)
            elif option == cts.opcion_dos:
                data.wait_data(True)
                data.save_csv()
                data.wait_data(False)