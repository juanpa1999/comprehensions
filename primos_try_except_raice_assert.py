def primo(numero):
    contador = 0
    for i in range (1, numero + 1):
        if i == 1 or i == numero:
            continue
        elif numero % i == 0:
            print(i)
            contador += 1
        elif contador != 0:
            return True
    if contador == 0:
        return False     


def run():
    try:
        numero = int(input('escribe un numero: '))
        #if numero <= 0:
        #    raise Exception
        assert numero > 0, 'debe ser un numero positivo mayor a cero'
        numero = primo(numero)
        if numero == True:
            print('NO ES primo')
        else:
            print('ES PRIMO')
    except ValueError:
        print('debes escribir un numero no una letra o caracter')
    #except Exception:
    #    print('solo puedes escribir numeros positivos')


if __name__ == '__main__':
    run()