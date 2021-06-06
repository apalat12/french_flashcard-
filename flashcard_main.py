from tkinter import *
import pandas as pd
import random
import time
from tkinter import messagebox
import pyperclip
import json

BACKGROUND_COLOR = "#B1DDC6"
GREEN = "#9bdeac"
WHITE = "#FFFFFF"

CURR_WORD = {}

try:
    new_data = pd.read_csv("flash-card-project-start/data/words_to_learn.csv")
    fr_words_list = new_data.to_dict(orient="records")

except:
    words = pd.read_csv("flash-card-project-start/data/french_words.csv")
    # names_dict = {v.French: v.English for (k, v) in words.iterrows()}
    fr_words_list = words.to_dict(orient="records")

def next_card():
    global CURR_WORD
    CURR_WORD = random.choice(fr_words_list)
    canvas.itemconfig(card_image, image=front_card)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_front_word, text=CURR_WORD["French"])
    window.after(3000, func=flip_card)


def flip_card():
    global CURR_WORD
    canvas.itemconfig(card_image, image=back_card)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_front_word, text=CURR_WORD["English"])


def is_known():
    global CURR_WORD
    fr_words_list.remove(CURR_WORD)
    print(len(fr_words_list))
    new_data = pd.DataFrame(fr_words_list)
    new_data.to_csv("flash-card-project-start/data/words_to_learn.csv",index=False)
    next_card()


# ------------------------UI Setup --------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)  # Just one time thing after 3secs

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, border="0", highlightthickness=0)
front_card = PhotoImage(file="flash-card-project-start/images/card_front.png")
card_image = canvas.create_image(400, 263, image=front_card)

card_title = canvas.create_text(400, 100, text="", font=("Ariel", "40", "italic"))
card_front_word = canvas.create_text(400, 263, text="", font=("Ariel", "40", "bold"))
canvas.grid(row=0, column=0, columnspan=2)

back_card = PhotoImage(file="flash-card-project-start/images/card_back.png")
# back_card_image = canvas.create_image(400, 263, image=back_card)


cross_image = PhotoImage(file="flash-card-project-start/images/wrong.png")
cross = Button(image=cross_image, highlightthickness=0, command=next_card)
cross.grid(row=1, column=0)

green_check = PhotoImage(file="flash-card-project-start/images/right.png")
check_button = Button(image=green_check, highlightthickness=0,command=is_known)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()
