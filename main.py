import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
from textwrap import wrap


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

"""
Вот тут ниже буду писать вые функции
№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
"""



def db_window():
    def showbutton():
        group_id = comboGroup.get()
        shop = comboShop.get()
        shop2 = comboShop2.get()
        prod = prod_id.get()
        photo_chek = comboPhoto.get()
        if prod != '' and group_id == 'Выберите группу товаров' and shop == '' and shop2 == '' and photo_chek == 'укажите':
            print(prod)
            return prod
        else:
            print('No prod')

        if group_id != 'Выберите группу товаров' and shop != '' and shop2 != '' and photo_chek == 'укажите':

            print(group_id, shop, shop2)
            return (group_id, shop, shop2)
        elif group_id != 'Выберите группу товаров' and shop != ''and photo_chek == 'укажите':

            print(group_id, shop)
            return (group_id, shop)
        elif group_id != 'Выберите группу товаров'and photo_chek == 'укажите':

            print(group_id)
            return group_id
        else:
            print('no group, shop, shop2')

        #if photo_chek == 'Да' and group_id == 'Выберите группу товаров' and shop == '' and shop2 == '' and prod == '':
           # print(photo_chek)
        #else:
            #print('no photo')




    windows = Toplevel()
    windows.title('Окно работы с БД')
    windows.geometry('800x300+400+150')

    comboGroup = ttk.Combobox(windows,
                              values=[
                                  "Выберите группу товаров",
                                  "  5 КЛЕЕНКА",
                                  " 10 ТОВАРЫ ДЛЯ КОНСЕРВИРОВАНИЯ;",
                                  " 15 КЕРАМИЧЕСКОЕ КАШПО;",
                                  " 20 ПЛАСТМАССОВОЕ КАШПО;",
                                  " 25 ПЛАСТМАССОВАЯ ПОСУДА;",
                                  " 30 ПЛАСТМАССОВЫЕ БЫТ.ИЗДЕЛИЯ;",
                                  " 31 ТОВАРЫ ДЛЯ УБОРКИ;",
                                  " 35 ОЦИНКОВАННЫЕ ИЗДЕЛИЯ;",
                                  " 40 БАТАРЕЙКИ;",
                                  " 45 ЭЛЕКТРОУСТАНОВОЧНЫЕ ИЗДЕЛ.;",
                                  " 50 ЭЛЕКТРОМАТЕРИАЛЫ;",
                                  " 55 ЭЛЕКТРОЛАМПЫ;",
                                  " 70 СРЕДСТВА ДЛЯ СТИРКИ;",
                                  " 75 СРЕДСТВА ДЛЯ ЧИСТКИ;",
                                  " 80 МЫЛО;",
                                  " 95 КОСМ.СР-ВА, ПЕНА Д/БРИТЬЯ;",
                                  "110 АНТИСТАТИК,ЛАК,ОСВЕЖИТЕЛИ;",
                                  "115 ГИГИЕНИЧЕСКИЕ СРЕДСТВА;",
                                  "120 ГАЛАНТЕРЕЙНЫЕ ТОВАРЫ;",
                                  "125 ПАКЕТЫ, МЕШКИ ДЛЯ МУСОРА;",
                                  "126 ПОДАРОЧНЫЕ ПАКЕТЫ;",
                                  "130 СР-ВА Д/ОБУВИ И КОЖ.ИЗДЕЛ.;",
                                  "135 СР-ВА ОТ ГРЫЗУНОВ;",
                                  "140 СР-ВА ОТ КОМАРОВ, КЛЕЩЕЙ;",
                                  "145 СР-ВА ОТ БЫТОВЫХ НАСЕКОМЫХ;",
                                  "150 СР-ВА ОТ САД.ВРЕДИТЕЛЕЙ;",
                                  "155 СР-ВА ОТ БОЛЕЗНЕЙ РАСТЕНИЙ;",
                                  "160 СР-ВА ОТ СОРНЯКОВ;",
                                  "161 СР-ВА ДЛЯ ТУАЛЕТОВ, СЕПТИКОВ, КОМПОСТА, ПРУДОВ;",
                                  "165 РЕГУЛЯТОРЫ РОСТА РАСТЕНИЙ;",
                                  "168 МИКРОУДОБРЕНИЯ;",
                                  "169 ЖИДКИЕ УДОБРЕНИЯ;",
                                  "170 УДОБРЕНИЯ;",
                                  "171 ГАЗОНЫ,РОЗЫ,ПОСАД.МАТЕРИАЛ;",
                                  "173 КОРМА ДЛЯ ДОМАШНИХ ЖИВОТНЫХ;",
                                  "175 ГРУНТ, ДРЕНАЖ, ДЕКОР;",
                                  "176 СЕМЕНА ОДНОЛЕТНИХ ЦВЕТОВ;",
                                  "177 СЕМЕНА ОВОЩНЫХ КУЛЬТУР;",
                                  "185 ОПРЫСКИВАТЕЛИ,ШЛАНГИ;",
                                  "186 ЛЕЙКИ;",
                                  "187 СЕМЕНА ОВОЩНЫХ КУЛЬТУР Б/П;",
                                  "190 ПЛЕНКА П/Э;",
                                  "191 УКРЫВНОЙ МАТЕРИАЛ;",
                                  "195 ХОЗИНВЕНТАРЬ;",
                                  "196 САДОВЫЙ ДЕКОР,АРКИ,ШПАЛЕРЫ;",
                                  "197 ИНТЕРЬЕР;",
                                  "198 ТАЧКИ,СТРЕМЯНКИ,ГЛАД.ДОСКИ;",
                                  "199 ПАРНИКИ,ТЕПЛИЦЫ;",
                                  "200 ХОЗТОВАРЫ, ТОВАРЫ Д/ДОМА;",
                                  "201 ТОВАРЫ ДЛЯ РАССАДЫ;",
                                  "202 СКОТЧ,УПЛОТНИТЕЛЬ;",
                                  "205 ПЕРЧАТКИ,РУКАВИЦЫ,СПЕЦ.ОБ.;",
                                  "210 СТРОЙМАТЕРИАЛЫ;",
                                  "220 КЛЕЙ,ГЕРМЕТИК,ПЕНА МОНТАЖ.;",
                                  "225 ЭМАЛЬ, КРАСКИ;",
                                  "226 ВД, КОЛЕР;",
                                  "227 ЛАКИ, МОРИЛКИ;",
                                  "228 АЭРОЗ.КРАСКИ, ЭМАЛИ, ГРУНТЫ;",
                                  "240 ГВОЗДИ,МЕТИЗЫ,ШУРУПЫ;",
                                  "242 ИНСТРУМЕНТ ИНСТАР, Russland;",
                                  "244 МИР ИНСТРУМЕНТА;",
                                  "245 КРУГИ;",
                                  "246 ИНСТРУМЕНТ РЕСАНТА;",
                                  "247 ИНСТРУМЕНТ ОРМИС;",
                                  "255 СЛЕСАР.СТОЛЯР.ИНСТРУМЕНТ;",
                                  "264 ЭЛЕКТРОИНСТРУМЕНТ;",
                                  "280 САНФАЯНС, АКСЕСС. Д/ВАННОЙ;",
                                  "295 ЗАМКИ;",
                                  "305 ПЕЧНОЕ ЛИТЬЕ $;",
                                  "306 ТЕКСТИЛЬ;",
                                  "307 ВАЗЫ ДЕКОРАТИВНЫЕ СТЕКЛО;",
                                  "308 ВАЗЫ ДЕКОРАТИВНЫЕ КЕРАМИКА;",
                                  "310 КУХОННАЯ УТВАРЬ $;",
                                  "311 РАСХОДНЫЕ МАТЕРИАЛЫ ДЛЯ КУХНИ;",
                                  "315 СТОЛОВЫЕ ПРИБОРЫ, НОЖИ $;",
                                  "320 ТЕРМОСЫ $;",
                                  "325 ПОСУДА СТЕКЛО ИМПОРТ;",
                                  "326 ПОСУДА СТЕКЛО РОССИЯ;",
                                  "327 ПОСУДА СТЕКЛО ОСЗ;",
                                  "328 ПОСУДА СТЕКЛО ТУРЦИЯ;",
                                  "329 ПОСУДА СТЕКЛО ФРАНЦИЯ;",
                                  "330 ПОСУДА КЕРАМИКА, ФАРФОР $;",
                                  "331 ПОСУДА ФАРФОР ДОБРУШ;",
                                  "332 ПОСУДА ФАРФОР КРУЖКИ;",
                                  "333 ПОСУДА КОРАЛЛ;",
                                  "335 ПОСУДА АЛЮМИНИЕВАЯ,ЧУГУН.;",
                                  "336 ПОСУДА ДОЛОМИТ;",
                                  "337 ПОСУДА СТЕКЛОКЕРАМИКА;",
                                  "340 ПОСУДА ЭМАЛИРОВАННАЯ $;",
                                  "345 ПОСУДА ЖАРОПРОЧНАЯ СВЧ $;",
                                  "350 ПОСУДА АНТИПРИГАРНАЯ $;",
                                  "355 ПОСУДА НЕРЖАВЕЙКА $;",
                                  "374 БЫТОВАЯ ТЕХНИКА ENERGY,HOMESTAR;",
                                  "375 ПРОЧАЯ БЫТОВАЯ ТЕХНИКА;",
                                  "377 БЫТОВАЯ ТЕХНИКА DELTA;",
                                  "378 БЫТОВАЯ ТЕХНИКА SKIFF;",
                                  "380 ЧАСЫ, БУДИЛЬНИКИ;",
                                  "384 ИГРУШКИ;",
                                  "385 ЕЛОЧНЫЕ УКРАШЕНИЯ;",
                                  "390 НОВОГОДНИЕ ТОВАРЫ;",
                                  "395 ТОВАРЫ Д/ОТДЫХА, ТУРИЗМА;",
                                  "400 ПРОЧЕЕ;",
                                  "403 ТОВАРЫ ПРИКАССОВОЙ ЗОНЫ;",
                                  "405 ОБУВЬ;",
                                  "410 КАНЦЕЛЯРСКИЕ ТОВАРЫ;",
                                  "411 ТОВАРЫ ДЛЯ ТВОРЧЕСТВА;",
                                  "412 ТОВАРЫ ДЛЯ ПРАЗДНИКА;",
                                  "415 СУВЕНИРЫ;",
                                  "416 УПАК.МАТЕРИАЛ,ЭЛ-ТЫ ДЕКОРА;",
                                  "417 ПЕЧАТНАЯ ПРОДУКЦИЯ;",
                                  "418 НАСТОЛЬНЫЕ ИГРЫ, ПАЗЛЫ;",
                                  "420 ЧУЛОЧНО-НОСОЧНЫЕ ИЗДЕЛИЯ;"]
                              ,
                                width=40,
                                justify='center')
    comboGroup.place(x=127, y=0)
    comboGroup.current(0)

    comboShop = ttk.Combobox(windows,
                             values=['У20',
                                     'У21'],
                             width=12,
                             justify='center')
    comboShop.place(x=400, y= 0)
    #comboShop.current(0)

    comboShop2 = ttk.Combobox(windows,
                             values=['У20',
                                     'У21'],
                             width=12,
                             justify='center')
    comboShop2.place(x=500, y=0)
    #comboShop2.current()

    comboPhoto = ttk.Combobox(windows,
                              values=[
                                  'укажите',
                                  'Да',
                                      'Нет'],
                              width=12,
                              justify='center')
    comboPhoto.place(x=600, y=0)
    comboPhoto.current(0)

    button = tk.Button(windows, text="КНОПКА ДЛЯ ТЕСТОВ!НЕ ТРОГАТЬ ",
    command=showbutton)
    button.place(x=300, y=180)

    prod_id = StringVar()
    prod_id_field = Entry(windows, textvariable=prod_id )
    prod_id_field.place(x=0, y=0)



