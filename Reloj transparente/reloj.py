# https://www.youtube.com/c/MagnoEfren/videos
# Reloj transparente en tkinter

from tkinter import Label, Tk
import time  

ventana = Tk() 
ventana.config(bg='gray')
ventana.wm_attributes('-transparentcolor', 'gray')
# ventana.wm_attributes("-alpha", 0.5) Para linux
# ventana.wait_visibility(ventana)  Para linux
ventana.overrideredirect(1)   # Eliminar barra de titulo

def salir(*args):
    ventana.destroy()
    ventana.quit()

def obtener_tiempo():	
	hora =  time.strftime('%H:%M:%S')
	zona = time.strftime('%Z')	
	fecha_formatol2 = time.strftime(
        '%A' ' ' '%d' ' ' '%B' ' ' '%Y' )

	texto_hora['text'] = hora
	texto_fecha12['text']= fecha_formatol2
	zona_horaria['text'] = zona
	texto_hora.after(1000, obtener_tiempo)


def start(event):
    global x, y
    x = event.x
    y = event.y
 
def stop(event):
    global x, y
    x = None
    y = None
 
def mover(event):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    ventana.geometry("+%s+%s" % (ventana.winfo_x() + 
        deltax, ventana.winfo_y() + deltay))
    ventana.update()

ventana.bind("<ButtonPress-1>", start)                                      
ventana.bind("<ButtonRelease-1>", stop)                                      
ventana.bind("<B1-Motion>", mover)                                              
ventana.bind("<KeyPress-Escape>", salir)                                         # salir 

texto_hora = Label(ventana,  fg = 'white', bg='gray', 
font = ('Star Jedi Hollow', 50, 'bold'), width=10)                                #Star Jedi Hollow  #SolsticeOfSuffering
texto_hora.grid(column=0, row=0, ipadx=1, ipady=1)

texto_fecha12 = Label(ventana,  fg = 'white',  
    bg='gray', font = ('Vivaldi',20, 'bold'))
texto_fecha12.grid(column= 0, row=1)

zona_horaria = Label(ventana,  fg = 'white',  
    bg='gray', font = ('Lucida Sans',12)) 
zona_horaria.grid(column = 0, row=2)

obtener_tiempo()
ventana.mainloop() 
