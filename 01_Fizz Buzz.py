'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 '''

for n in range(1,100):
    if(n % 3 == 0 and n % 5 == 0):
        print("Fizz Buzz")
    elif (n % 3 == 0):
        print("Fizz")
    elif (n % 5 == 0):
        print("Buzz")
    else:
        print(n)
    
    n += 1