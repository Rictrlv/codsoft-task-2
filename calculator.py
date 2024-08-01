import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculation():
    try:
        expression = entryfield.get()
        result = eval(expression)
        resultlabel.config(text=f"{result}")
    except Exception as error:
        messagebox.showerror("Error", f"Invalid input: {error}")

def addtoexpression(symbol):
    currenttext = entryfield.get()
    entryfield.delete(0, tk.END)
    entryfield.insert(0, currenttext + str(symbol))

def clearinput():
    entryfield.delete(0, tk.END)
    resultlabel.config(text="")

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


createbutton("C", clearinput, 2, 0)
createbutton("/", lambda: addtoexpression('/'), 2, 1)
createbutton("*", lambda: addtoexpression('*'), 2, 2)
createbutton("-", lambda: addtoexpression('-'), 2, 3)

createbutton("7", lambda: addtoexpression(7), 3, 0)
createbutton("8", lambda: addtoexpression(8), 3, 1)
createbutton("9", lambda: addtoexpression(9), 3, 2)
createbutton("+", lambda: addtoexpression('+'), 3, 3)

createbutton("4", lambda: addtoexpression(4), 4, 0)
createbutton("5", lambda: addtoexpression(5), 4, 1)
createbutton("6", lambda: addtoexpression(6), 4, 2)

createbutton("1", lambda: addtoexpression(1), 5, 0)
createbutton("2", lambda: addtoexpression(2), 5, 1)
createbutton("3", lambda: addtoexpression(3), 5, 2)

createbutton("0", lambda: addtoexpression(0), 6, 0, colspan=2)
createbutton(".", lambda: addtoexpression('.'), 6, 2)

createbutton("=", calculation, 4, 3, rowspan=3)

for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(7):
    window.rowconfigure(i, weight=1)

window.mainloop()
