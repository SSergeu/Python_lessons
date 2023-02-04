from tkinter import *
from tkinter import ttk
import view 
import model 

def output_ever_click():
    view.output_guide(model.open_guide_dict(in_entry_patch()))

def but_new_enrty_click():
    new_data = entry.get()
    model.add(in_entry_patch(), new_data)

def in_entry_patch():
    path = entry_patch.get()
    return path

def start():
    global entry
    global entry_patch

    window = Tk()
    window.title('Телефонный справочник')
    frm = ttk.Frame(window, padding=30)
    frm.grid()  
        
    patch_lable = ttk.Label(frm, text = 'Введите путь к справочнику: ')
    patch_lable.grid(row=0,column=0)

    dop_info = ttk.Label(frm, text='Например: guide.txt')
    dop_info.grid(row=0,column=2)
    
    button_new_entry = ttk.Button(frm, text='Добавить запись', width=20, command=but_new_enrty_click)
    button_new_entry.grid(row=1, column=1)

    output_everything = ttk.Button(frm, text = 'Вывод всего справочника', width=26, command=output_ever_click)
    output_everything.grid(row=2, column=0)

    entry = ttk.Entry(frm, width=26)
    entry.grid(row=1, column=0)

    entry_patch = ttk.Entry(frm)
    entry_patch.grid(row=0,column=1)
       
    window.mainloop()   


start()