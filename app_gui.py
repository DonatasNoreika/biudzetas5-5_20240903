from biudzetas import Biudzetas
from tkinter import *
from tkinter import ttk

biudzetas = Biudzetas()

window = Tk()
window.geometry("480x470")
window.title("Mano biudžetas")

income_frame = Frame(window)
expense_frame = Frame(window)
list_frame = Frame(window)
balance_frame = Frame(window)

# functions
def enter_income():
    suma = int(inc_sum_entry.get())
    siuntejas = inc_siunt_entry.get()
    info = inc_info_entry.get()
    biudzetas.prideti_pajamu_irasa(suma, siuntejas, info)
    update_windows()
    inc_sum_entry.focus()

def enter_expense():
    suma = int(exp_sum_entry.get())
    atsiskaitymas = exp_ats_entry.get()
    isigyta = exp_isig_entry.get()
    biudzetas.prideti_islaidu_irasa(suma, atsiskaitymas, isigyta)
    update_windows()
    exp_sum_entry.focus()

def update_windows():
    inc_sum_entry.delete(0, END)
    inc_siunt_entry.delete(0, END)
    inc_info_entry.delete(0, END)
    exp_sum_entry.delete(0, END)
    exp_ats_entry.delete(0, END)
    exp_isig_entry.delete(0, END)
    mylist.delete(0, END)
    mylist.insert(0, *biudzetas.zurnalas[::-1])
    balance_label["text"] = f"BALANSAS: {biudzetas.gauti_balansa()}"


# objects

income_title = Label(income_frame, text="Įveskite pajamas:")
inc_sum_label = Label(income_frame, text="Suma:")
inc_sum_entry = Entry(income_frame)
inc_siunt_label = Label(income_frame, text="Siuntėjas:")
inc_siunt_entry = Entry(income_frame)
inc_info_label = Label(income_frame, text="Info:")
inc_info_entry = Entry(income_frame)
inc_button = Button(income_frame, text="Įvesti", command=enter_income)

separator1 = ttk.Separator(income_frame, orient='horizontal')

expense_title = Label(expense_frame, text="Įveskite išlaidas:")
exp_sum_label = Label(expense_frame, text="Suma:")
exp_sum_entry = Entry(expense_frame)
exp_ats_label = Label(expense_frame, text="Atsiskaitymo būdas:")
exp_ats_entry = Entry(expense_frame)
exp_isig_label = Label(expense_frame, text="Įsigyta prekė/paslauga:")
exp_isig_entry = Entry(expense_frame)
exp_button = Button(expense_frame, text="Įvesti", command=enter_expense)

separator2 = ttk.Separator(expense_frame, orient='horizontal')

balance_label = Label(balance_frame, text=f"BALANSAS: {biudzetas.gauti_balansa()}", fg="blue")


mylist = Listbox(list_frame, width=70)
mylist.insert(0, *biudzetas.zurnalas[::-1])

# packing

income_frame.pack()
expense_frame.pack()
balance_frame.pack()
list_frame.pack()

income_title.grid(row=0, columnspan=2)
inc_sum_label.grid(row=1, column=0)
inc_sum_entry.grid(row=1, column=1)
inc_siunt_label.grid(row=2, column=0)
inc_siunt_entry.grid(row=2, column=1)
inc_info_label.grid(row=3, column=0)
inc_info_entry.grid(row=3, column=1)
inc_button.grid(row=4, columnspan=2)

separator1.grid(row=5, columnspan=2, pady=10)

expense_title.grid(row=0, columnspan=2)
exp_sum_label.grid(row=1, column=0)
exp_sum_entry.grid(row=1, column=1)
exp_ats_label.grid(row=2, column=0)
exp_ats_entry.grid(row=2, column=1)
exp_isig_label.grid(row=3, column=0)
exp_isig_entry.grid(row=3, column=1)
exp_button.grid(row=4, columnspan=2)

separator2.grid(row=5, columnspan=2, pady=10)

balance_label.pack()

mylist.pack()
window.mainloop()