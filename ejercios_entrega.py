# aqui se subieran lo ejercicio que deben ser entregados.

#Ejercicio de listas enlazadas.
#Ejercicio 1: Diseñe  un sistema para el control de un sistema de un parque Zoologico.
'''class Animal:
    def __init__(self, edad:int, tipo:str):
        self.edad = edad
        self.tipo = tipo
    
    def __str__(self):
        return "El animal es {} y tiene {} años.".format(self.tipo, self.edad)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, animal):
        nuevo_nodo = Nodo(animal)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                if actual.dato.tipo == animal.tipo and actual.dato.edad == animal.edad:
                    return  #Este animal ya existe
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir_recursivo(self, nodo):
        if nodo is None:
            return
        print(nodo.dato)
        self.imprimir_recursivo(nodo.siguiente)

    def imprimir_bucle(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente

lista_animales = ListaEnlazada()
lista_animales.agregar(Animal(10, 'águila'))
lista_animales.agregar(Animal(8, 'pantera'))
lista_animales.agregar(Animal(5, 'vaca'))
lista_animales.agregar(Animal(10, 'águila'))  #Ya existe entonces no se agrega
lista_animales.agregar(Animal(13, 'cocodrilo'))
lista_animales.agregar(Animal(15, 'elefante'))
lista_animales.agregar(Animal(3, 'zorro'))

print("\nImpresión de la manera recursiva:")
lista_animales.imprimir_recursivo(lista_animales.cabeza)

print("\nImpresión de la manera con bucle:")
lista_animales.imprimir_bucle()'''

#----------------------------------------------------------------------------------------------------------------
#Ejercicio 2: Diseña e implementa un sistema de gestión de tareas utilizando listas enlazadas.

'''from datetime import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento

    def __str__(self):
        return f"Descripción: {self.descripcion}, Prioridad: {self.prioridad}, Fecha de Vencimiento: {self.fecha_vencimiento}"

class Nodo:
    def __init__(self, tarea=None):
        self.tarea = tarea  
        self.siguiente = None  

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # El primer nodo de la lista enlazada
    
    
    def agregar_tarea(self, nueva_tarea):
        nuevo_nodo = Nodo(nueva_tarea)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            
            actual = self.cabeza
            anterior = None
            while actual is not None and (actual.tarea.prioridad < nueva_tarea.prioridad or
                                          (actual.tarea.prioridad == nueva_tarea.prioridad and actual.tarea.fecha_vencimiento <= nueva_tarea.fecha_vencimiento)):
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo_nodo.siguiente = self.cabeza
                self.cabeza = nuevo_nodo
            else:
                anterior.siguiente = nuevo_nodo
                nuevo_nodo.siguiente = actual
        print(f"Tarea '{nueva_tarea.descripcion}' agregada correctamente.")

    
    def eliminar_tarea(self, descripcion):
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.tarea.descripcion == descripcion:
                if anterior is None:
                    self.cabeza = actual.siguiente  # Eliminar la cabeza
                else:
                    anterior.siguiente = actual.siguiente  # Saltar el nodo
                print(f"Tarea '{descripcion}' eliminada.")
                return
            anterior = actual
            actual = actual.siguiente

        print(f"Tarea '{descripcion}' no encontrada.")

    
    def mostrar_tareas(self):
        if self.cabeza is None:
            print("No hay tareas en la lista.")
            return

        actual = self.cabeza
        print("Tareas pendientes:")
        while actual is not None:
            print(actual.tarea)
            actual = actual.siguiente

    
    def buscar_tarea(self, descripcion):
        actual = self.cabeza
        while actual is not None:
            if actual.tarea.descripcion == descripcion:
                print(f"Tarea encontrada: {actual.tarea}")
                return
            actual = actual.siguiente
        print(f"Tarea '{descripcion}' no encontrada.")

    
    def marcar_completada(self, descripcion):
        self.eliminar_tarea(descripcion)


def convertir_fecha(fecha_str):
    return datetime.strptime(fecha_str, "%Y-%m-%d").date()


lista_tareas = ListaEnlazada()

def menu():
    while True:
        print("\nSistema de Gestión de Tareas:")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar todas las tareas")
        print("4. Buscar tarea por descripción")
        print("5. Marcar tarea como completada")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            prioridad = int(input("Prioridad (1: Alta, 3: Baja): "))
            fecha_vencimiento_str = input("Fecha de vencimiento (YYYY-MM-DD): ")
            fecha_vencimiento = convertir_fecha(fecha_vencimiento_str)
            nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
            lista_tareas.agregar_tarea(nueva_tarea)

        elif opcion == "2":
            descripcion = input("Descripción de la tarea a eliminar: ")
            lista_tareas.eliminar_tarea(descripcion)

        elif opcion == "3":
            lista_tareas.mostrar_tareas()

        elif opcion == "4":
            descripcion = input("Descripción de la tarea a buscar: ")
            lista_tareas.buscar_tarea(descripcion)

        elif opcion == "5":
            descripcion = input("Descripción de la tarea a marcar como completada: ")
            lista_tareas.marcar_completada(descripcion)

        elif opcion == "6":
            print("Saliendo del sistema de gestión de tareas.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

#Aqui se llama al menú 
menu()'''

#Aqui se explica el funcionamiento de las pilas en
class Pila:
    def __init__(self):
        self.elementos = [1,2,3,4,5,6,7,8,9]
    
    def push(self, elementos):
        self.elementos.append(elementos)

    def pop(self):
        return self.elementos.pop()
    
    def peek(self):
        return self.elementos[len(self.elementos)-1]
    
    def isEmpty(self):
        return self.elementos == []

my_pila = Pila()

print("La pila actual es:", my_pila.elementos)
print("\nAhora vamos a agregar un elemento a la pila.")
my_pila.push(10)
print("Ahora la pila se ve asi:", my_pila.elementos)
print("\nAhora vamos a eliminar el ultimo elemento.")
my_pila.pop()
print("Ahora la pila se ve asi:", my_pila.elementos)
print("\nAhora vamos a ver el ultimo elemento de la lista")
print("El ultimo elemento es:", my_pila.peek())
print("\n¿Esta la pila vacía?") 
print(my_pila.isEmpty())