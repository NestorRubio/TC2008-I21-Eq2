def leerOpcionMenu():
    print('''Selecciona la opción del problema que te gustaría correr: 
                1. Problema 7: productor-consumidor en buffer de tamaño 2
                2. Problema 8: puesto de hamburguesas
                3. Poblema extra 
                0. Salir ''')
    opcion = int(input("Qué desea hacer?"))
    return opcion

def main():
    opcion=leerOpcionMenu()
    while opcion !=0:
        if opcion == 1: 
            #correr problema 1
            print("problema 1")
        elif opcion == 2:
            #correr programa 2
            print ("problema 2")
        elif opcion==3:
            #correr programa 3
            print ("problema 3")
        else: 
            print("Esta opción no es válida, selecciona una opción correcta")

    print("Termina Programa")


main()