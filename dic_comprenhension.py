import numbers


import math

def run():
    #natural_numbers = {}
    #for key in range(1, 101):
    #    if key % 3 != 0:
    #        natural_numbers[key]= key**3
    #print(natural_numbers)

    #natural_numbers = {key: key**3 for key in range(1, 101) if key % 3 != 0}
    #print(natural_numbers)

    #raiz = {}
    #for i in range(1, 1000):
    #    raiz[i]= math.sqrt(i)
    #print(raiz)

    raiz = {i: math.sqrt(i) for i in range(1, 100)}
    print(raiz)


if __name__ == '__main__':
    run()