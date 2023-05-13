from PIL import Image, ImageTk
import tkinter as tk 
from pygame import mixer 
import random

mixer.init() 
window = tk.Tk()
window.geometry('1000x600')
window.title('Flappy Bird')

x = 150
y = 300
score = 0
speed = 10
game_over = False

img_bird = Image.open('images/bird.png')
img_bird = ImageTk.PhotoImage(img_bird)

img_pipe_down = Image.open('images/pipe.png')           # 104x900
img_pipe_top = img_pipe_down.rotate(180)

img_pipe_down = ImageTk.PhotoImage(img_pipe_down)
img_pipe_top = ImageTk.PhotoImage(img_pipe_top)

img_reset = Image.open('images/reiniciar.png')
img_reset = ImageTk.PhotoImage(img_reset)

canvas = tk.Canvas(window, highlightthickness=0, bg= '#00bfff')
canvas.place(relwidth = 1, relheight=1)

text_score = canvas.create_text(50,50, text= '0', fill='white', font=('D3 Egoistism outline', 30))

bird = canvas.create_image(x,y, anchor = 'nw', image =img_bird)
pipe_top = canvas.create_image(1200, -550, anchor= 'nw', image = img_pipe_top)
pipe_down = canvas.create_image(1200, 550, anchor= 'nw', image = img_pipe_down)

mixer.music.load('audio/swoosh.wav')
mixer.music.play(loops= 0)

def move_bird_key(event):
	global x,y
	if not game_over:
		y -=30
		canvas.coords(bird, x,y)
		mixer.music.load('audio/wing.wav')
		mixer.music.play(loops= 0)


window.bind( "<space>", move_bird_key)


def move_bird():
	global x,y
	y +=5
	canvas.coords(bird, x,y)
	if y<0 or y> window.winfo_height():
		game_end()

	if not game_over:
		window.after(50, move_bird)

def move_pipe():
	global score, game_over, speed
	canvas.move(pipe_top, -speed, 0)
	canvas.move(pipe_down, -speed, 0)
	if canvas.coords(pipe_down)[0] < -100:
		score += 1
		speed += 1
		canvas.itemconfigure(text_score, text = str(score))
		h = window.winfo_height()
		num = random.choice([i for i in range(160,h, 160)])
		canvas.coords(pipe_down, window.winfo_width(), num+160)
		canvas.coords(pipe_top, window.winfo_width(), num-900)

	if 0 < canvas.coords(pipe_down)[0]<160:
		channel = mixer.Channel(1)
		channel.set_volume(1.0)
		sound = mixer.Sound('audio/point.wav')
		channel.play(sound, loops= 0)

	if canvas.coords(pipe_down):
		if canvas.bbox(bird)[0] < canvas.bbox(pipe_down)[2] and canvas.bbox(bird)[2]> canvas.bbox(pipe_down)[0]:
			if canvas.bbox(bird)[1] < canvas.bbox(pipe_top)[3] or canvas.bbox(bird)[3]> canvas.bbox(pipe_down)[1]:
				game_end()
	if  not game_over:
		window.after(50, move_pipe)


def reset_game():
	global x,y,score, speed, game_over
	x = 150
	y = 300
	score = 0
	speed = 10
	game_over = False
	canvas.coords(bird, x,y)
	canvas.coords(pipe_top, 1200,-550)
	canvas.coords(pipe_down, 1200, 550)
	canvas.itemconfigure(text_score, text ="0")
	lbl_game_over.place_forget()
	bt_reset.place_forget()
	move_bird()
	move_pipe()
	mixer.music.load('audio/swoosh.wav')
	mixer.music.play(loops= 0)

def game_end():
	global game_over
	game_over = True
	lbl_game_over.place(relx =0.5, rely =0.5, anchor='center')
	bt_reset.place(relx = 0.5, rely = 0.7, anchor ='center')
	mixer.music.load('audio/hit.wav')
	mixer.music.play(loops= 0)
	while mixer.music.get_busy():
		continue
	mixer.music.load('audio/die.wav')
	mixer.music.play(loops= 0)

lbl_game_over = tk.Label(window, text = 'Game Over !', font= ('D3 Egoistism outline', 30), fg='white', bg='#00bfff')
bt_reset = tk.Button(window, border = 0, image= img_reset, activebackground='#00bfff', bg= '#00bfff', command = reset_game)

window.after(50, move_bird)
window.after(50, move_pipe)

window.call('wm', 'iconphoto', window._w, img_bird) 
window.mainloop()
