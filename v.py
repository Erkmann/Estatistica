def get_v_quadrado(v, media):
    return pow(v - media, 2)

c = True
while c:
    v = float(input('V: '))
    media = float(input('Media: '))

    print(get_v_quadrado(v, media))

    cont = float(input('Continuar? (1,0): '))

    if cont == 0:
        c = False

    print('\n')