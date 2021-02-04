import threading
import time
import sys

# Shop problem
# Una tienda acaba de reabrir porque hay semáforo rojo por la situación de coronavirus. Únicamente hay un
# empleado y solamente puede haber n personas esperando a ser atendidas, puesto que el aforo máximo de la
# tienda es de n. Si ya hay n personas esperando y llega otro cliente, dicho cliente deberá retirarse del
# lugar. El empleado únicamente podrá atender a una persona a la vez y si no hay clientes en la tienda, el
# empleado deberá ponerse a desinfectar el lugar.

nInicial = 10  # numero de asientos/lugares de la fila
n = 10  # contador de asientos/lugares de la fila
empleadoDisponible = threading.Semaphore(0)  # semáforo para verificar si el empleado está disponible (el escenario inicial es que está desinfectando) - boolean
lugarDisponible = threading.Semaphore(1)  #evitar que haya deadlock al revisar si hay lugares, accede al contador n.
clientes = threading.Semaphore(0)  #indica que ya hay clientes en la tienda


def cliente():  # Cliente llega
    while (True):
        global n
        lugarDisponible.acquire()
        print("Lugares disponibles: ", n)
        if (n > 0):
            #lugarDisponible.acquire()
            n -= 1
            lugarDisponible.release()
            print("Un cliente acaba de entrar a la tienda, lugares disponibles: ", n)
            clientes.release()
            empleadoDisponible.acquire() #espera a ser atendido por el empleado
        else:
            lugarDisponible.release()
            print("Un cliente quería entrar pero no habían lugares disponibles, el cliente se tuvo que retirar.")
        time.sleep(0.5)


def empleado():  # Funciones del empleado
    while (True):
        global n
        if (n == nInicial):
            print("Empleado desinfectando el lugar")
        clientes.acquire()  # en lo que espera se pone a desinfectar
        empleadoDisponible.release()  # se dirige hacia el cliente
        print("Empleado atendiendo a un cliente.")
        lugarDisponible.acquire()
        n += 1
        lugarDisponible.release()
        print("El cliente ha sido atendido y se ha retirado")

        time.sleep(0.5)


def main():
    hilo1 = threading.Thread(target=empleado, daemon=True)
    hilo2 = threading.Thread(target=cliente, daemon=True)
    hilo3 = threading.Thread(target=cliente, daemon=True)
    hilo4 = threading.Thread(target=cliente, daemon=True)
    hilo1.start()
    time.sleep(1)
    hilo2.start()
    time.sleep(2)
    hilo3.start()
    time.sleep(1)
    hilo4.start()
    time.sleep(2)

    sys.exit()


main()