from colored import fg, bg, attr

color = fg(255) + bg(124)
reset = attr('reset')
letra = attr(1)


def turno(mi_turno):
    print('Hola, tu turno es: ')
    print(f'{letra}',f'{color}', next(mi_turno), f'{reset}')
    print('Por favor espere...')


def perfumes():
    p = 0
    while True:
        p += 1
        yield f'P-{p}'


def farmacia():
    f = 0
    while True:
        f += 1
        yield f'F-{f}'


def cosmeticos():
    c = 0
    while True:
        c += 1
        yield f'C-{c}'
