num = int(input('Por favor digite su numero: '))            # Ingresar un numero
num_str = str(num)                                          # Convertimos de int -> str
potencia = len(num_str) - 1                                 # Cantidad de digitos
my_list = []

dividendo = num

for i in range(len(num_str)):
    division = dividendo // 10**potencia                    # División entera por potencia de 10
    my_list.append(division)
    dividendo = dividendo % 10**potencia                    # Actualizamos el dividendo para la siguiente iteración
    potencia -= 1

sum = 0
num_two = 0

for i in range (len(num_str)):
    num_two = my_list[i]
    operacion = pow(num_two,len(num_str))
    sum = sum + operacion

if sum == num:
    print(f"El {num} es un numero armstrong")
else:
    print(f"El {num} no es un numero armstrong")