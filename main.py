import tkinter as tk
from tkinter import ttk


def getResolution(input_res):
    values = {
        '1000 x 1000': 1000,
        '1500 x 1500': 1500,
        '2000 x 2000': 2000
              }
    return(values[input_res])


def getBright():
    bright = int(scaleExample.get())
    return bright


def showbutton():
    res = comboExample.get()
    print('Значние стороны: ',getResolution(res), "Пикселей")
    print("Добавить яркость:", getBright(), "%")





app = tk.Tk()
app.geometry('800x800')

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

app.mainloop()



