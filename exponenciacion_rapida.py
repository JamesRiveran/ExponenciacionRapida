def exponenciacion_rapida(base, exponente, modulo=None):
    resultado = 1
    base = base % modulo if modulo else base

    while exponente > 0:
        if (exponente % 2) == 1:
            resultado = (resultado * base) % modulo if modulo else resultado * base
        exponente = exponente >> 1
        base = (base * base) % modulo if modulo else base * base

    return resultado

# Ejemplo de uso
base = 2
exponente = 10
modulo = 1000
print(f"{base}^{exponente} mod {modulo} = {exponenciacion_rapida(base, exponente, modulo)}")
