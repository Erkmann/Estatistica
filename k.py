def get_numero_classes(amplitude, desvio, n):
    raiz_cubica = n ** (1/3)

    return (1 + ((amplitude * raiz_cubica) / (3.49 * desvio)))


c = True
while c:
    amplitude = float(input('Amplitude: '))
    desvio = float(input('Desvio: '))
    n = float(input('Tamanho: '))

    print(get_numero_classes(amplitude, desvio, n))

    cont = float(input('Continuar? (1,0): '))

    if cont == 0:
        c = False

    print('\n')