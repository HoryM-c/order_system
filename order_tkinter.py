from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

class Menu():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f'{self.name}：¥{self.price}'

    def food_name(self):
        return self.name

    def food_price(self):
        return self.price
#Comboboxの生成
def combobox_create():
    combo_box = ttk.Combobox(main_frame3, state = 'readonly', values = vlist, width = 5, justify = RIGHT, style = 'MyWidget.TCombobox')
    return combo_box
#food_labelの作成
def food_label_create(number):
    food_label = ttk.Label(main_frame2, text = number.info(), style = 'MyWidget.TLabel', justify = LEFT)
    return food_label
        
food1 = Menu('サンドイッチ', 500)
food2 = Menu('チョコケーキ', 400)
food3 = Menu('シュークリーム', 200)

foods = [food1, food2, food3]
food_names = [food.food_name() for food in foods]
food_prices = [food.food_price() for food in foods]
menu_prices = dict(zip(food_names, food_prices))

def order_button_click():
    final_info = []
    final_price = 0
    counts = [var.get() for var in combo_list]
    for count, value in enumerate(food_names):
        if counts[count] == '個数':
            counts[count] = '0'
        total_price = menu_prices.get(value) * int(counts[count])
        final_price += total_price
        info_message = ('{0}の注文が{1}個、金額は{2}です。'.format(value, counts[count], total_price))
        if int(counts[count]) != 0:
            final_info.append(info_message)
    message_text = ''
    
    for message in final_info:
        if final_info.index(message) == 0:
            message_text = message
        else:
            message_text += '\n' + message
    if message_text == '':
        mb.showinfo('困りました', '注文されませんでした。')
    else:
        mb.showinfo('ご注文内容を確認します', message_text + f'\n合計は{str(final_price)}円です。')

#ウィンドウを作成
win = Tk()
win.title('☆注文システム☆')
win.geometry('300x250')
#スタイルを作成
s = ttk.Style()
s.theme_use('default')
s.configure('MyWidget.TFrame', relief = RIDGE, background = '#FFFFFF', ipadx = 10, ipady = 10)
s.configure('MyWidget2.TFrame', background = '#FFFFFF', padx = 10, pady = 10)
s.configure('MyWidget.TLabel', background = '#FFFFFF')
s.configure('MyWidget.TCombobox', background = '#FFFFFF')
#ヘッダーフレーム
top_frame = ttk.Frame(win)
top_frame.pack(pady = 10)
#メインフレーム
main_frame = ttk.Frame(win, style = 'MyWidget.TFrame')
main_frame.pack(ipadx = 10, ipady = 10)
main_frame2 = ttk.Frame(main_frame, style = 'MyWidget2.TFrame')
main_frame2.grid(row = 0, column = 0, padx = 10, pady = 10)
main_frame3 = ttk.Frame(main_frame, style = 'MyWidget2.TFrame')
main_frame3.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = E)
#サブフレーム
sub_frame = ttk.Frame(win,relief = RAISED)
sub_frame.pack(pady = 20)
#ラベルの作成
info_label = ttk.Label(top_frame, text = '商品を選んでください', style = 'MyWidget.TLabel')
info_label.pack()
food1_label = food_label_create(food1)
food2_label = food_label_create(food2)
food3_label = food_label_create(food3)
food1_label.grid(column = 0, row = 0, sticky = W, pady = 5)
food2_label.grid(column = 0, row = 1, sticky = W)
food3_label.grid(column = 0, row = 2, sticky = W, pady = 5)
#Comboboxの生成
vlist = [i for i in range(0,11)]
Combo1 = combobox_create()
Combo2 = combobox_create()
Combo3 = combobox_create()
combo_list = [Combo1, Combo2, Combo3]
for combo in combo_list:
    combo.set('個数')
Combo1.grid(row = 0, column = 1, sticky = E, pady = 5)
Combo2.grid(row = 1, column = 1, sticky = E)
Combo3.grid(row = 2, column = 1, sticky = E, pady = 5)
#ボタンの作成
order_button = ttk.Button(sub_frame, text = '◎注文◎', command = order_button_click)
order_button.pack()

win.mainloop()