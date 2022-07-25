# Menu Lateral desplegable y base de datos MySQL
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren
# https://www.youtube.com/watch?v=01W_qYxnHbI&t=525s

from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import  StringVar,Scrollbar,Frame
from conexion import*
import time
class Ventana(Frame):
	def __init__(self, master, *args):
		super().__init__( master,*args)

		self.menu = True
		self.color = True
		self.codigo = StringVar()
		self.nombre = StringVar()
		self.modelo = StringVar()
		self.precio = StringVar()
		self.cantidad = StringVar()
		self.buscar = StringVar()
		self.buscar_actualiza =  StringVar()
		self.id = StringVar()
		self.base_datos = Registro_datos()

		self.frame_inicio = Frame(self.master, bg='black', width=50, height=45)
		self.frame_inicio.grid_propagate(0)
		self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
		self.frame_menu = Frame(self.master, bg='black', width = 50)
		self.frame_menu.grid_propagate(0)
		self.frame_menu.grid(column=0, row = 1, sticky='nsew')
		self.frame_top = Frame(self.master, bg='black', height = 50)
		self.frame_top.grid(column = 1, row = 0, sticky='nsew')
		self.frame_principal = Frame(self.master, bg='black')
		self.frame_principal.grid(column=1, row=1, sticky='nsew')
		self.master.columnconfigure(1, weight=1)
		self.master.rowconfigure(1, weight=1)
		self.frame_principal.columnconfigure(0, weight=1)
		self.frame_principal.rowconfigure(0, weight=1)
		self.widgets()		

	def pantalla_inicial(self):
		self.paginas.select([self.frame_uno])
		
	def pantalla_datos(self):
		self.paginas.select([self.frame_dos])
		self.frame_dos.columnconfigure(0, weight=1)
		self.frame_dos.columnconfigure(1, weight=1)
		self.frame_dos.rowconfigure(2, weight=1)
		self.frame_tabla_uno.columnconfigure(0, weight=1)
		self.frame_tabla_uno.rowconfigure(0, weight=1)

	def pantalla_escribir(self):
		self.paginas.select([self.frame_tres])
		self.frame_tres.columnconfigure(0, weight=1)
		self.frame_tres.columnconfigure(1, weight=1)

	def pantalla_actualizar(self):
		self.paginas.select([self.frame_cuatro])	
		self.frame_cuatro.columnconfigure(0, weight=1)
		self.frame_cuatro.columnconfigure(1, weight=1)

	def pantalla_buscar(self):
		self.paginas.select([self.frame_cinco])
		self.frame_cinco.columnconfigure(0, weight=1)
		self.frame_cinco.columnconfigure(1, weight=1)
		self.frame_cinco.columnconfigure(2, weight=1)
		self.frame_cinco.rowconfigure(2, weight=1)
		self.frame_tabla_dos.columnconfigure(0, weight=1)
		self.frame_tabla_dos.rowconfigure(0, weight=1)

	def pantalla_ajustes(self):
		self.paginas.select([self.frame_seis])

	def menu_lateral(self):
		if self.menu is True:
			for i in range(50,170,10):				
				self.frame_menu.config(width= i)
				self.frame_inicio.config(width= i)
				self.frame_menu.update()
				clik_inicio = self.bt_cerrar.grid_forget()
				if clik_inicio is None:		
					self.bt_inicio.grid(column=0, row=0, padx =10, pady=10)
					self.bt_inicio.grid_propagate(0)
					self.bt_inicio.config(width=i)
					self.pantalla_inicial()
			self.menu = False
		else:
			for i in range(170,50,-10):
				self.frame_menu.config(width=  i)
				self.frame_inicio.config(width= i)
				self.frame_menu.update()
				clik_inicio = self.bt_inicio.grid_forget()
				if clik_inicio is   None:
					self.frame_menu.grid_propagate(0)		
					self.bt_cerrar.grid(column=0, row=0, padx =10, pady=10)
					self.bt_cerrar.grid_propagate(0)
					self.bt_cerrar.config(width=i)
					self.pantalla_inicial()
			self.menu = True

	def cambiar_color(self):
		if self.color == True:
			self.bt_color['image'] = self.dia
			self.titulo.config(fg='deep sky blue')
			self.frame_seis.config(bg= 'black')
			self.text_ajustes.config(bg='black')
			self.texto.config(bg='black')
			self.bt_color.config(bg='black',activebackground='black')	
			self.color = False	
		else:
			self.bt_color['image'] = self.noche
			self.titulo.config(fg='DarkOrchid1')
			self.frame_seis.config(bg= 'white')
			self.text_ajustes.config(bg='white')
			self.texto.config(bg='white')
			self.bt_color.config(bg='white',activebackground='white')	
			self.color = True
	def widgets(self):
		self.imagen_inicio = PhotoImage(file ='inicio.png')
		self.imagen_menu = PhotoImage(file ='menu.png')
		self.imagen_datos = PhotoImage(file ='datos.png')
		self.imagen_registrar = PhotoImage(file ='escribir.png')
		self.imagen_actualizar = PhotoImage(file ='actualizar.png')
		self.imagen_buscar = PhotoImage(file ='buscar.png')
		self.imagen_ajustes = PhotoImage(file ='configuracion.png')

		self.logo = PhotoImage(file ='logo.png')
		self.imagen_uno = PhotoImage(file ='imagen_uno.png')
		self.imagen_dos= PhotoImage(file ='imagen_dos.png')
		self.dia = PhotoImage(file ='dia.png')
		self.noche= PhotoImage(file ='noche.png')
		self.bt_inicio = Button(self.frame_inicio, image= self.imagen_inicio, bg='black',activebackground='black', bd=0, command = self.menu_lateral)
		self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
		self.bt_cerrar = Button(self.frame_inicio, image= self.imagen_menu, bg='black',activebackground='black', bd=0, command = self.menu_lateral)
		self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)	
		#BOTONES Y ETIQUETAS DEL MENU LATERAL 
		Button(self.frame_menu, image= self.imagen_datos, bg='black', activebackground='black', bd=0, command = self.pantalla_datos).grid(column=0, row=1, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_registrar, bg='black',activebackground='black', bd=0, command =self.pantalla_escribir ).grid(column=0, row=2, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_actualizar, bg= 'black',activebackground='black', bd=0, command = self.pantalla_actualizar).grid(column=0, row=3, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_buscar, bg= 'black',activebackground='black', bd=0, command = self.pantalla_buscar).grid(column=0, row=4, pady=20,padx=10)		
		Button(self.frame_menu, image= self.imagen_ajustes, bg= 'black',activebackground='black', bd=0, command = self.pantalla_ajustes).grid(column=0, row=5, pady=20,padx=10)
		
		Label(self.frame_menu, text= 'Base Datos', bg= 'black', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
		Label(self.frame_menu, text= 'Registrar', bg= 'black', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
		Label(self.frame_menu, text= ' Actualizar', bg= 'black', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=3, pady=20, padx=2)
		Label(self.frame_menu, text= 'Eliminar', bg= 'black', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=4, pady=20, padx=2)	
		Label(self.frame_menu, text= 'Ajustes', bg= 'black', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=5, pady=20, padx=2)

        	#############################  CREAR  PAGINAS  ##############################
		estilo_paginas = ttk.Style()
		estilo_paginas.configure("TNotebook", background='black', foreground='black', padding=0, borderwidth=0)
		estilo_paginas.theme_use('default')
		estilo_paginas.configure("TNotebook", background='black', borderwidth=0)
		estilo_paginas.configure("TNotebook.Tab", background="black", borderwidth=0)
		estilo_paginas.map("TNotebook", background=[("selected", 'black')])
		estilo_paginas.map("TNotebook.Tab", background=[("selected", 'black')], foreground=[("selected", 'black')]);

		#CREACCION DE LAS PAGINAS 
		self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook') #, style = 'TNotebook'
		self.paginas.grid(column=0,row=0, sticky='nsew')
		self.frame_uno = Frame(self.paginas, bg='DarkOrchid1')
		self.frame_dos = Frame(self.paginas, bg='white')
		self.frame_tres = Frame(self.paginas, bg='white')
		self.frame_cuatro = Frame(self.paginas, bg='white')
		self.frame_cinco = Frame(self.paginas, bg='white')
		self.frame_seis = Frame(self.paginas, bg='white')
		self.paginas.add(self.frame_uno)
		self.paginas.add(self.frame_dos)
		self.paginas.add(self.frame_tres)
		self.paginas.add(self.frame_cuatro)
		self.paginas.add(self.frame_cinco)
		self.paginas.add(self.frame_seis)
		##############################         PAGINAS       #############################################

		######################## FRAME TITULO #################
		self.titulo = Label(self.frame_top,text= 'APLICACION DE ESCRITORIO EN PYTHON CON TKINTER', bg='black', fg= 'DarkOrchid1', font= ('Imprint MT Shadow', 15, 'bold'))
		self.titulo.pack(expand=1)
		######################## VENTANA PRINCIPAL #################
		Label(self.frame_uno, text= 'Electrónica Programación y Tecnología', bg='DarkOrchid1', fg= 'white', font= ('Freehand521 BT', 20, 'bold')).pack(expand=1)
		Label(self.frame_uno ,image= self.logo, bg='DarkOrchid1').pack(expand=1)

		######################## MOSTRAR TODOS LOS PRODUCTOS DE LA BASE DE DATOS MYSQL #################
		Label(self.frame_dos, text= 'Datos de MySQL', bg='white', fg= 'DarkOrchid1', font= ('Comic Sans MS', 12, 'bold')).grid(column =0, row=0)
		Button(self.frame_dos, text='ACTUALIZAR',fg='black' ,font = ('Arial', 11,'bold'), command= self.datos_totales, bg = 'green2', bd = 2, borderwidth=2).grid(column=1, row=0, pady=5)
		#ESTILO DE LAS TABLAS DE DATOS TREEVIEW
		estilo_tabla = ttk.Style()
		estilo_tabla.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')  #, fieldbackground='yellow'
		estilo_tabla.map('Treeview',background=[('selected', 'DarkOrchid1')], foreground=[('selected','black')] )		
		estilo_tabla.configure('Heading',background = 'white', foreground='navy',padding=3, font= ('Arial', 10, 'bold'))
		estilo_tabla.configure('Item',foreground = 'white', focuscolor ='DarkOrchid1')
		estilo_tabla.configure('TScrollbar', arrowcolor = 'DarkOrchid1',bordercolor  ='black', troughcolor= 'DarkOrchid1',background ='white')
		#TABLA UNO 
		self.frame_tabla_uno = Frame(self.frame_dos, bg= 'gray90')
		self.frame_tabla_uno.grid(columnspan=3, row=2, sticky='nsew')		
		self.tabla_uno = ttk.Treeview(self.frame_tabla_uno) 
		self.tabla_uno.grid(column=0, row=0, sticky='nsew')
		ladox = ttk.Scrollbar(self.frame_tabla_uno, orient = 'horizontal', command= self.tabla_uno.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = ttk.Scrollbar(self.frame_tabla_uno, orient ='vertical', command = self.tabla_uno.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.tabla_uno.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
		self.tabla_uno['columns'] = ('Nombre', 'Modelo', 'Precio', 'Cantidad')
		self.tabla_uno.column('#0', minwidth=100, width=120, anchor='center')
		self.tabla_uno.column('Nombre', minwidth=100, width=130 , anchor='center')
		self.tabla_uno.column('Modelo', minwidth=100, width=120, anchor='center' )
		self.tabla_uno.column('Precio', minwidth=100, width=120 , anchor='center')
		self.tabla_uno.column('Cantidad', minwidth=100, width=105, anchor='center')

		self.tabla_uno.heading('#0', text='Codigo', anchor ='center')
		self.tabla_uno.heading('Nombre', text='Nombre', anchor ='center')
		self.tabla_uno.heading('Modelo', text='Modelo', anchor ='center')
		self.tabla_uno.heading('Precio', text='Precio', anchor ='center')
		self.tabla_uno.heading('Cantidad', text='Cantidad', anchor ='center')
		self.tabla_uno.bind("<<TreeviewSelect>>", self.obtener_fila) 

		######################## REGISTRAR  NUEVOS PRODUCTOS #################
		Label(self.frame_tres, text = 'Agregar Nuevos Datos',fg='purple', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
		Label(self.frame_tres, text = 'Codigo',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15, padx=5)
		Label(self.frame_tres, text = 'Nombre',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
		Label(self.frame_tres, text = 'Modelo',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
		Label(self.frame_tres, text = 'Precio', fg='navy',bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
		Label(self.frame_tres, text = 'Cantidad',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)  ##E65561

		Entry(self.frame_tres, textvariable=self.codigo , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=1)
		Entry(self.frame_tres, textvariable=self.nombre , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=2)
		Entry(self.frame_tres, textvariable=self.modelo , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=3)
		Entry(self.frame_tres, textvariable=self.precio , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=4)
		Entry(self.frame_tres, textvariable=self.cantidad , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=5)

		Button(self.frame_tres,command= self.agregar_datos, text='REGISTRAR', font=('Arial',10,'bold'), bg='magenta2').grid(column=3,row=6, pady=10, padx=4)
		Label(self.frame_tres, image= self.imagen_uno, bg= 'white').grid(column= 3, rowspan= 5, row = 0, padx= 50)
		self.aviso_guardado = Label(self.frame_tres, bg= 'white', font=('Comic Sans MS', 12), fg='black')
		self.aviso_guardado.grid(columnspan= 2 , column =0, row = 6, padx= 5)

		########################   ACTUALIZAR LOS PRODUCTOS REGISTRADOS     #################
		Label(self.frame_cuatro, text = 'Actualizar Datos',fg='purple', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan=4, row=0)		
		Label(self.frame_cuatro, text = 'Ingrese el nombre del producto a actualizar',fg='black', bg ='white', font=('Rockwell',12)).grid(columnspan=2,row=1)
		Entry(self.frame_cuatro, textvariable= self.buscar_actualiza , font=('Comic Sans MS', 12), highlightbackground = "magenta2", width=12, highlightthickness=5).grid(column=2,row=1, padx=5)
		Button(self.frame_cuatro, command= self.actualizar_datos, text='BUSCAR', font=('Arial',12,'bold'), bg='deep sky blue').grid(column=3,row=1, pady=5, padx=15)
		self.aviso_actualizado = Label(self.frame_cuatro, fg='black', bg ='white', font=('Arial',12,'bold'))
		self.aviso_actualizado.grid(columnspan= 2, row=7, pady=10, padx=5)

		Label(self.frame_cuatro, text = 'Codigo',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15, padx=10)
		Label(self.frame_cuatro, text = 'Nombre',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
		Label(self.frame_cuatro, text = 'Modelo',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
		Label(self.frame_cuatro, text = 'Precio', fg='navy',bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
		Label(self.frame_cuatro, text = 'Cantidad',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15)  ##E65561

		Entry(self.frame_cuatro, textvariable=self.codigo , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=2)
		Entry(self.frame_cuatro, textvariable=self.nombre , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=3)
		Entry(self.frame_cuatro, textvariable=self.modelo , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=4)
		Entry(self.frame_cuatro, textvariable=self.precio , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=5)
		Entry(self.frame_cuatro, textvariable=self.cantidad , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=6)

		Button(self.frame_cuatro,command= self.actualizar_tabla, text='ACTUALIZAR', font=('Arial',12,'bold'), bg='magenta2').grid(column=2, columnspan= 2 ,row=7, pady=2)
		Label(self.frame_cuatro, image= self.imagen_dos, bg='white').grid(column= 2,columnspan= 2, rowspan= 5, row = 1, padx=2)

		######################## BUSCAR y ELIMINAR DATOS #################
		Label(self.frame_cinco, text = 'Buscar y Eliminar Datos',fg='purple', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan= 4,  row=0,sticky='nsew',padx=2)
		Entry(self.frame_cinco, textvariable= self.buscar , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "deep sky blue", highlightthickness=5).grid(column=0,row=1,sticky='nsew', padx=2)
		Button(self.frame_cinco,command = self.buscar_nombre, text='BUSCAR POR NOMBRE', font=('Arial',8,'bold'), bg='deep sky blue').grid(column = 1, row=1, sticky='nsew', padx=2)		
		Button(self.frame_cinco,command = self.eliminar_fila, text='ELIMINAR', font=('Arial',8,'bold'), bg='red').grid(column = 2, row=1, sticky='nsew',padx=2)
		self.indica_busqueda= Label(self.frame_cinco, width= 15,text = '',fg='purple', bg ='white', font=('Arial',12,'bold'))
		self.indica_busqueda.grid(column = 3,  row=1,padx=2)

		#TABLA DOS
		self.frame_tabla_dos = Frame(self.frame_cinco, bg= 'gray90')
		self.frame_tabla_dos.grid(columnspan=4, row=2, sticky='nsew')
		self.tabla_dos = ttk.Treeview(self.frame_tabla_dos) 
		self.tabla_dos.grid(column=0, row=0, sticky='nsew')
		ladox = ttk.Scrollbar(self.frame_tabla_dos, orient = 'horizontal', command= self.tabla_dos.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = ttk.Scrollbar(self.frame_tabla_dos, orient ='vertical', command = self.tabla_dos.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.tabla_dos.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set,)
		self.tabla_dos['columns'] = ('Nombre', 'Modelo', 'Precio', 'Cantidad')
		self.tabla_dos.column('#0', minwidth=100, width=120, anchor='center')
		self.tabla_dos.column('Nombre', minwidth=100, width=130 , anchor='center')
		self.tabla_dos.column('Modelo', minwidth=100, width=120, anchor='center' )
		self.tabla_dos.column('Precio', minwidth=100, width=120 , anchor='center')
		self.tabla_dos.column('Cantidad', minwidth=100, width=105, anchor='center')
		self.tabla_dos.heading('#0', text='Codigo', anchor ='center')
		self.tabla_dos.heading('Nombre', text='Nombre', anchor ='center')
		self.tabla_dos.heading('Modelo', text='Modelo', anchor ='center')
		self.tabla_dos.heading('Precio', text='Precio', anchor ='center')
		self.tabla_dos.heading('Cantidad', text='Cantidad', anchor ='center')
		self.tabla_dos.bind("<<TreeviewSelect>>", self.obtener_fila)  	
		######################## AJUSTES #################
		self.text_ajustes = Label(self.frame_seis, text = 'Configuracion',fg='purple', bg ='white', font=('Kaufmann BT',28,'bold'))
		self.text_ajustes.pack(expand=1)
		self.bt_color = Button(self.frame_seis, image = self.noche , command= self.cambiar_color, bg = 'white', bd=0, activebackground='white')
		self.bt_color.pack(expand=1)
		self.texto = Label(self.frame_seis, text = '@autor:Magno Efren \n Desarrollado en Python',fg='red', bg ='white', font=('Kaufmann BT',18))
		self.texto.pack(expand=1)

	def datos_totales(self):
		datos = self.base_datos.mostrar_productos()
		self.tabla_uno.delete(*self.tabla_uno.get_children())
		i = -1
		for dato in datos:
			i= i+1
			self.tabla_uno.insert('',i, text = datos[i][1:2], values=datos[i][2:6])

	def agregar_datos(self):
		codigo = self.codigo.get()
		nombre = self.nombre.get()
		modelo = self.modelo.get()
		precio = self.precio.get()
		cantidad = self.cantidad.get()
		datos = (nombre, modelo, precio, cantidad)
		if codigo and nombre and modelo and precio and cantidad !='':
			self.tabla_uno.insert('',0, text = codigo, values=datos)
			self.base_datos.inserta_producto(codigo, nombre, modelo, precio, cantidad)
			self.aviso_guardado['text'] = 'Datos Guardados'
			self.limpiar_datos()
			self.aviso_guardado.update()						
			time.sleep(1) 
			self.aviso_guardado['text'] = ''						
		else:
			self.aviso_guardado['text'] = 'Ingrese todos los datos'
			self.aviso_guardado.update()
			time.sleep(1) 
			self.aviso_guardado['text'] = ''

	def actualizar_datos(self):
		dato = self.buscar_actualiza.get()
		dato = str("'" + dato + "'")
		nombre_buscado = self.base_datos.busca_producto(dato)
		if nombre_buscado == []:
			self.aviso_actualizado['text'] = 'No existe'			
			self.indica_busqueda.update()						
			time.sleep(1) 
			self.limpiar_datos()
			self.aviso_actualizado['text'] = ''
		else:
			i = -1
			for dato in nombre_buscado:
				i= i+1
				self.id.set(nombre_buscado[i][0])
				self.codigo.set(nombre_buscado[i][1])
				self.nombre.set(nombre_buscado[i][2])
				self.modelo.set(nombre_buscado[i][3])
				self.precio.set(nombre_buscado[i][4])
				self.cantidad.set(nombre_buscado[i][5])

	def actualizar_tabla(self):	
		Id = self.id.get() 	
		codigo = self.codigo.get()
		nombre = self.nombre.get()
		modelo = self.modelo.get()
		precio = self.precio.get()
		cantidad = self.cantidad.get()
		self.base_datos.actualiza_productos(Id, codigo, nombre, modelo, precio, cantidad)		
		self.aviso_actualizado['text'] = 'Datos Actualizados'			
		self.indica_busqueda.update()						
		time.sleep(1) 
		self.aviso_actualizado['text'] = ''
		self.limpiar_datos()
		self.buscar_actualiza.set('')				
	def limpiar_datos(self):
		self.codigo.set('')
		self.nombre.set('')
		self.modelo.set('')
		self.precio.set('')
		self.cantidad.set('')

	def buscar_nombre(self):
		nombre_producto = self.buscar.get()
		nombre_producto = str("'" + nombre_producto + "'")
		nombre_buscado = self.base_datos.busca_producto(nombre_producto)
		if nombre_buscado == []:
			self.indica_busqueda['text'] = 'No existe'
			self.indica_busqueda.update()						
			time.sleep(1) 
			self.indica_busqueda['text'] =''
		i = -1
		for dato in nombre_buscado:
			i= i+1
			self.tabla_dos.insert('',i, text = nombre_buscado[i][1:2], values=nombre_buscado[i][2:6])
	def eliminar_fila(self):
		fila = self.tabla_dos.selection()
		if len(fila) !=0:
			self.tabla_dos.delete(fila)
			nombre = ("'"+ str(self.nombre_borrar) + "'")
			self.base_datos.elimina_productos(nombre)
			self.indica_busqueda['text'] = 'Eliminado'
			self.indica_busqueda.update()						
			self.tabla_dos.delete(*self.tabla_dos.get_children())
			time.sleep(1)
			self.indica_busqueda['text'] =''
			self.limpiar_datos()
		else:
			self.indica_busqueda['text'] = 'No se Elimino'
			self.indica_busqueda.update()
			self.tabla_dos.delete(*self.tabla_dos.get_children())						
			time.sleep(1) 
			self.indica_busqueda['text'] =''
			self.buscar.set('')
			self.limpiar_datos()

	def obtener_fila(self, event):
		current_item = self.tabla_dos.focus()
		if not current_item:
			return
		data = self.tabla_dos.item(current_item)
		self.nombre_borrar = data['values'][0]

if __name__ == "__main__":
	ventana = Tk()
	ventana.title('')
	ventana.minsize(height= 475, width=795)
	ventana.geometry('1000x500+180+80')
	ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))	
	app = Ventana(ventana)
	app.mainloop()
