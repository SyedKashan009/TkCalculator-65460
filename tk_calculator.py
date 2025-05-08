import tkinter as tk
from tkinter import messagebox


def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

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

        result_label.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))


root = tk.Tk()
root.title("Simple Calculator")


tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, pady=5)


tk.Button(root, text="Add", width=10, command=lambda: calculate("add")).grid(row=2, column=0, pady=5)
tk.Button(root, text="Subtract", width=10, command=lambda: calculate("subtract")).grid(row=2, column=1, pady=5)
tk.Button(root, text="Multiply", width=10, command=lambda: calculate("multiply")).grid(row=3, column=0, pady=5)
tk.Button(root, text="Divide", width=10, command=lambda: calculate("divide")).grid(row=3, column=1, pady=5)


result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)


root.mainloop()
