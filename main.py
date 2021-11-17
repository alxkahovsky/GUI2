import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog


def getResolution(input_res):
    values = {
        '1000 x 1000': 1000,
        '1500 x 1500': 1500,
        '2000 x 2000': 2000
              }
    return values[input_res]


def getBright():
    bright = int(scaleExample.get())
    return bright


def showbutton():
    res = comboExample.get()
    print('Значние стороны: ',getResolution(res), "Пикселей")
    print("Добавить яркость:", getBright(), "%")


def pic():

    our_image = PhotoImage(file="163387.png")
    our_image = our_image.subsample(5, 5)
    our_label = Label(app)
    our_label.image = our_image
    our_label['image'] = our_label.image
    our_label.place(x=400, y=400)

def info_window():
    windows = Toplevel()
    windows.title('Водяной знак')
    windows.geometry('1000x1000')
    panel = Label(windows, image=img)
    panel.pack(side="bottom", fill="both", expand="no")

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)







app = tk.Tk()
app.title(" программа на Python")
app.geometry('1000x800+400+150')
img = ImageTk.PhotoImage(Image.open("163387.png"))
labelTop = tk.Label(app,
                    text = "Выбери размер Выбери размер Выбери размер Выбери размер Выбери размер ")
labelTop.grid(column=1, row=1)

comboExample = ttk.Combobox(app,
                            values=[
                                    "1000 x 1000",
                                    "1500 x 1500",
                                    "2000 x 2000",
                                    ])
#print(dict(comboExample))
comboExample.grid(column=0, row=1)
comboExample.current(0)

button = tk.Button(app, text="размер",
             command=showbutton)
button.grid(column=0, row=2)
scaleExample = tk.Scale(app,
                        orient='horizontal',
                        resolution=1,
                        from_=-100,
                        to=100,
                        length=200,
                        )

scaleExample.grid(column=0, row=3)


button = tk.Button(app, text="show",
             command=info_window)
button.grid(column=0, row=5)


our_image = PhotoImage(file="logotype128x37.png")
our_image = our_image.subsample(1, 1)
our_label = Label(app)
our_label.image = our_image
our_label['image'] = our_label.image
our_label.place(x=0, y=200)


folder_path = StringVar()

lbl1 = Label(master=app,textvariable=folder_path, bg='gray50', width=50)
lbl1.grid(row=10, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=10, column=3)



app.mainloop()






