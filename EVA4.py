numero = elegir(0)
edad = 0
temperatura = 0.0




def opcion():
    print("|||||||||||||menu principal||||||||||||||")
    print("1. agregar paciente")
    print("2. buscar paciente")
    print("3. eliminar paciente")
    print("4. actualizar estado")
    print("5. mostrar pacientes")
    print("6. salir")

def elegir(numero):
    return int(input("Elija una opcion del menu: "))

x = elegir(numero)
print(x)


if numero == 1:
    def agregar_paciente():
        nombre = input("Ingrese nombre del paciente: ")
        edad = int(input("Ingrese edad del paciente: "))
        temperatura = float(input("Ingrese temperatura del paciente: "))
        print(f"Paciente {nombre} agregado con éxito.")

if numero == 2:
    nombre = input("Ingrese nombre del paciente a buscar: ")
    print(f"Buscando paciente {nombre}...")
    # Aquí iría la lógica para buscar al paciente
    def buscar_paciente(nombre):
        # Lógica para buscar al paciente en la base de datos
        print(f"Paciente {nombre} encontrado.")

if numero == 3:
    nombre = input("Ingrese nombre del paciente a eliminar: ")
    print(f"Eliminando paciente {nombre}...")
    # Aquí iría la lógica para eliminar al paciente
    def eliminar_paciente(nombre):
        # Lógica para eliminar al paciente de la base de datos
        print(f"Paciente {nombre} eliminado.")

if numero == 4:
    nombre = input("Ingrese nombre del paciente a actualizar: ")
    nuevo_estado = input("Ingrese el nuevo estado del paciente: ")
    print(f"Actualizando estado del paciente {nombre} a {nuevo_estado}...")
    # Aquí iría la lógica para actualizar el estado del paciente
    def actualizar_estado(nombre, nuevo_estado):
        # Lógica para actualizar el estado del paciente en la base de datos
        print(f"Estado del paciente {nombre} actualizado a {nuevo_estado}.")

if numero == 5:
    print("Mostrando todos los pacientes...")
    # Aquí iría la lógica para mostrar todos los pacientes
    def mostrar_pacientes():
        # Lógica para mostrar todos los pacientes en la base de datos
        print("Lista de pacientes:")
        print(nombre)