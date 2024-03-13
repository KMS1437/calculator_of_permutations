import tkinter as tk
from tkinter import messagebox
from math import factorial
from tkinter import ttk


def calc_permutations():
    nums = entry_n.get()
    lst = nums.split()
    long = len(lst)
    messagebox.showinfo("Результат", f"{factorial(long)}")


def calc_combinations():
    n = int(entry_n.get())
    k = int(entry_k.get())
    messagebox.showinfo("Результат", f"{factorial(n) / factorial(n - k)}")


def calc_placement():
    n = int(entry_n.get())
    k = int(entry_k.get())
    messagebox.showinfo("Результат", f"{factorial(n) / (factorial(n - k) * factorial(k))}")


root = tk.Tk()
root.title("Калькулятор комбинаторики")
root.geometry("350x300")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12))

frame = tk.Frame(root)
frame.pack(expand=True)


btn_permutations = ttk.Button(frame, text="Вычислить перестановки", command=calc_permutations)
btn_permutations.pack(pady=10)

btn_combinations = ttk.Button(frame, text="Вычислить сочетания", command=calc_combinations)
btn_combinations.pack(pady=10)

btn_arrangements = ttk.Button(frame, text="Вычислить размещения", command=calc_placement)
btn_arrangements.pack(pady=10)

label_n = tk.Label(frame, text="Введите n:")
label_n.pack()
entry_n = tk.Entry(frame)
entry_n.pack()

label_k = tk.Label(frame, text="Введите k:")
label_k.pack()
entry_k = tk.Entry(frame)
entry_k.pack()

frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
