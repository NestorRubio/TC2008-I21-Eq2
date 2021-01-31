import threading 

p = threading.Semaphore(2) # proceso que falta por producir 
c =  threading.Semaphore(0) # procesos disponibles para que consumidor
bff = list()

def productor():
    while(True):
        print ("Valor del semaforo p: ", p._value)
        print ("Valor del semaforo c: ", c._value)
        dato = "a"
        p.acquire() # P(SP)
        print("Producto enviado al buffer")
        bff.append(dato)
        c.release() #v(SC)
        print ("Valor del semaforo p: ", p._value)
        print ("Valor del semaforo c: ", c._value)

def consumidor():
    while(True):
        c.acquire() #V(SC)
        c.acquire() #V(SC)
        print("Dos datos tomados por el consumidor")
        bff.pop()
        bff.pop()
        p.release() #V(SP)
        p.release() #V(SP)
        print ("Valor del semaforo p: ", p._value)
        print ("Valor del semaforo c: ", c._value)

def main():
    hilo1=threading.Thread(target=productor)
    hilo2=threading.Thread(target=consumidor)
    hilo1.start()
    hilo2.start()



main()
