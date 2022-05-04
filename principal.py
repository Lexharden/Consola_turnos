import numeros
import time


def validar_opcion():
    opcion = 'x'
    while opcion != 4:
        while True:
            try:
                opcion = int(input('Ingresa tu opcion (1-4): '))
                if opcion == 1:
                    print('*' * 30)
                    print('PERFUMES')
                    print('*' * 30)
                    numeros.turno(perfume)
                    regresar()
                elif opcion == 2:
                    print('*' * 30)
                    print('FARMACIA')
                    print('*' * 30)
                    numeros.turno(farmacia)
                    regresar()
                elif opcion == 3:
                    print('*' * 30)
                    print('COSMETICOS')
                    print('*' * 30)
                    numeros.turno(cosmetico)
                    regresar()
                elif opcion == 4:
                    print('*' * 30)
                    print('Gracias por utilizar el sistema de turnos! Adios!')
                    print('*' * 30)
                    break
                else:
                    print('Opcion invalida')
                    time.sleep(1)
            except ValueError:
                print('Unicamente numeros')
            else:
                break


def menu():
    print('*' * 30)
    print('Bienvenido a Farmacia Python')
    print('*' * 30)
    print("""
    1-Perfmues
    2-Farmacia
    3-Cosmeticos
    4-Salir
    """)


def regresar():
    input('Presiona ENTER para regresar: ')
    menu()


perfume = numeros.perfumes()
farmacia = numeros.farmacia()
cosmetico = numeros.cosmeticos()

if __name__ == '__main__':
    menu()
    validar_opcion()
