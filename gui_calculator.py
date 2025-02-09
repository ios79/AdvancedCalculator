import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator - By Ioseb Vardoshvili")  # ✅ Branding in the title
        self.root.geometry("400x550")

        self.expression = ""
        self.last_result = "0"
        self.dark_mode = False  # Default to Light Mode

        # Entry Widget for Display
        self.entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, sticky="nsew")

        # Watermark in the Entry Field ✅
        self.entry.insert(0, "By Ioseb Vardoshvili")  
        self.entry.bind("<FocusIn>", self.clear_watermark)  

        # Button Layout
        buttons = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "C", "+"),
            ("sqrt", "sin", "cos", "tan"),
            ("log", "exp", "pi", "^"),
            ("(", ")", "ans", "=")
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                self.create_button(text, r + 1, c)

        # Toggle Dark Mode Button ✅
        self.toggle_btn = tk.Button(root, text="Toggle Dark Mode", font=("Arial", 14), command=self.toggle_dark_mode)
        self.toggle_btn.grid(row=len(buttons) + 1, column=0, columnspan=4, ipadx=10, ipady=5, sticky="nsew")

        # About Button ✅
        self.about_btn = tk.Button(root, text="About", font=("Arial", 14), command=self.show_about)
        self.about_btn.grid(row=len(buttons) + 2, column=0, columnspan=4, ipadx=10, ipady=5, sticky="nsew")

        # Credit Label at the Bottom ✅
        self.credit_label = tk.Label(root, text="Created by Ioseb Vardoshvili", font=("Arial", 12, "italic"))
        self.credit_label.grid(row=len(buttons) + 3, column=0, columnspan=4, sticky="nsew")

        # Expand rows & columns for resizing
        for i in range(len(buttons) + 4):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

        self.apply_theme()

    def create_button(self, text, row, col):
        btn = tk.Button(self.root, text=text, font=("Arial", 18), command=lambda: self.on_button_click(text))
        btn.grid(row=row, column=col, ipadx=10, ipady=10, sticky="nsew")
        btn.configure(bg=self.get_button_color(), fg=self.get_text_color())

    def on_button_click(self, char):
        if char == "=":
            self.evaluate_expression()
        elif char == "C":
            self.expression = ""
            self.entry.delete(0, tk.END)
        else:
            if char == "^":
                char = "**"
            elif char == "pi":
                char = str(math.pi)
            elif char == "ans":
                char = self.last_result
            self.expression += char
            self.entry.insert(tk.END, char)

    def evaluate_expression(self):
        try:
            result = eval(self.expression, {"__builtins__": None}, {
                "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan,
                "log": math.log, "exp": math.exp, "pi": math.pi, "e": math.e
            })
            self.last_result = str(result)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
            self.expression = str(result)
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            self.expression = ""

    def toggle_dark_mode(self):
        """Toggles between Light and Dark mode"""
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        """Applies the current theme (Light or Dark)"""
        bg_color = "#1e1e1e" if self.dark_mode else "#ffffff"  # Background color
        text_color = "#ffffff" if self.dark_mode else "#000000"  # Text color
        btn_color = "#333333" if self.dark_mode else "#f0f0f0"  # Button color

        self.root.configure(bg=bg_color)
        self.entry.configure(bg=bg_color, fg=text_color, insertbackground=text_color)

        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) or isinstance(widget, tk.Label):
                widget.configure(bg=btn_color, fg=text_color)

    def get_button_color(self):
        return "#333333" if self.dark_mode else "#f0f0f0"

    def get_text_color(self):
        return "#ffffff" if self.dark_mode else "#000000"

    def show_about(self):
        """Opens a pop-up window with information about the calculator"""
        about_window = tk.Toplevel(self.root)
        about_window.title("About")
        about_window.geometry("300x150")

        label = tk.Label(about_window, text="Advanced Calculator\nCreated by Ioseb Vardoshvili", 
                         font=("Arial", 14), pady=20)
        label.pack()

        close_btn = tk.Button(about_window, text="Close", font=("Arial", 12), command=about_window.destroy)
        close_btn.pack(pady=10)

    def clear_watermark(self, event):
        """Removes the watermark when the user starts typing"""
        if self.entry.get() == "By Ioseb Vardoshvili":
            self.entry.delete(0, tk.END)


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
