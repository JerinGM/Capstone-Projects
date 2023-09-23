from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

########### Read data from CSV
try:
    data = pandas.read_csv("./data/newData.csv")

except FileNotFoundError:
    new_data = pandas.read_csv("./data/french_words.csv")
    new_dict = new_data.to_dict()
else:
    new_dict = data.to_dict(orient="records")
#print(new_dict)


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(new_dict)
    canvas.itemconfig(french_word, text="French", fill="black")
    canvas.itemconfig(french_words, text=f"{current_card['French']}", fill='black')
    canvas.itemconfig(image, image=imgOne)
    timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(image, image=imgTwo)
    canvas.itemconfig(french_word, text="English", fill="white")
    canvas.itemconfig(french_words, text=f"{current_card['English']}", fill="white")


def learned():
    new_dict.remove(current_card)
    data = pandas.DataFrame(new_dict)
    data.to_csv("data/newData.csv", index=False)
    next_card()

# # print(random.choice(new_dict['French']))
# rand = random.choice(list(new_dict['French'].keys()))
# # print(rand) Got the index
# rand_word = new_dict['French'][rand]
# # print(rand_word)

# window object
window = Tk()
window.title("Flash Card - Learning Game")
window.config(padx=20, pady=80, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

# canvas one white
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
imgOne = PhotoImage(file="./images/card_front.png")
imgTwo = PhotoImage(file="./images/card_back.png")
image = canvas.create_image(412, 270, image=imgOne)
french_word = canvas.create_text(410, 200, text="", font=("Ariel", 30, "italic"))
french_words = canvas.create_text(410, 280, text="", font=("Ariel", 35, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Red Button
rButton = PhotoImage(file="./images/wrong.png")
redButton = Button(image=rButton, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
redButton.grid(row=1, column=0)

# Green Button
gButton = PhotoImage(file="./images/right.png")
greenButton = Button(image=gButton, highlightthickness=0, bg=BACKGROUND_COLOR, command=learned)
greenButton.grid(row=1, column=1)

next_card()

window.mainloop()
