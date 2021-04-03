from math import nan
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

#=================== EXCEL MANIPULATION ===================#

data = pd.read_excel("data.xlsx", engine="openpyxl")
data_df = pd.DataFrame(data=data)
data_df.dropna(subset=["front"], inplace=True)
df = data_df.loc[:, ~data_df.columns.str.contains('^Unnamed')]  # drops Unnamed columns

to_learn = df.to_dict(orient="records")
current_card = {}


#=================== BUTTON FUNCTION ===================#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Key", fill="black")
    canvas.itemconfig(card_word, text=current_card["front"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text= "Definition", fill="white")
    canvas.itemconfig(card_word, text=current_card["back"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    


#=================== GUI SET-UP ===================#

window = Tk()
window.title("Flashy")
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=1000, height=600)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(600, 300, image=card_front_img)
card_title = canvas.create_text(100, 50, text=" ", font=("Arial", 20, "italic"))
card_word = canvas.create_text(200, 100, text="", font=("Arial", 14, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image, height=80,
                        width=80, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="right.png")
known_button = Button(image=check_image, height=80,
                      width=80, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()

