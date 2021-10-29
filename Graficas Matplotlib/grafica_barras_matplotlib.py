# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren/

from tkinter import Tk, Frame,Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ventana = Tk()
ventana.geometry('990x325')
ventana.wm_title('Graficas Matplotlib')
ventana.minsize(width=950,height=325)

frame = Frame(ventana,  bg='blue')
frame.grid(column=0,row=0, sticky='nsew')

nombres = ['Azul', 'Rojo', 'Verde', 'Magenta','Negro']
colores = ['blue','red','green','magenta', 'black']
tamaño = [15, 25, 10, 20, 30]

fig, axs = plt.subplots(1,3 , dpi=80, figsize=(13, 4), 
	sharey=True, facecolor='#00f9f844')

fig.suptitle('Graficas Matplotlib')

axs[0].bar(nombres, tamaño, color = colores)  # edgecolor='black',linewidth=1.2
axs[1].scatter(nombres, tamaño, color = colores)
axs[2].plot(nombres, tamaño, color = 'm')


canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
canvas.draw()
canvas.get_tk_widget().grid(column=0, row=0)


ventana.mainloop()
