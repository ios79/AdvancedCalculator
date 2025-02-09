import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator - By Ioseb Vardoshvili")  
        self.root.geometry("400x550")

        self.expression = ""  # Stores user input
        self.last_result = "0"
        self.dark_mode = False  # Default Light Mode

        # Entry Widget for Display (Now Accepts Keyboard Input)
        self.entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, sticky="nsew")

        # ✅ Fix: Enable full keyboard support
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<Return>", self.on_enter_key)
        self.root.bind("<BackSpace>", self.on_backspace)

        # Button Layout
        buttons = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "C", "+"),  # ✅ "C" Button added
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

        # Credit Label ✅
        self.credit_label = tk.Label(root, text="Created by Ioseb Vardoshvili", font=("Arial", 12, "italic"))
        self.credit_label.grid(row=len(buttons) + 3, column=0, columnspan=4, sticky="nsew")

        # Grid Configuration for Resizing
        for i in range(len(buttons) + 4):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

        self.apply_theme()

    def create_button(self, text, row, col):
        """Creates buttons dynamically and applies the theme"""
        btn = tk.Button(self.root, text=text, font=("Arial", 18), command=lambda: self.on_button_click(text))
        btn.grid(row=row, column=col, ipadx=10, ipady=10, sticky="nsew")
        btn.configure(bg=self.get_button_color(), fg=self.get_text_color())

        # Add hover effect
        btn.bind("<Enter>", lambda e: btn.config(bg="gray"))
        btn.bind("<Leave>", lambda e: btn.config(bg=self.get_button_color()))

    def on_button_click(self, char):
        """Handles button press"""
        if char == "=":
            self.evaluate_expression()
        elif char == "C":  # ✅ Clear screen button support
            self.clear_screen()
        else:
            if char == "^":
                char = "**"
            elif char == "pi":
                char = str(math.pi)
            elif char == "ans":
                char = self.last_result

            self.expression += str(char)
            self.entry.delete(0, tk.END)  
            self.entry.insert(tk.END, self.expression)

    def on_key_press(self, event):
        """Handles keyboard input for numbers, operators, and clear screen"""
        key = event.char
        allowed_chars = "0123456789+-*/().^"

        if key in allowed_chars:
            self.expression += key
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)
        elif key.lower() == "c":  # ✅ Typing "C" clears screen
            self.clear_screen()
        elif key == "\r":  # ✅ Enter key (same as "=" button)
            self.evaluate_expression()

    def on_backspace(self, event):
        """Handles Backspace key press"""
        self.expression = self.expression[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def on_enter_key(self, event):
        """Handles 'Enter' key press (same as clicking '=')"""
        self.evaluate_expression()

    def evaluate_expression(self):
        """Evaluates the current expression"""
        try:
            safe_dict = {
                "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan,
                "log": math.log, "exp": math.exp, "pi": math.pi, "e": math.e
            }
            result = eval(self.expression, {"__builtins__": None}, safe_dict)
            self.last_result = str(result)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
            self.expression = str(result)  # ✅ Ensure the next input is correct
        except ZeroDivisionError:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Math Error")
            self.expression = ""
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Invalid")
            self.expression = ""

    def clear_screen(self):
        """Clears the calculator screen"""
        self.expression = ""
        self.entry.delete(0, tk.END)

    def toggle_dark_mode(self):
        """Toggles between Light and Dark mode"""
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        """Applies the current theme (Light or Dark)"""
        bg_color = "#1e1e1e" if self.dark_mode else "#ffffff"
        text_color = "#ffffff" if self.dark_mode else "#000000"
        btn_color = "#333333" if self.dark_mode else "#f0f0f0"

        self.root.configure(bg=bg_color)
        self.entry.configure(bg=bg_color, fg=text_color, insertbackground=text_color)

        # Update buttons & labels dynamically
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

        label = tk.Label(about_window, text="Advanced Calculator\nCreated by Ioseb Vardoshvili", font=("Arial", 14), pady=20)
        label.pack()

        close_btn = tk.Button(about_window, text="Close", font=("Arial", 12), command=about_window.destroy)
        close_btn.pack(pady=10)

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
