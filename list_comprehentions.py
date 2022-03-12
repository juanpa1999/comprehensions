def run():
    # primer ejemplo de guia para utilizar el for en una lista y agregar estos valores a una lista
    #squares = []
    #for i in range(1, 101):
    #    if i**2 % 3 != 0:
    #        squares.append(i**2)
    #    
    #print(squares)
    # ejemplo completo de list comprenhentions
    #squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    #print(squares)
    multiples_4_6_9 = [ i % 4 or 6 or 9 for i in range(0,100000) if i % 4 or 6 or 9 != 0]
    print(multiples_4_6_9)

if __name__ == '__main__':
    run()