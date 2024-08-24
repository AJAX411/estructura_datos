#sistema de control de ingreso para evitar sobre cupo
entrada_permitida = 0
import time

while entrada_permitida < 5:
        print("\nSu boleto es para la pelicula de las 10 AM?")
        respuesta = input("si/no: ")
        if respuesta == "si":
            print("Adelante, puede ingresar.")
            entrada_permitida = entrada_permitida + 1
            time.sleep(1)
        elif respuesta == "no":
            print("Acceso no permitido")
            time.sleep(1)
        elif respuesta == "contador":
            print("El numero de personas ingresadas es ", entrada_permitida)
            
print("\nYa no se permiten mas ingresos.")


