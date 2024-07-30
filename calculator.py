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

def add_to_expression(symbol):
    current_text = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(0, current_text + str(symbol))

def clear_input():
    entry_field.delete(0, tk.END)
    result_label.config(text="")

def create_button(text, command, row, col, colspan=1, rowspan=1):
    button = ttk.Button(window, text=text, command=command, style="TButton")
    button.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, padx=5, pady=5)

window = tk.Tk()
window.title("GUI Calculator")
window.geometry("320x460")


entry_field = tk.Entry(window, justify='right', font=('Arial', 20), bg="#3C4043", fg="white")
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

result_label = tk.Label(window, text="", pady=10,font=('Arial', 16))
result_label.grid(row=1, column=0, columnspan=4)

style = ttk.Style()
style.configure('TButton', font=('Arial', 14))
style.map('TButton')

# Clear and operation buttons
create_button("C", clear_input, 2, 0)
create_button("/", lambda: add_to_expression('/'), 2, 1)
create_button("*", lambda: add_to_expression('*'), 2, 2)
create_button("-", lambda: add_to_expression('-'), 2, 3)

# Number buttons
create_button("7", lambda: add_to_expression(7), 3, 0)
create_button("8", lambda: add_to_expression(8), 3, 1)
create_button("9", lambda: add_to_expression(9), 3, 2)
create_button("+", lambda: add_to_expression('+'), 3, 3)

create_button("4", lambda: add_to_expression(4), 4, 0)
create_button("5", lambda: add_to_expression(5), 4, 1)
create_button("6", lambda: add_to_expression(6), 4, 2)

create_button("1", lambda: add_to_expression(1), 5, 0)
create_button("2", lambda: add_to_expression(2), 5, 1)
create_button("3", lambda: add_to_expression(3), 5, 2)

create_button("0", lambda: add_to_expression(0), 6, 0, colspan=2)
create_button(".", lambda: add_to_expression('.'), 6, 2)

# Equals button
create_button("=", calculation, 4, 3, rowspan=3)

for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(7):
    window.rowconfigure(i, weight=1)

window.mainloop()