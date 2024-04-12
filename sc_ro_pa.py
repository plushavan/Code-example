#Paper, Scissors, Rock app (tkinter, random etc.)

#Modules
import tkinter as tk
from tkinter import ttk
from random import choice
import time as tm
from PIL import Image, ImageTk


#Window settings
window = tk.Tk()
window.geometry("600x600")
window.title("Камень, ножницы, бумага")



#Appearance (alterable)
def appearance():
    canvas_line = tk.Canvas(height = 50, width = 600)
    canvas_line.place(x = 1, y = 300)
    canvas_line.create_line(1, 25, 600, 25, fill = "grey", width = 4)
appearance()


#Text
you_lab = tk.Label(window, text = "YOU", font = "fantasy 12", borderwidth = 10)
opp_lab = tk.Label(window, text = "OPPONENT\n\n*waiting*", font = "fantasy 12", borderwidth = 10)
win_or_lose = tk.Label(window, text = None, font = "fantasy 14", borderwidth = 10)
you_lab.place(x = 1, y = 1)
opp_lab.place(x = 1, y = 330)
win_or_lose.place(x = 1, y = 450)


#Main Interface
start_button = tk.Button(window, text = "PLAY", font = "Sans-Serif 15 bold", borderwidth = 5,
                         padx = 50, bg = "powder blue", state = "disabled", command = lambda: opp_logic(choice_tool))
choice_tool = ttk.Combobox(window, values = ["Scissors", "Paper", "Rock"], state = "readonly", justify = "center", width = 10,
                           font = "fantasy 12 bold")
image_label = ttk.Label(window, image = None)
opp_image = ttk.Label(window, image = None)
start_button.place(x = 1, y = 270)
choice_tool.place(x = 1, y = 100)
image_label.place(x = 300, y = 100)
opp_image.place(x = 300, y = 400)

#Main Logic
class Score:
    def __init__(self, score, score_lab):
        self.score = score
        self.score_lab = score_lab
        
        
    def altering(self, new):
        self.score += new
        self.score_lab.configure(text = f"Score: {str(self.score)}")
        
    def zero(self):
        self.score *= 0
        self.score_lab.configure(text = "Score: 0")
        
        
score_lab = tk.Label(window, text = "Score: 0", font = "fantasy 13", borderwidth = 10)
score_opp = tk.Label(window, text = "Score: 0", font = "Times_New_Roman 13", borderwidth = 10)
score_lab.place(x = 300, y = 1)
score_opp.place(x = 300, y = 330)
score = Score(0, score_lab)
score_opp = Score(0, score_opp)


def choosen(event=None):
    start_button.configure(state = "normal")
    info = choice_tool.get()
    image = choose_image(info)
    image_label.configure(image = image, width = 10)
    image_label.image = image
    
choice_tool.bind("<<ComboboxSelected>>", choosen)

def opp_logic(choice_tool):
    opp_lab.configure(text = "OPPONENT")
    your = choice_tool.get()
    responce = choice(["Paper", "Scissors", "Rock"])
    image = choose_image(responce)
    opp_image.configure(image = image, width = 10)
    opp_image.image = image
    result = hierarchy(your, responce)
    if result == 1:
        win_or_lose.configure(text = "YOU WIN", fg = "#2ECC71")
        score.altering(1)
        score_opp.zero()
    elif result == 2:
        win_or_lose.configure(text = "DRAW", fg = "#F4D03F")
    else:
        win_or_lose.configure(text = "YOU LOSE", fg = "#E74C3C")
        score.zero()
        score_opp.altering(1)

#Sub Logic
def choose_image(tool):
    if tool == "Paper":
        image = Image.open("images/.Paper_small.png")
        image = ImageTk.PhotoImage(image)
    elif tool == "Rock":
        image = Image.open("images/.Rock_small.png")
        image = ImageTk.PhotoImage(image)
    elif tool == "Scissors":
        image = Image.open("images/.scissors_small.png") 
        image = ImageTk.PhotoImage(image)
    return image

def hierarchy(your, responce):
    if your == "Paper":
        if responce == "Paper":
            return 2
        elif responce == "Rock":
            return 1
        else:
            return 0
    elif your == "Rock":
        if responce == "Paper":
            return 0
        elif responce == "Rock":
            return 2
        else:
            return 1
    else:
        if responce == "Paper":
            return 1
        elif responce == "Rock":
            return 0
        else:
            return 2

#Incomplete
#def text_vanish(win_or_lose):
#    tm.sleep(3)
#    win_or_lose.configure(text = None)
    
    
    
        
        
            
window.mainloop()