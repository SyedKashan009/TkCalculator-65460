import tkinter as tk
from tkinter import messagebox
import math

# Function to perform calculations
def calculate(operation):
    try:
        num1_text = entry1.get()
        num2_text = entry2.get()

        if num1_text.strip() == "":
            raise ValueError("First number is required.")
        num1 = float(num1_text)

        result = None

        if operation in ["add", "subtract", "multiply", "divide"]:
            if num2_text.strip() == "":
                raise ValueError("Second number is required for this operation.")
            num2 = float(num2_text)

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    raise ValueError("Cannot divide by zero.")
                result = num1 / num2

        elif operation == "square":
            result = num1 ** 2
        elif operation == "sqrt":
            if num1 < 0:
                raise ValueError("Cannot take square root of a negative number.")
            result = math.sqrt(num1)

        result_label.config(text=f"Result: {result:.4f}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Main GUI window
root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("300x300")  # set fixed size

# Input fields
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root, width=25)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root, width=25)
entry2.pack()

# Operation buttons frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

# Row 1
tk.Button(btn_frame, text="Add", width=12, command=lambda: calculate("add")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Subtract", width=12, command=lambda: calculate("subtract")).grid(row=0, column=1, padx=5, pady=5)

# Row 2
tk.Button(btn_frame, text="Multiply", width=12, command=lambda: calculate("multiply")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Divide", width=12, command=lambda: calculate("divide")).grid(row=1, column=1, padx=5, pady=5)

# Row 3
tk.Button(btn_frame, text="Square", width=12, command=lambda: calculate("square")).grid(row=2, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Square Root", width=12, command=lambda: calculate("sqrt")).grid(row=2, column=1, padx=5, pady=5)

# Result display
result_label = tk.Label(root, text="Result:", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
