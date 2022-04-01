def primo(numero):
    contador = 0
    for i in range (1, numero + 1):
        if i == 1 or i == numero:
            continue
        elif numero % i == 0:
            contador += 1
        elif contador != 0:
            return True
    if contador == 0:
        return numero


def run():
    lista_de_primos = []
    for numero in range (1, 104730):
        numero = primo(numero)
        if numero != True:
            lista_de_primos.append(numero)
    print(len(lista_de_primos))
      


if __name__ == '__main__':
    run()