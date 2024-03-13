import tkinter as tk
from tkinter import ttk, messagebox
from math import factorial

root = tk.Tk()
root.title("Калькулятор комбинаторики")
root.geometry("350x400")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12))

frame = tk.Frame(root)
frame.pack(expand=True)


def create_entry(text):
    label = tk.Label(frame, text=text)
    label.pack()
    entry = tk.Entry(frame)
    entry.pack()
    return entry


entry_n = create_entry("Введите n:")
entry_k = create_entry("Введите k:")


def calc_permutations():
    n = entry_n.get()
    result = factorial(len(n.split()))
    messagebox.showinfo("Результат", f"{result}")


def calc_permutations_with_repeat():
    n = entry_n.get()
    result = 1
    for num in n:
        result *= factorial(num)
    messagebox.showinfo("Результат", f"{result}")


def calc_combinations():
    n = int(entry_n.get())
    k = int(entry_k.get())
    result = factorial(n) // (factorial(k) * factorial(n - k))
    messagebox.showinfo("Результат", f"{result}")


def calc_combinations_with_repeat():
    n = int(entry_n.get())
    k = int(entry_k.get())
    result = factorial(n + k - 1) // (factorial(k) * factorial(n - 1))
    messagebox.showinfo("Результат", f"{result}")


def calc_arrangements():
    n = int(entry_n.get())
    k = int(entry_k.get())
    result = factorial(n) // factorial(n - k)
    messagebox.showinfo("Результат", f"{result}")


def calc_arrangements_with_repeat():
    n = int(entry_n.get())
    k = int(entry_k.get())
    result = n ** k
    messagebox.showinfo("Результат", f"{result}")


btn_permutations = ttk.Button(frame, text="Вычислить перестановки", command=calc_permutations)
btn_permutations.pack(pady=10)

btn_permutations = ttk.Button(frame, text="Вычислить перестановки с повторениями", command=calc_permutations)
btn_permutations.pack(pady=10)

btn_combinations = ttk.Button(frame, text="Вычислить сочетания", command=calc_combinations_with_repeat)
btn_combinations.pack(pady=10)

btn_combinations = ttk.Button(frame, text="Вычислить сочетания с повторениями", command=calc_combinations_with_repeat)
btn_combinations.pack(pady=10)

btn_arrangements = ttk.Button(frame, text="Вычислить размещения", command=calc_arrangements)
btn_arrangements.pack(pady=10)

btn_arrangements = ttk.Button(frame, text="Вычислить размещения с повторениями", command=calc_arrangements_with_repeat)
btn_arrangements.pack(pady=10)

frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
root.mainloop()
