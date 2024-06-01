# exponenciacion_rapida_gui.py
import tkinter as tk
from tkinter import messagebox
from exponenciacion_rapida import calcular

# Crear la ventana principal
root = tk.Tk()
root.title("Exponenciación Rápida")

# Crear y colocar los widgets
tk.Label(root, text="Base:").grid(row=0, column=0, padx=10, pady=10)
entry_base = tk.Entry(root)
entry_base.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Exponente:").grid(row=1, column=0, padx=10, pady=10)
entry_exponente = tk.Entry(root)
entry_exponente.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Módulo:").grid(row=2, column=0, padx=10, pady=10)
entry_modulo = tk.Entry(root)
entry_modulo.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Calcular", command=lambda: calcular(entry_base, entry_exponente, entry_modulo, messagebox)).grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
