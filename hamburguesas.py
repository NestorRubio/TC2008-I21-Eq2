import threading
import time
import sys



#creacion de los semaforos
MG = threading.Semaphore(1)
MH = threading.Semaphore(1)
MP = threading.Semaphore(1)
DMG = threading.Semaphore(5) #Semaforo de lugares disponibles en mesa giratoria
DMH = threading.Semaphore(8) #Semaforo de lugares disponibles en mesa de hamburguesa
DMP = threading.Semaphore(8) #Semaforo de lugares disponibles en mesa de pedidos
OMG = threading.Semaphore(0)
OMH = threading.Semaphore(0)
OMP = threading.Semaphore(0)


def despachador():
  while  True:
    DMG.acquire()
    MG.acquire()
    print("DESPACHADOR: Coloca pedido en la mesa giratoria")
    MG.release()
    OMG.release()
    time.sleep(0.5)
  


def cocinero():
  while True:
    DMH.acquire()
    MH.acquire()
    print("COCINERO: Coloca hamburguesa en la mesa de hamburguesas")
    MH.release()
    OMH.release()
    time.sleep(0.5)



def empacador():
  while True:
    DMP.acquire()
    OMH.acquire()
    OMG.acquire()
    MP.acquire()
    print("EMPACADOR: recoge orden de la mesa giratoria")
    MP.release()
    MH.acquire()
    print("EMPACADOR: recoge hamburguesa de la mesa de hamburguesa")
    MH.release()
    MP.acquire()
    print("EMPACADOR: Coloca hamburguesa en la mesa de pedidos")
    MG.release()
    DMG.release() 
    DMH.release()
    OMP.release()
    MP.release()
    time.sleep(0.5)

def cajero():
  while True:
    OMP.acquire()
    MP.acquire()
    print("CAJERO: recoge hamburguesa de la mesa de pedidos y la entrega al cliente")
    MP.release()
    DMP.release()
    time.sleep(0.5)

def main():

  hilo1=threading.Thread(target=despachador, daemon=True)
  hilo1.start()
  time.sleep(0.5)

  hilo2=threading.Thread(target=cocinero, daemon= True)
  hilo2.start()
  time.sleep(0.5)

  hilo3=threading.Thread(target=empacador, daemon= True)
  hilo3.start()
  time.sleep(0.5)

  hilo4=threading.Thread(target=cajero, daemon= True)
  hilo4.start()
  time.sleep(0.5)

  sys.exit

main()
