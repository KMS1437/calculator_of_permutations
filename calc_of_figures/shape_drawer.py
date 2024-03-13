import tkinter as tk
from tkinter import ttk

class ShapeDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Геометрические фигуры")

        style = ttk.Style()
        style.theme_settings("default", {
            "TCombobox": {
                "configure": {"padding": 5},
                "map": {
                    "background": [("active", "green2"), ("!disabled", "green4")],
                    "fieldbackground": [("!disabled", "green3")],
                    "foreground": [("focus", "OliveDrab1"), ("!disabled", "OliveDrab2")]
                }
            }
        })

        self.root.configure(background='lightgrey')

        self.shape_choice = tk.StringVar()
        self.color_choice = tk.StringVar()

        self.shape_label = tk.Label(self.root, text="Выберите тип фигуры:")
        self.shape_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.shape_menu = ttk.Combobox(self.root, textvariable=self.shape_choice, values=["Круг", "Квадрат", "Треугольник"])
        self.shape_menu.grid(row=0, column=1, padx=10, pady=10)

        self.color_label = tk.Label(self.root, text="Выберите цвет фигуры:")
        self.color_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.color_menu = ttk.Combobox(self.root, textvariable=self.color_choice, values=["красный", "синий", "зеленый"])
        self.color_menu.grid(row=1, column=1, padx=10, pady=10)

        self.size_label = tk.Label(self.root, text="Введите размер стороны:")
        self.size_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.size_entry = tk.Entry(self.root)
        self.size_entry.grid(row=2, column=1, padx=10, pady=10)

        self.draw_button = tk.Button(self.root, text="Нарисовать", command=self.draw_shape)
        self.draw_button.grid(row=3, columnspan=2, padx=10, pady=10)

    def draw_shape(self):
        shape = self.shape_choice.get()
        color = self.color_choice.get()
        size = self.size_entry.get()

        if shape not in ["Круг", "Квадрат", "Треугольник"]:
            self.show_error_message("Выберите правильную фигуру: Круг, Квадрат или Треугольник")
            return

        if color not in ["красный", "синий", "зеленый"]:
            self.show_error_message("Выберите правильный цвет: красный, синий или зеленый")
            return

        if not size.isdigit():
            self.show_error_message("Размер стороны должен быть целым числом")
            return

        size = int(size)

        shape_window = tk.Toplevel(self.root)
        shape_window.title("Нарисованная фигура")

        canvas = tk.Canvas(shape_window, width=1080, height=720)
        canvas.pack()

        if color == "красный":
            color = "red"
        elif color == "синий":
            color = "blue"
        elif color == "зеленый":
            color = "green"

        if shape == "Круг":
            canvas.create_oval(540-size//2, 360-size//2,
540+size//2, 360+size//2, fill=color)
        elif shape == "Квадрат":
            canvas.create_rectangle(540-size//2, 360-size//2, 540+size//2, 360+size//2, fill=color)
        elif shape == "Треугольник":
            canvas.create_polygon(540, 360-size//2, 540+size//2, 360+size//2, 540-size//2, 360+size//2, fill=color)

    def show_error_message(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Ошибка")
        error_label = tk.Label(error_window, text=message)
        error_label.pack()

root = tk.Tk()
app = ShapeDrawer(root)
root.mainloop()
