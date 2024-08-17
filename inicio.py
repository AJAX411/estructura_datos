'''#primer ejercicio en clase de estructura de datos.
print("A continuacion ingrese 3 números diferentes")
valor1 = int(input("Ingrese un número: "))
valor2 = int(input("Ingrese otro número: "))
valor3 = int(input("Ingrese otro número: "))
numeros = [valor1, valor2, valor3]
numero_mayor = max(numeros)
numero_menor= min(numeros)
print(f"El número mayor es {numero_mayor} y el menor es {numero_menor}.")'''

'''#segundo ejercicio en clase de estructura de datos.
print("Vamos a determinar si un numero es par o impar.")
numero_par_impar = int(input("Ingrese un numero: "))
if numero_par_impar % 2 == 0:
  print(numero_par_impar, "es un numero par.")
else:
  print(numero_par_impar, "es un numero impar.")'''

'''#tercer ejercicio en clase de estructura de datos.
print("Aqui vamos a sumar, restar y dividir.")
numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("ingrese otro numero: "))
print("\n Que desea realizar?")
print("1. suma")
print("2. resta")
print("3. division")
operacion = int(input("Seleccione la operacion: "))
if operacion == 1:
  suma = numero_1 + numero_2
  print("El resultado de la suma es ", suma)
elif operacion == 2:
  resta = numero_1 - numero_2
  print("El resultador de la resta es", resta)
elif operacion == 3:
  division = numero_1 / numero_2
  print("El resultado de la division es", division)'''

'''#cuarto ejercicio en clase de estructura de datos.
print("vamos a calcular su IMC.")
peso = int(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
imc = peso / (altura ** 2)
if imc < 18.5:
  print("Su perso es insuficiente.")
elif imc >= 18.5 and imc <= 24.9:
  print("Su peso es saludable.")
elif imc >= 25 and imc <= 29.9:
  print("presentas sobrepeso.")
elif imc >= 30 and imc <= 34.9:
  print("Presentas obesidad.")
elif imc >= 35:
  print("Presentas obesidad mórbida.")'''