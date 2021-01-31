import threading


#Shop problem
#Una tienda acaba de reabrir porque hay semáforo rojo por la situación de coronavirus. Únicamente hay un 
#empleado y solamente puede haber n personas esperando a ser atendidas, puesto que el aforo máximo de la
#tienda es de n. Si ya hay n personas esperando y llega otro cliente, dicho cliente deberá retirarse del 
#lugar. El empleado únicamente podrá atender a una persona a la vez y si no hay clientes en la tienda, el 
#empleado deberá ponerse a desinfectar el lugar.

n = 10 #numero de asientos/lugares de la fila
empleadoDisponible = threading.Semaphore(1) #revisa si el empleado está disponible - boolean
a = threading.Semaphore(1) #n es el lugar indefinido de asientos/lugares de la fila
cliente = threading.Semaphore(1) #indica si el cliente ya puede ser atendido

def cliente():  #Cliente llega 
    while (True):
        if (n > 0):
            print("No hay lugares") 
    return

def empleado():  #Funciones del empleado

    return