def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)


def LoadFile(2):
    ftypes = [('Все файлы', '*'), ('Текстовые файлы TXT ', '*.txt'), ('Файлы Python', '*.py'),
              ('HTML документ', '*.html')]  # Фильтр файлов
    fn = tk.filedialog.Open(app, filetypes=ftypes).show()
    print(fn)
    if fn == '':
        return
    text.delete('1.0', 'end')  # Очищаем окно редактирования
    text.insert('1.0', open(fn, encoding='utf-8', mode='r').read())  # Вставляем текст в окно редактирования

    global cur_path
    cur_path = fn  # Храним путь к открытому файлу

def SaveFile():
    ftypes = [('Все файлы', '*'), ('Текстовые файлы TXT ', '*.txt'), ('Файлы Python', '*.py'),
              ('HTML документ', '*.html')]  # Фильтр файлов
    #fn = tk.filedialog.asksaveasfilename(name="ttt")
    fn = tk.filedialog.asksaveasfilename(initialfile="Новый документ", defaultextension='.txt', filetypes=ftypes)
    if fn == '':
        return
    open(fn, encoding='utf-8', mode='wt').write(text.get('1.0', 'end'))


app = tk.Tk()
app.title("Python resize tool")
app.geometry('663x600+500+250')
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

button = tk.Button(app, text="КНОПКА ДЛЯ ТЕСТОВ!НЕ ТРОГАТЬ ",
             command=db_window)
