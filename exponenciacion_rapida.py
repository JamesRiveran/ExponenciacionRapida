def exponenciacion_rapida(base, exponente, modulo=None):
    resultado = 1
    base = base % modulo if modulo else base

    while exponente > 0:
        if (exponente % 2) == 1:
            resultado = (resultado * base) % modulo if modulo else resultado * base
        exponente = exponente >> 1
        base = (base * base) % modulo if modulo else base * base

    return resultado

def calcular(base, exponente, modulo, label_resultado, label_titulo):
    resultado = exponenciacion_rapida(base, exponente, modulo)
    label_titulo.config(text=f"{base}^{exponente} mod {modulo}")
    label_resultado.config(text=f"{resultado}")