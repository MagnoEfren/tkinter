# Youtube: Magno Efren

from tkinter import Tk, Frame, Button,PhotoImage,Label,Text
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox
from customtkinter import CTk, CTkButton
import openai  #pip install openai  

openai.api_key ="OPENAI_API_KEY"

def generate_text(prompt):
	try:
	    response = openai.Completion.create(
	        model="text-davinci-003",
	        prompt=prompt,
	        temperature=0.7,
	        max_tokens=100,
	        top_p=1,
	        frequency_penalty=0,
	        presence_penalty=0,
	    )
	    return response.choices[0].text
	except Exception as e:
		return 'No se conecto a la IA'

def save_file():
    text = text_out.get("1.0", 'end') 
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, "w") as file:
        file.write(text)


def show_data():
	question = text_in.get('1.0', 'end')
	if len(question) != 0:
		text_in.delete('1.0', 'end')
		question_show = '\n'  + 'YO: ' + '\n'  + question      
		text_out.insert('end', question_show)
		res = generate_text(question)
		res = 'IA: ' + res  #'\n' 
		text_out.insert('end', res)
	else:
		messagebox.showerror('Error', 'No se logro comunicar')

window = CTk() 
window.geometry('600x400+400+100')
window.title('Aplicación ChatGTP')
window.config(bg='black')
window.minsize(500, 300)
window.iconphoto(False, PhotoImage(file='assets/icon.png'))

img_save = PhotoImage(file= 'assets/save.png')
img_send = PhotoImage(file= 'assets/send.png')


frame_text = Frame(window, bg= 'white', width=400, height=400)
frame_text.grid(column=0, row=0, sticky='nsew', pady = 5, padx=5)
frame_control = Frame(window, bg= 'black', width=200, height=400)
frame_control.grid(column=1, row=0, sticky='nsew', pady = 5, padx=5)

window.columnconfigure(0, weight=6)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)

frame_text.grid_propagate(0)
frame_control.grid_propagate(0)

frame_text.columnconfigure(0, weight=1)
frame_text.rowconfigure(0, weight=1)

frame_control.columnconfigure(0, weight=1)
frame_control.rowconfigure([0,1,2], weight=1)

text_out = ScrolledText(frame_text, font = ('Arial', 12), insertbackground= 'blue',
	bg= 'black', fg= 'white')
text_out.grid(column=0, row=0, sticky= 'nsew')

text_in = Text(frame_control, font = ('Arial', 12), insertbackground= 'blue',
	bg= 'black', fg= 'white', height=12)
text_in.grid(column=0, row=0)

button_send = CTkButton(frame_control,image = img_send,compound= 'left',text= '  ENVIAR',
	text_font= ('Arial', 11, 'bold') , fg_color= 'blue', command= show_data)
button_send.grid(column = 0, row=1, sticky='nsew',pady = 15, padx=15)

button_save = CTkButton(frame_control,image = img_save,compound= 'left',text= 'GUARDAR',
	text_font= ('Arial', 11, 'bold') , fg_color= 'blue', command= save_file)
button_save.grid(column = 0, row=2, sticky='nsew',pady = 15, padx=15)


window.mainloop()