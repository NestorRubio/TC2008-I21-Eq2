import os


def leerOpcionMenu():
    print('''Selecciona la opción del problema que te gustaría correr: 
                1. Problema 7: productor-consumidor en buffer de tamaño 2
                2. Problema 8: puesto de hamburguesas
                3. Poblema extra: tienda en tiempos de COVID 
                0. Salir ''')
    opcion = int(input("Qué desea hacer? "))
    return opcion


def main():
    
    opcion = leerOpcionMenu()
    while opcion != 0:
      if opcion == 1:
          print()
          os.system("python productorconsumidor.py")
          print()
      elif opcion == 2:
          print()
          os.system("python hamburguesas.py")
          print()
      elif opcion == 3:
          print()
          os.system("python tienda.py")
          print()
      else:
          print("Esta opción no es válida, selecciona una opción correcta")
      opcion = leerOpcionMenu()

    print()
    print("Termina Programa")


main()
