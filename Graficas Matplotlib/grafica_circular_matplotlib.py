# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren/

from tkinter import Tk, Frame,Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


ventana = Tk()
ventana.geometry('655x505')
ventana.wm_title('Grafica Circular')
ventana.minsize(width=655,height=505)
frame = Frame(ventana,  bg='blue')
frame.grid(column=0,row=0, sticky='nsew')

nombres = ['Fresa', 'Piña', 'Manzana', 'Uva']
colores = ['blue','red','aqua','fuchsia']
tamaño = [20, 26, 30, 24]
explotar = [0.05, 0.05, 0.05, 0.05] 

fig , ax1 = plt.subplots(dpi=100, facecolor = 'white',
	figsize=(5,5))

plt.title("Cantidad de Frutas Disponibles",
	color='black',size=18, family="Arial")

ax1.pie(tamaño, explode = explotar, labels = nombres, 
	colors = colores,
		autopct = '%1.0f%%', pctdistance = 0.6,
        shadow=True, startangle=90, radius = 0.8, 
        labeldistance=0.3)  

ax1.axis('equal')  #Dibuja el circulo

canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
canvas.draw()
canvas.get_tk_widget().grid(column=0, row=0, rowspan=3)

Button(frame, text='Grafica Datos', width = 20, bg='green2').grid(column=1, row=0)
Button(frame, text='Grafica Datos', width = 20, bg='magenta').grid(column=1, row=1)
Button(frame, text='Grafica Datos', width = 20, bg='orange').grid(column=1, row=2)

ventana.mainloop()

