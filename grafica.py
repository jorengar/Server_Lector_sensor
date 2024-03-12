import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class Grafica:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.x_data, self.y_data = [], []
        self.line, = self.ax.plot([], [], label='Datos de entrada')

    def init(self):
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.ax.set_xlabel('Tiempo')
        self.ax.set_ylabel('Valor')
        self.ax.legend()
        return self.line,

    def update(self, frame):
        x, y = frame
        self.x_data.append(x)
        self.y_data.append(y)
        self.line.set_data(self.x_data, self.y_data)
        return self.line,

    def animate(self):
        ani = animation.FuncAnimation(self.fig, self.update, init_func=self.init, blit=True, interval=100)
        plt.show()

    def agregar_dato(self, nuevo_dato):
        x, y = nuevo_dato
        self.x_data.append(x)
        self.y_data.append(y)
        self.line.set_data(self.x_data, self.y_data)
        self.fig.canvas.draw_idle()