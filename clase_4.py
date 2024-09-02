#En esta clase se vio el tema de funciones (def)
#Ejercicio 1 operaciones basicas

'''def operacion(opcion:int, n1:int, n2:int):
    if opcion == 1:
        resultado_suma = (n1 + n2)
        return f"El resultado de la suma es {resultado_suma}"
    elif opcion == 2:
        resultado_resta = (n1 - n2)
        return f"El resultado de la resta es {resultado_resta}"
    elif opcion == 3:
        resultado_mult = (n1 * n2)
        return f"El resultado de la multiplicacion es {resultado_mult}"
    elif opcion == 4:
        resultado_div = (n1 / n2)
        return f"El resultado de la division es {resultado_div}"
    elif opcion > 4: 
        return "Opcion no valida."
    
print("Aqui podras realizar operaciones como:")
print("1. suma")
print("2. resta")
print("3. multiplicar")
print("4. dividir")
opcion = int(input("Que desea realizar? "))
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
print(operacion(opcion,n1,n2))'''

#Ejercicio 2 conversion temperatura

'''def convertidor(temp_celsius:float):
    fahrenheit = 1.08 * temp_celsius + 32
    return f"La temperatura en fahrenheit es {fahrenheit}"

print("Aqui vamos a converir temperatura de celsius a fahrenheit.")
temp_celsius = int(input("Ingrese la temperatura a convertir: "))
print(convertidor(temp_celsius))'''

#Ejercicio 3 verificacion de palindromo
'''def verificacion_p(palabra):
    palabra = palabra.replace("","").lower()
    return palabra == palabra[::-1]

print("aqui vamos a verificar si una palabra es un palindromo.")
palabra = str(input("Escriba la palabra: "))
if verificacion_p(palabra):
    print("La palbra", palabra, "es un palindromo")
else:
    print("La palabra", palabra, "no es un palindromo.")'''

#Ejercicio 4 generador de contraceña

import random
import string

def generador_contra(cant_caracteres):
    caracteres = string.ascii_letters + string.digits
    contraseña = ''.join(random.choice(caracteres) for _ in range(cant_caracteres))
    return contraseña

print("Aqui vamos a generar contraceñas aleatorias.")
cant_caracteres = int(input("ingrese la cantidad de caracteres a generar: "))
contraseña = generador_contra(cant_caracteres)
print(f'La contraseña generada es: {contraseña}')