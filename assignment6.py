import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        input_field = tk.Entry(self.input_frame, font=('arial', 18), textvariable=self.input_text, width=28, bd=5, insertwidth=2, borderwidth=4)
        input_field.grid(row=0, column=0, columnspan=4)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 4)
        ]

        for (text, row, col, colspan) in [(*btn, 1) if len(btn) == 3 else btn for btn in buttons]:
            tk.Button(
                self.button_frame,
                text=text,
                padx=20,
                pady=20,
                bd=4,
                font=('arial', 14),
                command=lambda t=text: self.on_button_click(t)
            ).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.input_text.set("")
                self.expression = ""
        elif char == "C":
            self.input_text.set("")
            self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
