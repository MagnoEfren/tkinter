# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren/
#Tkinter y Matplotlib Animacion

from tkinter import Tk, Frame,Button,Label, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(facecolor='#4F406A')
plt.title("Grafica en Tkinter con Matplotlib",color='white',size=16, family="Arial")

ax.tick_params(direction='out', length=6, width=2, 
	colors='white',
    grid_color='r', grid_alpha=0.5)


x = np.arange(-2*np.pi, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x), color='r', marker='o', linestyle='dotted', 
	linewidth=8, markersize=1, markeredgecolor='m')  #dotted, dashdot,dashed

plt.xlim([-2*np.pi, 2*np.pi])
plt.ylim([-2,2])  #x.min(), x.max()


def animate(i):
    line.set_ydata(np.sin(x+ i/40))  
    return line,

def iniciar():	
	global ani
	ani = animation.FuncAnimation(fig, animate, 
		interval=20, blit=True, save_count=10)	 
	canvas.draw()

def pausar():
	ani.event_source.stop() 

def reanudar():
	ani.event_source.start()

ventana = Tk()
ventana.geometry('642x535')
ventana.wm_title('Grafica Matplotlib Animacion')
ventana.minsize(width=642,height=535)

frame = Frame(ventana,  bg='gray22',bd=3)
frame.pack(expand=1, fill='both')

canvas = FigureCanvasTkAgg(fig, master = frame)  
canvas.get_tk_widget().pack(padx=5, pady=5 , expand=1, fill='both') 


Button(frame, text='Grafica Datos', width = 15, bg='purple4',fg='white', command=iniciar).pack(pady =5,side='left',expand=1)
Button(frame, text='Pausar', width = 15, bg='salmon',fg='white', command=pausar).pack(pady =5,side='left',expand=1)
Button(frame, text='Reanudar', width = 15, bg='green',fg='white', command=reanudar).pack(pady =5,side='left',expand=1)

ventana.mainloop()

"""
plt.figure () : Para crear una nueva figura
plt.plot () : Trace y versus x como líneas y / o marcadores
plt.xlabel () : Establezca la etiqueta para el eje x
plt.ylabel () : Establezca la etiqueta para el eje y
plt.title () : Establecer un título para los ejes
plt.grid () : Configurar las líneas de la cuadrícula
plt.legend () : Colocar una leyenda en los ejes
plt.savefig () : Para guardar la figura actual en el disco
plt.show () :muestra una figura 
plt.clf () : borra la figura actual útil para trazar varias figuras en el mismo código

"""



"""        y1 = value*np.sin(x) + int(value-2)
        y2 = value*np.sin(x) - int(value-2)

        plt.fill_between(x, y1 , y2 , alpha = .05, color = 'darkorchid')"""