import threading
import time

#creacion de los semaforos
MG = threading.Semaphore(1)
MH = threading.Semaphore(1)
MP = threading.Semaphore(1)
DMG = threading.Semaphore()
DMH = threading.Semaphore()
DMP = threading.Semaphore()
OMG = threading.Semaphore(0)
OMH = threading.Semaphore(0)
OMP = threading.Semaphore(0)

def despachador():
    while True:
        DMG.release()
        print(DMG)
        MG.release()
        print(MG)
        #COLOCA PEDIDO
        MG.acquire()
        print(MG)
        OMG.acquire()
        print(OMG)
    


def cocinero():
    while True:
        DMH.release()
        MH.release()
        #coloca hamburguesas
        MH.acquire()
        OMH.acquire()



def empacador():
    while True:
        DMP.release()
        OMH.release()
        OMG.release()
        MP.release()
        #Surte pedido
        MP.acquire()
        MH.release()
        #coloca hamburguesa
        MH.acquire()
        MP.release()
        #coloca hamburguesa
        MG.acquire()
        DMG.acquire() 
        DMH.acquire()
        OMP.acquire()

def cajero():
    while True:
        OMP.release()
        MP.release()
        #coloca hamburguesa
        MP.release()
        DMP.release()

def main():

    hilo1.threading.Thread(target=despachador)
    hilo2.threading.Thread(target=cocinero)
    hilo3.threading.Thread(target=empacador)
    hilo4.threading.Thread(target=cajero)