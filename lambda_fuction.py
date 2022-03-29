palimdrom = lambda word: word == word[::-1]
print(palimdrom('holaa'))
# aqui tenemos un ejemplo de la fuction lambda que nos da los detalles de una funcion osea True or False normalmente se utilizan dentro de funciones de orden superior
divisors = lambda num: [x for x in range(1, num + 1) if num % x == 0]
# otro ejemplo de una lambda haciendo que se almacenen datos en una list comprehentions