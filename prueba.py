import threading 
n = 5
e = threading.Semaphore(5) # proceso que falta por producir 
f =  threading.Semaphore(0) # procesos disponibles para que consumidor
b =  threading.Semaphore(1) # indica si el buffer esta en uso
bff = list()

def productor():
    while(True):
        dato = "a"
        e.acquire() # P(e) e-1
        b.acquire() # se esta usando el buffer
        print("anadiendo dato al buffer en la pos", len(bff))
        print ("Semaforo e", e._value,b._value)
        bff.append(dato)
        b.release() #v(b)
        f.release() #v(b)

def consumidor():
    while(True):
        f.acquire() 
        b.acquire() # se esta usando el buffer
        print("eliminando dato al buffer en la pos", len(bff)-1)
        print (e._value,b._value)
        bff.pop()
        b.release() #v(b)
        e.release() #v(e)

def main():
    hilo1=threading.Thread(target=productor)
    hilo2=threading.Thread(target=consumidor)
    hilo1.start()
    hilo2.start()


main()

