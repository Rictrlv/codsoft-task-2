import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculation():
    try:
        expression = entry_field.get()
        result = eval(expression)
        result_label.config(text=f"{result}")
    except Exception as error:
        messagebox.showerror("Error", f"Invalid input: {error}")

def addtoexpression(symbol):
    current_text = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(0, current_text + str(symbol))

def clearinput():
    entry_field.delete(0, tk.END)
    result_label.config(text="")

def createbutton(text, command, row, col, colspan=1, rowspan=1):
    button = ttk.Button(window, text=text, command=command, style="TButton")
    button.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, padx=5, pady=5)

window = tk.Tk()
window.title("GUI Calculator")
window.geometry("320x460")


entryfield = tk.Entry(window, justify='right', font=('Arial', 20), bg="#3C4043", fg="white")
entryfield.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

resultlabel = tk.Label(window, text="", pady=10,font=('Arial', 16))
resultlabel.grid(row=1, column=0, columnspan=4)

style = ttk.Style()
style.configure('TButton', font=('Arial', 14))
style.map('TButton')


create_button("C", clear_input, 2, 0)
create_button("/", lambda: addtoexpression('/'), 2, 1)
create_button("*", lambda: addtoexpression('*'), 2, 2)
create_button("-", lambda: addtoexpression('-'), 2, 3)

create_button("7", lambda: addtoexpression(7), 3, 0)
create_button("8", lambda: addtoexpression(8), 3, 1)
create_button("9", lambda: addtoexpression(9), 3, 2)
create_button("+", lambda: addtoexpression('+'), 3, 3)

create_button("4", lambda: addtoexpression(4), 4, 0)
create_button("5", lambda: addtoexpression(5), 4, 1)
create_button("6", lambda: addtoexpression(6), 4, 2)

create_button("1", lambda: addtoexpression(1), 5, 0)
create_button("2", lambda: addtoexpression(2), 5, 1)
create_button("3", lambda: addtoexpression(3), 5, 2)

create_button("0", lambda: addtoexpression(0), 6, 0, colspan=2)
create_button(".", lambda: addtoexpression('.'), 6, 2)

create_button("=", calculation, 4, 3, rowspan=3)

for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(7):
    window.rowconfigure(i, weight=1)

window.mainloop()
