def busqueda_binaria(lista, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1  # Elemento no encontrado

    medio = (izquierda + derecha) // 2
    valor_medio = lista[medio]

    if valor_medio == objetivo:
        return medio  # Elemento encontrado
    elif valor_medio < objetivo:
        return busqueda_binaria(lista, objetivo, medio + 1, derecha)  # Buscar en la mitad derecha
    else:
        return busqueda_binaria(lista, objetivo, izquierda, medio - 1)  # Buscar en la mitad izquierda


lista = [2, 4, 6, 8, 10, 12, 14, 16]
objetivo = 10
resultado = busqueda_binaria(lista, objetivo, 0, len(lista) - 1)

if resultado != -1:
    print(f'Elemento encontrado: {resultado}')
else:
    print('Elemento no encontrado')
