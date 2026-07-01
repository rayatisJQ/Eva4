agregar_paciente=0
eliminar_paciente=0
actualizar_estado=0
mostrar_pacientes=0
pacientes = 0

def opcion():
    print("|||||||||||||menu principal||||||||||||||")
    print("1. agregar paciente")
    print("2. buscar paciente")
    print("3. eliminar paciente")
    print("4. actualizar estado")
    print("5. mostrar pacientes")
    print("6. salir")

def elegir(numero):
    if numero == 1:
        nombre = input("Ingrese nombre del paciente: ")
        while True:
            try:
                edad = int(input("Ingrese edad del paciente: "))
                if edad < 0:
                    print("La edad no puede ser negativa. Intente nuevamente.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un número entero válido para la edad.")

        while True:
            try:
                temperatura = float(input("Ingrese temperatura del paciente: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para la temperatura.")
    elif numero == 2:
        nombre = input("Ingrese nombre del paciente a buscar: ")
        def busqueda(nombre):
            for paciente in pacientes:
                if paciente['nombre'] == nombre:
                    print(f"Paciente encontrado: {paciente} {edad} {temperatura}")
                    return
            print("Paciente no encontrado.")
    elif numero == 3:
        nombre = input("Ingrese nombre del paciente a eliminar: ")
        eliminar_paciente(nombre)
        def eliminar_paciente(nombre):
            for paciente in pacientes:
                if paciente['nombre'] == nombre:
                    pacientes.remove(paciente)
                    print(f"Paciente {nombre} eliminado.")
                    return
            print("Paciente no encontrado.")
    elif numero == 4:
        nombre = input("Ingrese nombre del paciente a actualizar: ")
        nuevo_estado = input("Ingrese el nuevo estado del paciente: ")
        actualizar_estado(nombre, nuevo_estado)
        def actualizar_estado(nombre, nuevo_estado):
            for paciente in pacientes:
                if paciente['nombre'] == nombre:
                    paciente['estado'] = nuevo_estado
                    print(f"Estado del paciente {nombre} actualizado a {nuevo_estado}.")
                    return
            print("Paciente no encontrado.")
    elif numero == 5:
        def mostrar_pacientes():
            if not pacientes:
                print("No hay pacientes registrados.")
            else:
                print("Lista de pacientes:")
                for paciente in pacientes:
                    print(f"Nombre: {paciente['nombre']}, Edad: {paciente['edad']}, Temperatura: {paciente['temperatura']}")
        mostrar_pacientes()
    elif numero == 6:
        print("gracias por utilizar el sistema de registro de pacientes")

print(opcion())
print(elegir(int(input("Ingrese una opcion del menu: "))))
