# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren/
# ProgressBar Circular

from tkinter import Canvas, Tk,Frame ,LAST, Button,ttk
from math import cos, sin, radians, pi

ventana = Tk()
ventana.title('ProgressBar Circular')
ventana.geometry('620x650+290+10')
ventana.config(bg='black')

frame = Frame(ventana, height=600, width =600,  
	bg= 'black', relief ='sunken')
frame.grid(columnspan=2,row=0)

canvas = Canvas(frame, bg= 'black', width = 
	585, height =585, relief ='raised', bd =1)
canvas.grid( padx=5, pady = 5)

nivel = 0
def progressBar():
	global nivel	
	nivel = int(scale1.get()) 

	canvas.create_oval(100,100,500,500, 
		fill="", outline ='',width=5)

	canvas.create_line(300,300, 300 + 150*sin(radians(nivel)), 
		300 - 150*cos(radians(nivel)), 
		fill='deep sky blue',width=20)
	canvas.create_line(300,300, 300 + 150*sin(radians(nivel+8)), 
		300 - 150*cos(radians(nivel+8)), 
		fill='black',width=20)

	if nivel == 0:
		canvas.create_line(300,300, 300 + 150*sin(radians(0)),
		 300 - 150*cos(radians(0)), 
			fill='black',width=20)
		canvas.create_line(300,300, 300 + 150*sin(radians(8)), 300 - 150*cos(radians(8)), 
			fill='black',width=20)
	if nivel == 360:
		canvas.create_line(300,300, 300 + 150*sin(radians(0)), 300 - 150*cos(radians(0)), 
			fill='deep sky blue',width=20)
		canvas.create_line(300,300, 300 + 150*sin(radians(8)), 300 - 150*cos(radians(8)), 
			fill='deep sky blue',width=20)

	canvas.create_oval(150,150,450,450, fill= '', outline='dark violet', width= 6)
	canvas.create_oval(180,180,420,420, fill='gray22', outline='dark violet', width=6)

	#############TEXTO ################
	texto = int(nivel/3.6)
	texto = str(texto) + '%'
	canvas.create_text(300, 300, text= texto, font=('Arial',42, 'bold'), fill ='deep sky blue')
	canvas.create_text(300, 350, text= 'PYTHON' , font=('Cambria Math',22, 'bold'), fill ='white')
	canvas.create_text(300, 380, text= 'Tkinter' , font=('Freestyle Script',25, 'bold'), fill ='orange')

	ventana.after(100,progressBar)


scale1 = ttk.Scale(ventana, orient= 'horizontal', style="Horizontal.TScale", from_ = 0, to=360, length=400)
scale1.set(0)
scale1.grid(column=1, row=1,  pady=10, padx=5)

style = ttk.Style()
style.configure("Horizontal.TScale", background="black")  

Button(ventana, text= 'Iniciar', bg= 'green2',width=20, command= progressBar).grid(column=0,row=1, padx=3, pady=5)
ventana.mainloop()
































