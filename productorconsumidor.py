import threading
import time
import sys

p = threading.Semaphore(2) # procesos que falta por producir
c =  threading.Semaphore(0) # procesos disponibles para que consumidor
bff = list()

def productor():
    while(True):
        dato = "a"
        p.acquire() # P(SP)
        print("Generando el producto número:", len(bff)+1)
        bff.append(dato)
        c.release() #v(SC)
        time.sleep(0.5)

def consumidor():
    while(True):
        c.acquire() #V(SC)
        c.acquire() #V(SC)
        print("Consumidor tomando los dos datos")
        bff.pop()
        bff.pop()
        print("Productos tomados: ", len(bff)+2)
        print("Esperando a que se genere otro producto")
        p.release() #V(VP)
        p.release() #V(VP)
        time.sleep(0.5)

def main():

    t1 = threading.Thread(target=productor, daemon=True)
    t1.start()
    time.sleep(3)

    t2 = threading.Thread(target=consumidor, daemon=True)
    t2.start()
    time.sleep(3)

    sys.exit()
main()