button.place(x=0, y=550)



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
folder_button = PhotoImage(file='folder_button.png')

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
lbl3.place(x=427, y=345)

lbl4 = Label(master=app,text='в CSV таблицу:')
lbl4.place(x=427, y=365)

lbl5 = Label(master=app,text='В текстовом поле можно создавать и редактировать заметки:', font="16")
lbl5.place(x=10, y=80)

lbl6 = Label(master=app,text='В меню обработки изображений доступны функции:', font="16")
lbl6.place(x=10, y=317)

lbl7_text ='Добро пожаловать! Вы изпользуете PYRT, приложение предназначено для массовых манипуляций с файлами изображений'
lbl7 = Label(master=app,text=lbl7_text)
lbl7.place(x=170, y=15)

#button2 = Button(text="Обзор", command=browse_button, highlightcolor="red")
#button2.place(x=132, y=180)

app.update()

width = lbl7.winfo_width()
row = 500
if width > row:
    char_width = width / len(lbl7_text)
    wrapped_text = '\n'.join(wrap(lbl7_text, int(row / char_width)))
    lbl7['text'] = wrapped_text


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
button9.place(x=531, y=550)

button10 = Button(app, image=folder_button, command=lambda: print('Sort files'), bd=1, activebackground='LightCyan2')
button10.place(x=531, y=400)

text = Text(width=80, height=10, bg="azure")
text.place(x=10, y=100)

instruktionBtn = Button(app, text='Открыть заметку', command=LoadFile, bd=1, activebackground='LightCyan2', bg="mint cream")
instruktionBtn.place(x=10, y=270)

instruktionBtn = Button(app, text='Сохранить заметку', command=SaveFile, bd=1, activebackground='LightCyan2', bg="mint cream")
instruktionBtn.place(x=120, y=270)

app.mainloop()






