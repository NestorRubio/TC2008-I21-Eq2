import threading

p = threading.Semaphore(2)  # procesos que falta por producir
c = threading.Semaphore(0)  # procesos disponibles para que consumidor
bff = list()


def productor():
    while (True):
        dato = "a"
        p.acquire()  # P(SP)
        print("Generando el producto número:", len(bff) + 1)
        bff.append(dato)
        c.release()  #v(SC)


def consumidor():
    while (True):
        c.acquire()  #V(SC)
        c.acquire()  #V(SC)
        print("Consumidor tomando los dos datos")
        bff.pop()
        bff.pop()
        print("Productos tomados: ", len(bff) + 2)
        print("Esperando a que se genere otro producto")
        p.release()  #V(VP)
        p.release()  #V(VP)


def main():
    hilo1 = threading.Thread(target=productor)
    hilo2 = threading.Thread(target=consumidor)
    hilo2.start()
    hilo1.start()


main()
