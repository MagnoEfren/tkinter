# Juego Snake V2
# @autor: Magno Efren (Optimizado)
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Tk, Frame, Canvas, Button, Label, ALL
import random
from pygame import mixer

class SnakeGame:
    def __init__(self, ventana):
        self.ventana = ventana
        self.configurar_ventana()
        
        # Variables del juego
        self.x = 15
        self.y = 15
        self.direction = ''
        self.posicion_snake = [(75, 75)]
        self.posicion_food = (15, 15)
        self.juego_activo = False
        self.juego_pausado = False
        self.velocidad = 300
        self.posiciones_validas = [15, 45, 75, 105, 135, 165, 195, 225, 255, 
                                   285, 315, 345, 375, 405, 435, 465]
        
        # Inicializar mixer
        try:
            mixer.init()
        except:
            pass
        
        # Crear interfaz
        self.crear_interfaz()
        self.crear_tablero()
        
    def configurar_ventana(self):
        """Configura la ventana principal"""
        self.ventana.config(bg='black')
        self.ventana.title('Juego Snake - Mejorado')
        self.ventana.geometry('485x569')
        self.ventana.resizable(0, 0)
        
    def crear_interfaz(self):
        """Crea los frames y controles del juego"""
        # Frame superior (controles)
        self.frame_controles = Frame(self.ventana, width=485, height=60, bg='black')
        self.frame_controles.grid(column=0, row=0, pady=5)
        
        # Frame del juego
        self.frame_juego = Frame(self.ventana, width=485, height=490, bg='black')
        self.frame_juego.grid(column=0, row=1)
        
        # Botones de control
        self.btn_iniciar = Button(
            self.frame_controles, 
            text='▶ INICIAR', 
            bg='lime green',
            fg='white',
            font=('Arial', 10, 'bold'),
            width=10,
            command=self.iniciar_juego
        )
        self.btn_iniciar.grid(row=0, column=0, padx=5, pady=5)
        
        self.btn_pausar = Button(
            self.frame_controles, 
            text='⏸ PAUSAR', 
            bg='yellow',
            fg='black',
            font=('Arial', 10, 'bold'),
            width=10,
            command=self.pausar_juego,
            state='disabled'
        )
        self.btn_pausar.grid(row=0, column=1, padx=5, pady=5)
        
        self.btn_reset = Button(
            self.frame_controles, 
            text='🔄 RESET', 
            bg='orange',
            fg='white',
            font=('Arial', 10, 'bold'),
            width=10,
            command=self.resetear_juego
        )
        self.btn_reset.grid(row=0, column=2, padx=5, pady=5)
        
        self.btn_salir = Button(
            self.frame_controles, 
            text='✖ SALIR', 
            bg='red',
            fg='white',
            font=('Arial', 10, 'bold'),
            width=10,
            command=self.salir
        )
        self.btn_salir.grid(row=0, column=3, padx=5, pady=5)
        
        # Label de puntuación
        self.lbl_puntuacion = Label(
            self.frame_controles, 
            text='Puntuación 🍎: 1', 
            bg='black', 
            fg='lime green', 
            font=('Arial', 12, 'bold')
        )
        self.lbl_puntuacion.grid(row=1, column=0, columnspan=4, pady=5)
        
        # Canvas del juego
        self.canvas = Canvas(self.frame_juego, bg='black', width=479, height=479)
        self.canvas.pack()
        
        # Vincular teclas
        self.ventana.bind("<KeyPress-Up>", lambda e: self.cambiar_direccion('up'))
        self.ventana.bind("<KeyPress-Down>", lambda e: self.cambiar_direccion('down'))
        self.ventana.bind("<KeyPress-Left>", lambda e: self.cambiar_direccion('left'))
        self.ventana.bind("<KeyPress-Right>", lambda e: self.cambiar_direccion('right'))
        self.ventana.bind("<space>", lambda e: self.pausar_juego())
        
    def crear_tablero(self):
        """Crea el tablero del juego"""
        # Crear cuadrícula
        for i in range(0, 480, 30):
            for j in range(0, 480, 30):
                self.canvas.create_rectangle(
                    i, j, i+30, j+30, 
                    fill='gray10', 
                    outline='gray20'
                )
        
        # Crear comida inicial
        self.canvas.create_text(
            self.posicion_food[0], 
            self.posicion_food[1], 
            text='🍎', 
            fill='red2',
            font=('Arial', 18), 
            tag='food'
        )
        
        # Crear serpiente inicial
        self.canvas.create_text(
            *self.posicion_snake[0], 
            text='▀', 
            fill='lime green', 
            font=('Arial', 20), 
            tag='snake'
        )
        
    def cambiar_direccion(self, nueva_direccion):
        """Cambia la dirección de la serpiente"""
        if not self.juego_activo or self.juego_pausado:
            return
            
        direcciones_opuestas = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }
        
        if self.direction != direcciones_opuestas.get(nueva_direccion):
            self.direction = nueva_direccion
            
    def calcular_nueva_posicion(self):
        """Calcula la nueva posición de la cabeza de la serpiente"""
        if self.direction == 'up':
            self.y -= 30
            if self.y < 15:
                self.y = 465
        elif self.direction == 'down':
            self.y += 30
            if self.y > 465:
                self.y = 15
        elif self.direction == 'left':
            self.x -= 30
            if self.x < 15:
                self.x = 465
        elif self.direction == 'right':
            self.x += 30
            if self.x > 465:
                self.x = 15
                
        return (self.x, self.y)
        
    def mover_serpiente(self):
        """Mueve la serpiente"""
        if not self.juego_activo or self.juego_pausado:
            return
            
        # Calcular nueva posición
        nueva_cabeza = self.calcular_nueva_posicion()
        
        # Verificar colisión consigo misma
        if nueva_cabeza in self.posicion_snake and len(self.posicion_snake) >= 4:
            self.game_over()
            return
            
        # Actualizar posición de la serpiente
        self.posicion_snake.insert(0, nueva_cabeza)
        
        # Verificar si comió la manzana
        if nueva_cabeza == self.posicion_food:
            self.comer_manzana()
        else:
            self.posicion_snake.pop()
            
        # Actualizar visualización
        self.actualizar_canvas()
        
        # Verificar victoria
        if len(self.posicion_snake) >= 257:
            self.victoria()
            return
            
        # Continuar el juego
        self.ventana.after(self.velocidad, self.mover_serpiente)
        
    def comer_manzana(self):
        """Lógica cuando la serpiente come una manzana"""
        # Reproducir sonido
        try:
            mixer.music.load("assets/audio_snake.mp3")
            mixer.music.play(loops=0)
        except:
            pass
            
        # Actualizar puntuación
        puntuacion = len(self.posicion_snake)
        self.lbl_puntuacion['text'] = f'Puntuación 🍎: {puntuacion}'
        
        # Generar nueva comida
        self.generar_comida()
        
    def generar_comida(self):
        """Genera una nueva posición para la comida"""
        while True:
            self.posicion_food = (
                random.choice(self.posiciones_validas), 
                random.choice(self.posiciones_validas)
            )
            if self.posicion_food not in self.posicion_snake:
                break
                
        self.canvas.coords(self.canvas.find_withtag("food"), self.posicion_food)
        
    def actualizar_canvas(self):
        """Actualiza la visualización de la serpiente"""
        # Eliminar serpiente anterior
        self.canvas.delete("snake")
        
        # Dibujar serpiente nueva
        for i, pos in enumerate(self.posicion_snake):
            color = 'lime green' if i == 0 else 'green2'
            self.canvas.create_text(
                *pos, 
                text='▀', 
                fill=color, 
                font=('Arial', 20), 
                tag='snake'
            )
            
    def iniciar_juego(self):
        """Inicia el juego"""
        if not self.juego_activo:
            self.juego_activo = True
            self.juego_pausado = False
            self.direction = 'right'
            self.btn_iniciar.config(state='disabled')
            self.btn_pausar.config(state='normal')
            self.mover_serpiente()
            
    def pausar_juego(self):
        """Pausa o continúa el juego"""
        if not self.juego_activo:
            return
            
        self.juego_pausado = not self.juego_pausado
        
        if self.juego_pausado:
            self.btn_pausar.config(text='▶ CONTINUAR', bg='lime green', fg='white')
            self.mostrar_pausa()
        else:
            self.btn_pausar.config(text='⏸ PAUSAR', bg='yellow', fg='black')
            self.canvas.delete("pausa")
            self.mover_serpiente()
            
    def mostrar_pausa(self):
        """Muestra mensaje de pausa"""
        self.canvas.create_text(
            240, 240,
            text='PAUSA\n\nPresiona ESPACIO\no clic en CONTINUAR',
            fill='yellow',
            font=('Arial', 20, 'bold'),
            tag='pausa'
        )
        
    def resetear_juego(self):
        """Reinicia el juego"""
        # Detener juego actual
        self.juego_activo = False
        self.juego_pausado = False
        
        # Reiniciar variables
        self.x = 15
        self.y = 15
        self.direction = ''
        self.posicion_snake = [(75, 75)]
        self.posicion_food = (15, 15)
        
        # Limpiar canvas
        self.canvas.delete(ALL)
        
        # Recrear tablero
        self.crear_tablero()
        
        # Reiniciar puntuación
        self.lbl_puntuacion['text'] = 'Puntuación 🍎: 1'
        
        # Habilitar botón iniciar
        self.btn_iniciar.config(state='normal')
        self.btn_pausar.config(state='disabled', text='⏸ PAUSAR', bg='yellow', fg='black')
        
    def game_over(self):
        """Muestra pantalla de game over"""
        self.juego_activo = False
        self.canvas.delete(ALL)
        self.canvas.create_text(
            240, 240,
            text=f'GAME OVER\n\nPuntuación Final: {len(self.posicion_snake)}\n\n🍎\n\nPresiona RESET\npara jugar de nuevo',
            fill='red',
            font=('Arial', 20, 'bold')
        )
        self.btn_iniciar.config(state='disabled')
        self.btn_pausar.config(state='disabled')
        
    def victoria(self):
        """Muestra pantalla de victoria"""
        self.juego_activo = False
        self.canvas.delete(ALL)
        self.canvas.create_text(
            240, 240,
            text='¡EXCELENTE!\n\n°° VICTORIA °°\n\n🍎🍎🍎\n\n¡Completaste el juego!',
            fill='lime green',
            font=('Arial', 25, 'bold')
        )
        self.btn_iniciar.config(state='disabled')
        self.btn_pausar.config(state='disabled')
        
    def salir(self):
        """Cierra el juego"""
        self.ventana.destroy()
        self.ventana.quit()


# Ejecutar el juego
if __name__ == "__main__":
    ventana = Tk()
    juego = SnakeGame(ventana)
    ventana.mainloop()