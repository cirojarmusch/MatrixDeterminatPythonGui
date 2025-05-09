import tkinter as tk
import numpy as np

def calculate_determinant():
    try:
    
        size = int(size_selection.get())
        matrix = []

        
        for i in range(size):
            row = []
            for j in range(size):
                value = matrix_entries[i][j].get()
                row.append(float(value))
            matrix.append(row)

        
        matrix_np = np.array(matrix)
        determinant = np.linalg.det(matrix_np)

        
        result_var.set(f"Determinant: {round(determinant, 4)}")
    except ValueError:
        result_var.set("Error: Please enter valid numeric values.")
    except:
        result_var.set("Error: An unexpected problem occurred.")

def update_entries(*args):
    
    for row in matrix_entries:
        for entry in row:
            entry.destroy()
    matrix_entries.clear()

    
    size = int(size_selection.get())
    for i in range(size):
        row = []
        for j in range(size):
            entry = tk.Entry(root, width=5)
            entry.grid(row=i+2, column=j)
            row.append(entry)
        matrix_entries.append(row)


root = tk.Tk()
root.title("Determinant Calculator for Matrices")


tk.Label(root, text="Select Matrix Size:").grid(row=0, column=0, columnspan=3)
size_selection = tk.StringVar()
size_selection.set("2")
options = tk.OptionMenu(root, size_selection, "2", "3", "4", "5", command=update_entries)
options.grid(row=0, column=3)


tk.Button(root, text="Calculate Determinant", command=calculate_determinant).grid(row=1, column=0, columnspan=4)


result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12))
result_label.grid(row=8, column=0, columnspan=4)


matrix_entries = []


update_entries()

root.mainloop()
