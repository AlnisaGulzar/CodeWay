import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry widget to input numbers
        self.entry = tk.Entry(root, width=20, font=("Helvetica", 14), bd=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create buttons dynamically
        row_val, col_val = 1, 0
        for button in buttons:
            tk.Button(root, text=button, command=lambda b=button: self.on_button_click(b),
                      width=5, height=2, font=("Helvetica", 12)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current_entry_text = self.entry.get()

        if button == '=':
            try:
                result = eval(current_entry_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'C':
            self.entry.delete(0, tk.END)

        else:
            self.entry.insert(tk.END, button)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
