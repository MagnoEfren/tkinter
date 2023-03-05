# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren/
#Tkinter y Matplotlib

from tkinter import Tk, Frame,Button,Label, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(dpi=90, figsize=(7,5),facecolor='#00faafb7')
plt.title("Grafica en Tkinter con Matplotlib",color='red',size=16, family="Arial")

plt.xlim(-4, 14)
plt.ylim(-8, 8)
ax.set_facecolor('black')

ax.axhline(linewidth=2, color='r')
ax.axvline(linewidth=2, color='r')

ax.set_xlabel("Eje  Horizontal", color='black')
ax.set_ylabel("Eje  Vertical", color='black')
ax.tick_params(direction='out', length=6, width=2, 
	colors='black',
    grid_color='r', grid_alpha=0.5)

def graficar_datos():
	nivel = scale.get()
	x = np.arange(-np.pi, 4*np.pi, 0.01) 	
	line, = ax.plot(x, nivel*np.sin(x), 
		color ='b', linestyle='solid')
	canvas.draw()
	label.config(text= nivel)
	line.set_ydata(np.sin(x)+10)
	ventana.after(100, graficar_datos)

ventana = Tk()
ventana.geometry('642x498')
ventana.wm_title('Grafica Matplotlib con Scale')
ventana.minsize(width=642,height=495)

frame = Frame(ventana,  bg='gray22',bd=3)
frame.grid(column=0,row=0)

canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
canvas.get_tk_widget().grid(column=0, row=0, columnspan=3, padx=5, pady =5)

Button(frame, text='Grafica Datos', width = 15, bg='magenta',fg='white', command= graficar_datos).grid(column=0, row=1, pady =5)
label = Label(frame, width = 15)
label.grid(column=1, row=1, pady =5)

scale = ttk.Scale(frame, to = 6, from_ =0, orient='horizontal', length=300)
scale.grid(column=2, row=1)

style = ttk.Style()
style.configure("Horizontal.TScale", background= 'gray22')  
ventana.mainloop()

