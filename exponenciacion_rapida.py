# exponenciacion_rapida.py
def exponenciacion_rapida(base, exponente, modulo=None):
    resultado = 1
    base = base % modulo if modulo else base

    while exponente > 0:
        if (exponente % 2) == 1:
            resultado = (resultado * base) % modulo if modulo else resultado * base
        exponente = exponente >> 1
        base = (base * base) % modulo if modulo else base * base

    return resultado

def calcular(entry_base, entry_exponente, entry_modulo, messagebox):
    try:
        base = int(entry_base.get())
        exponente = int(entry_exponente.get())
        modulo = int(entry_modulo.get())
        
        resultado = exponenciacion_rapida(base, exponente, modulo)
        
        messagebox.showinfo("Resultado", f"El resultado de {base}^{exponente} mod {modulo} es {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores enteros válidos.")
