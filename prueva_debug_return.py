def divide(number):
    number = number % 2
    if number == 0:
        return True
    else:
        return False
    

def run():
    number = int(input('escribe un numero: '))
    divisible_by_2 = divide(number)
    if divisible_by_2 == True:
        print('es divisible en 2')
    else:
        print('falso')


if __name__ == '__main__':
    run()