import tkinter as tk
from tkinter import messagebox


def say_hello():
    messagebox.showinfo("Hello", "Hello World")


root = tk.Tk()
root.title("Hello App")

button = tk.Button(root, text="Click me", command=say_hello)
button.pack(padx=20, pady=20)

root.mainloop()
