#primer ejercicio
'''pares = [] 
for n in range(2,102,2):
    pares.append(n)
print(pares)'''

#segundo ejercicio
'''altura = int(input("ingrese la altura: "))
for x in range(1,altura+1):
    print("*" * x)'''

#tercer ejercicio
'''numeros_aleatorios = [1,6,3,7,9,3,6,44,6,7]
promedio = sum(numeros_aleatorios) / len(numeros_aleatorios)
print("el promedio de los numeros es ", promedio)'''

#cuarto ejercicio
print("Aqui vamos a calcular el factorial de un numero.")
numero = int(input("ingrese el numero: "))

factorial = 1

for i in range(1, numero + 1):
    factorial = factorial * i

print(f"El factorial de {numero} es {factorial}")