def run():
    # ejemplo 2 de como pasar de listas a list comprehensions
    #numeros = []
    #for i in range (0, 1000):
    #    if i % 4 == 0 and i % 6 == 0 and i % 9 == 0:
    #        numeros.append(i)
    #print(numeros)

    numeros = [i for i in range(0, 1000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(numeros)
    
    # ejemplo 1
    #squares = []
    #for i in range(1, 101):
    #    if i**2 % 3 != 0:
    #        squares.append(i**2)
    #print(squares)
    #
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

if __name__ == '__main__':
    run()