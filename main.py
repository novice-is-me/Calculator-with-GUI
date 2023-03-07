# Calculator with GUI tkinter

# ---------------------------
# SIMPLE CALCULATOR WITH GUI
# ---------------------------

# open for comments and suggestions
import tkinter as tk
from tkinter import *

# interface
root = Tk()
root.geometry("400x460")
root.config(bg="sky blue")
root.resizable(False, False)

# title of interface
root.title("CALCULATOR")

title = tk.Label(text="CALCULATOR X", font=("Times", 12, "bold"))
title.place(x=5, y=4)

# for displaying num
text_num = tk.Text(root, width="30", heigh="3", font=("Helvetica", 15, "bold"))
text_num.place(x=40, y=45)


# for calculating operations
def equals():
    expressions = text_num.get("1.0", END)
    result = str(eval(expressions))
    text_num.delete("1.0", END)
    text_num.insert("1.0", result)


def clear():
    text_num.delete("1.0", "end")


# for deleting last character
def delete():
    character = text_num.get("1.0", END)
    new_text = character[:-2]
    text_num.delete("1.0", END)
    text_num.insert("1.0", new_text)


def button_show(button):
    number = button["text"]
    text_num.insert(tk.END, number)


# for number's button
button = tk.Button(root, text="  ", width="10", height="2")
button.place(x=20, y=150)

button_percent = tk.Button(root, text="%", width="10", height="2")
button_percent.config(command=lambda: button_show(button_percent))
button_percent.place(x=110, y=150)

button_clear = tk.Button(root, text="C", width="10", height="2", command=clear)
button_clear.place(x=200, y=150)

button_X = tk.Button(root, text="Del", width="10", height="2", command=delete)
button_X.place(x=295, y=150)

button7 = tk.Button(root, text="7", width="10", height="2")
button7.config(command=lambda: button_show(button7))
button7.place(x=20, y=210)

button8 = tk.Button(root, text="8", width="10", height="2")
button8.config(command=lambda: button_show(button8))
button8.place(x=110, y=210)

button9 = tk.Button(root, text="9", width="10", height="2")
button9.config(command=lambda: button_show(button9))
button9.place(x=200, y=210)

button_divide = tk.Button(root, text="/", width="10", height="2")
button_divide.config(command=lambda: button_show(button_divide))
button_divide.place(x=295, y=210)

button4 = tk.Button(root, text="4", width="10", height="2")
button4.config(command=lambda: button_show(button4))
button4.place(x=20, y=270)

button5 = tk.Button(root, text="5", width="10", height="2")
button5.config(command=lambda: button_show(button5))
button5.place(x=110, y=270)

button6 = tk.Button(root, text="6", width="10", height="2")
button6.config(command=lambda: button_show(button6))
button6.place(x=200, y=270)

button_times = tk.Button(root, text="*", width="10", height="2")
button_times.config(command=lambda: button_show(button_times))
button_times.place(x=295, y=270)

button1 = tk.Button(root, text="1", width="10", height="2")
button1.config(command=lambda: button_show(button1))
button1.place(x=20, y=330)

button2 = tk.Button(root, text="2", width="10", height="2")
button2.config(command=lambda: button_show(button2))
button2.place(x=110, y=330)

button3 = tk.Button(root, text="3", width="10", height="2")
button3.config(command=lambda: button_show(button3))
button3.place(x=200, y=330)

button_minus = tk.Button(root, text="-", width="10", height="2")
button_minus.config(command=lambda: button_show(button_minus))
button_minus.place(x=295, y=330)

button_dot = tk.Button(root, text=".", width="10", height="2")
button_dot.config(command=lambda: button_show(button_dot))
button_dot.place(x=20, y=390)

button0 = tk.Button(root, text="0", width="10", height="2")
button0.config(command=lambda: button_show(button0))
button0.place(x=110, y=390)

button_equal = tk.Button(root, text="=", width="10", height="2", command=equals)
button_equal.place(x=200, y=390)

button_add = tk.Button(root, text="+", width="10", height="2")
button_add.config(command=lambda: button_show(button_add))
button_add.place(x=295, y=390)

root.mainloop()
