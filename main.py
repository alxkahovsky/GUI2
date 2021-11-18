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


def LoadFile():
    ftypes = [('Все файлы', '*'), ('txt файлы', '*.txt'), ('Файлы Python', '*.py'),
              ('Файлы html', '*.html')]  # Фильтр файлов
    fn = tk.filedialog.Open(app, filetypes=ftypes).show()

    if fn == '':
        return
    text.delete('1.0', 'end')  # Очищаем окно редактирования
    text.insert('1.0', open(fn).read())  # Вставляем текст в окно редактирования

    global cur_path
    cur_path = fn  # Храним путь к открытому файлу
    print(cur_path)

def SaveFile():
    fn = tk.filedialog.SaveAs(app, filetypes = [('Все файлы', '*'), ('txt файлы', '*.txt'), ('Файлы Python', '*.py'), ('Файлы html', '*.html')]).show()
    if fn == '':
        return
    open(fn, 'wt').write(text.get('1.0', 'end'))







app = tk.Tk()
app.title("Python resize tool")
app.geometry('530x600+400+150')
img = ImageTk.PhotoImage(Image.open("163387.png"))


comboExample = ttk.Combobox(app,
                            values=[
                                    "1000 x 1000",
                                    "1500 x 1500",
                                    "2000 x 2000",
                                    ],
                            width=18,
                            justify='center')
#print(dict(comboExample))
comboExample.place(x=0, y=374)
comboExample.current(0)

#button = tk.Button(app, text="КНОПКА ДЛЯ ТЕСТОВ!НЕ ТРОГАТЬ ",
             #command=showbutton)
#button.place(x=300, y=180)
scaleExample = tk.Scale(app,
                        orient='horizontal',
                        resolution=1,
                        from_=-100,
                        to=100,
                        length=128,
                        )

scaleExample.place(x=132, y=358)


button = tk.Button(app, text="Показать знак",
             command=info_window,
                   width=18, bd=1,
                   activebackground='LightCyan2')
button.place(x=264, y=373)


our_image = PhotoImage(file="logotype128x37.png")
our_image = our_image.subsample(1, 1)
#our_label = Label(app)
#our_label.image = our_image
#our_label['image'] = our_label.image
#our_label.place(x=150, y=35)



res_button = PhotoImage(file='resize button.png')
bri_button = PhotoImage(file='bright button.png')
wm_button = PhotoImage(file='watermark button.png')
csv_button = PhotoImage(file='csv button.png')

pyrt_logo = PhotoImage(file='pyrt_logo.png')
pyrt_logo = pyrt_logo.subsample(2, 2)
#pyrt_label = Label(app)
#pyrt_label.image = pyrt_logo
#pyrt_label['image'] = pyrt_label.image
#pyrt_label.place(x=0, y=0)


folder_path = StringVar()

lbl1 = Label(master=app,text='Изменить размер:')
lbl1.place(x=11, y=345)

lbl2 = Label(master=app,text='Изменить яркость:')
lbl2.place(x=140, y=345)

lbl3 = Label(master=app,text='Наложить водяной знак:')
lbl3.place(x=260, y=345)

lbl3 = Label(master=app,text='Импорт имен')
lbl3.place(x=426, y=345)

lbl4 = Label(master=app,text='в CSV таблицу:')
lbl4.place(x=425, y=365)
#button2 = Button(text="Обзор", command=browse_button, highlightcolor="red")
#button2.place(x=132, y=180)




button4 = Button(app, image=res_button, command=lambda: print('resize'), bd=1, activebackground='LightCyan2')
button4.place(x=0, y=400)

button5 = Button(app, image=bri_button, command=lambda: print('bright'), bd=1, activebackground='LightCyan2')
button5.place(x=132, y=400)

button6 = Button(app, image=wm_button, command=lambda: print('watermark'), bd=1, activebackground='LightCyan2')
button6.place(x=265, y=400)

button7 = Button(app, image=csv_button, command=lambda: print('CSV'), bd=1, activebackground='LightCyan2')
button7.place(x=398, y=400)

button8 = Button(app, image=pyrt_logo, command=lambda: print('info'), bd=0)
button8.place(x=0, y=0)


button9 = Button(app, image=our_image, command=lambda: print('usadba url'), bd=0)
button9.place(x=398, y=550)

text = Text(width=50, height=12)
text.place(x=10, y=100)







#instruktionBtn = Button(app, text='Открыть ТХТ', command=LoadFile)
#instruktionBtn.place(x=430, y=100)

instruktionBtn = Button(app, text='Сохранить ТХТ', command=SaveFile)
instruktionBtn.place(x=430, y=250)



app.mainloop()






