#PIDE AL USUARIO 3 NOMBRES Y LOS MUESTRA
nombres = []

def agregar(nombre): 
    nombres.append(nombre)

def mostrar():
    return nombres
   
def editar(posicion, nuevo_nombre):
    nombres[posicion] = nuevo_nombre

def eliminar(posicion, posicion1):
    nombres.pop(posicion1)

def eliminar(nombre):
    nombres.remove(nombre)

print(mostrar())

for i in range(3):
    nombre_usuario = input(f"Ingrese el nombre {i + 1}: ")
    agregar(nombre_usuario)

print("Los nombres ingresados son: ", mostrar())
    