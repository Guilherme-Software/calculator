from tkinter import *
from tkinter import ttk

#colors

c1 = "#000000" #black
c2 = "#3a85fc" #blue
c3 = "#1f2026" #gray
c4 = "#14d9b8" #blue2

#att value
def press(key):
    current = value_text.get()
    value_text.set(current + key)

#calculate
def calculate():
    try:
        result = eval(value_text.get())
        value_text.set(result)
    except Exception as e:
        value_text.set("Error")


#clear
def clear():
    value_text.set("")


window =Tk()
window.title("Calculator")
window.geometry("250x250")
window.config(bg=c1)


#frame creation 
frame_screen = Frame(window, width=250, height=60, bg=c3)
frame_screen.grid(row=0, column=0) 

frame_body = Frame(window, width=250, height=260)
frame_body.grid(row=1, column=0) 


#label
value_text = StringVar()

#screen value
app_label = Label(frame_screen, textvariable=value_text, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 19'), bg=c3, fg="white")
app_label.place(x=0, y=0)

#buttons

buttons = [
    {"text": "AC", "x": 0, "y": 0, "bg": c4, "width": 17, "command": clear},
    {"text": "%", "x": 125, "y": 0, "bg": c2, "command": lambda:press("%")},
    {"text": "/", "x": 190, "y": 0, "bg": c2, "command": lambda:press("/")},

    {"text": "9", "x": 0, "y": 38, "bg": c3, "fg": "white", "command": lambda:press("9")},
    {"text": "8", "x": 60, "y": 38, "bg": c3, "fg": "white", "command": lambda:press("8")},
    {"text": "7", "x": 125, "y":38, "bg": c3, "fg": "white", "command": lambda:press("7")},
    {"text": "*", "x": 190, "y": 38, "bg": c2, "command": lambda:press("*")},

    {"text": "4", "x": 0, "y": 76, "bg": c3, "fg": "white", "command": lambda:press("4")},
    {"text": "5", "x": 60, "y": 76, "bg": c3, "fg": "white", "command": lambda:press("5")},
    {"text": "6", "x": 125, "y": 76, "bg": c3, "fg": "white", "command": lambda:press("6")},
    {"text": "-", "x": 190, "y": 76, "bg": c2, "command": lambda:press("-")},

    {"text": "1", "x": 0, "y": 114, "bg": c3, "fg": "white", "command": lambda:press("1")},
    {"text": "2", "x": 60, "y": 114, "bg": c3, "fg": "white", "command": lambda:press("2")},
    {"text": "3", "x": 125, "y": 114, "bg": c3, "fg": "white", "command": lambda:press("3")},
    {"text": "+", "x": 190, "y": 114, "bg": c2, "command": lambda:press("+")},

    {"text": "0", "x": 0, "y": 152, "bg": c3, "fg": "white", "width": 17, "command": lambda:press("0")},
    {"text": ".", "x": 125, "y": 152, "bg": c3, "fg": "white", "command": lambda:press(".")},
    {"text": "=", "x": 190, "y": 152, "bg": c2, "command": calculate},


]

for button in buttons:
    command = button.get("command", None)
    Button(
        frame_body,
        text=button["text"],
        width=button.get("width", 8),
        height=button.get("height", 2),
        bg=button["bg"],
        font=('Ivy 8 bold'),
        relief=RAISED,
        overrelief=RIDGE,
        fg=button.get("fg", "black"),
        command=command,
        ).place(x=button["x"], y=button["y"])



window.mainloop()