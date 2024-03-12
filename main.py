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
root.geometry("400x300")

label_n = tk.Label(root, text="Введите n:")
label_n.pack()
entry_n = tk.Entry(root)
entry_n.pack()

label_k = tk.Label(root, text="Введите k:")
label_k.pack()
entry_k = tk.Entry(root)
entry_k.pack()

style = ttk.Style()
style.configure("TButton", font=("Arial", 12))

btn_permutations = ttk.Button(root, text="Вычислить перестановки", command=calc_permutations)
btn_permutations.pack()

btn_combinations = ttk.Button(root, text="Вычислить сочетания", command=calc_combinations)
btn_combinations.pack()

btn_arrangements = ttk.Button(root, text="Вычислить размещения", command=calc_placement)
btn_arrangements.pack()

root.mainloop()
