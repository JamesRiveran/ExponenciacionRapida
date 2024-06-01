import tkinter as tk
from tkinter import messagebox
from exponenciacion_rapida import calcular, exponenciacion_rapida

def limpiar():
    entry_base.delete(0, tk.END)
    entry_exponente.delete(0, tk.END)
    entry_modulo.delete(0, tk.END)
    label_resultado.config(text="")
    label_titulo.config(text="")

def on_entry_change(event):
    try:
        base = int(entry_base.get())
        exponente = int(entry_exponente.get())
        modulo = int(entry_modulo.get())
        calcular(base, exponente, modulo, label_resultado, label_titulo)
    except ValueError:
        label_resultado.config(text="Por favor, complete todos los campos con números enteros")


root = tk.Tk()
root.title("Exponenciación Rápida")


tk.Label(root, text="Base:").grid(row=0, column=0, padx=10, pady=10)
entry_base = tk.Entry(root)
entry_base.grid(row=0, column=1, padx=10, pady=10)
entry_base.bind('<KeyRelease>', on_entry_change)

tk.Label(root, text="Exponente:").grid(row=1, column=0, padx=10, pady=10)
entry_exponente = tk.Entry(root)
entry_exponente.grid(row=1, column=1, padx=10, pady=10)
entry_exponente.bind('<KeyRelease>', on_entry_change)

tk.Label(root, text="Módulo:").grid(row=2, column=0, padx=10, pady=10)
entry_modulo = tk.Entry(root)
entry_modulo.grid(row=2, column=1, padx=10, pady=10)
entry_modulo.bind('<KeyRelease>', on_entry_change)


label_titulo = tk.Label(root, text=" ")
label_titulo.grid(row=4, column=0, columnspan=2, pady=10)


label_resultado = tk.Label(root, text="Por favor, complete todos los campos con números enteros")
label_resultado.grid(row=5, column=0, columnspan=2, pady=10)


button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Limpiar", command=limpiar, bg='lightgrey').grid(row=0, column=0, padx=5)


root.mainloop()