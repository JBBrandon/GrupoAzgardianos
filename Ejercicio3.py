import math

def grados_a_radianes(grados):
    return grados * (math.pi / 180)

def radianes_a_grados(radianes):
    return radianes * (180 / math.pi)

def mostrar_menu():
    print("1. Convertir de grados a radianes")
    print("2. Convertir de radianes a grados")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            grados = float(input("Ingrese los grados a convertir a radianes: "))
            radianes = grados_a_radianes(grados)
            print(f"{grados} grados son aproximadamente {radianes:.2f} radianes\n")
        elif opcion == "2":
            radianes = float(input("Ingrese los radianes a convertir a grados: "))
            grados = radianes_a_grados(radianes)
            print(f"{radianes:.2f} radianes son aproximadamente {grados} grados\n")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.\n")

if __name__ == "__main__":
    main()
