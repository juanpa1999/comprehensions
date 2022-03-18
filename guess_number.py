import random


def run():
    naturals_numbers = []
    for i in range(1,101):
        naturals_numbers.append(i)
    numero = random.choice(naturals_numbers)
    
    print('hola es es el juego de adivina el numero de 1 a 100')
    print('vamos a comerzar.')
    answer = int(input('escribe tu numero: '))
    vida = 5
    while numero != answer:
        if numero > answer:
            print('el numero es mas grande')
            vida = vida - 1
            print('tienes ' + str(vida) + ' vidas')
            answer = int(input('escribe un nuevo numero: '))
            if vida == 0:
                print('perdiste')
                print(str(numero))
                break           
        elif numero < answer:
            print('el numero es mas pequeño')
            vida = vida - 1
            print('tienes ' + str(vida) + ' vidas')
            answer = int(input('escribe un nuevo numero: '))
            if vida == 0:
                print('perdiste')
                print(str(numero))
                break
        if answer == numero:
            print('ganaste')


if __name__ == '__main__':
    run()