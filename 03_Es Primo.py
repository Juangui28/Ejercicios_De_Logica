'''
* Escribe un programa que se encargue de comprobar si un número es o no primo.
* Hecho esto, imprime los números primos entre 1 y 100.
'''
num = int(input("Digite un numero: "))
count_one = 0


###### Saber si es numero primo o no ######
for n in range(1,num+1):
    if(num % n == 0):
        count_one += 1

if(count_one == 2):
    print(f"El {num} es numero primo") 
else:
    print(f"El {num} no es numero primo") 



###### Numeros primos del 1 al 100 ######
for n in range(1,101):
    count_two = 0
    for x in range(1,n+1):
        if(n % x == 0):
            count_two += 1

    if(count_two == 2):
        print(f"El {n} es numero primo") 

