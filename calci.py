import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.expression = ""
        
        self.input_text = tk.StringVar()
        
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()
        
        self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=30, insertwidth=4, width=14, borderwidth=4)
        self.input_field.grid(row=0, column=0)
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'sqrt',
            '1', '2', '3', '-', '^',
            '0', '.', '=', '+', 'M+'
        ]
        
        row_val = 0
        col_val = 0
        
        for button in buttons:
            action = lambda x=button: self.click(x)
            tk.Button(self.button_frame, text=button, padx=20, pady=20, font=('arial', 18, 'bold'), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def click(self, button):
        if button == 'C':
            self.expression = ""
            self.input_text.set(self.expression)
        elif button == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.input_text.set(self.expression)
        elif button == 'sqrt':
            try:
                result = str(math.sqrt(eval(self.expression)))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.input_text.set(self.expression)
        elif button == '^':
            self.expression += '**'
            self.input_text.set(self.expression)
        elif button == 'M+':
            try:
                self.memory = eval(self.expression)
                self.expression = ""
                self.input_text.set(self.expression)
                messagebox.showinfo("Memory", f"Stored {self.memory} in memory")
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.input_text.set(self.expression)
        else:
            self.expression += str(button)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
