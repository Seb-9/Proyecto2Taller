import random
import socket
import threading #para poder esperar por informacion mientras se hace otra accion 

#se define un puerto para recibir info
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # se obtiene la ip del dispositvo afitrion(servidor) en la red que se encuentra
ADDR = (SERVER,PORT) #establece la direccion IPv4 y el puerto a usar en el servidor 
HEADER = 64 #cantidad de bytes aceptables en un paquete
FORMAT = "utf-8" #formato para convertir a paquetes comunicables de bytes
DISCONNECT_MESSAGE = "!DISCONNECT" #se usa para eliminar cualquier hilo en desuso de los clientes
CONNECTIONS=[]
TURNO=0
insertard=0
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr): #Controla cada instancia de cliente que ingrese
    print(f"[New connection] {addr} connected.\n")
    CONNECTIONS.append(conn)
    TURNO=CONNECTIONS.index(conn)
    connected = True
    while connected:
        if TURNO==CONNECTIONS.index(conn):
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                else:
                    answer(conn,msg,TURNO)
            
    conn.close()
def answer(conn,msg,TURNO):
    while TURNO<4:
        TURNO+=1
    else:
        TURNO=0
    if msg=="GIVE":
        answer=Cartas_jugables.pop(random.randint(0,len(Cartas_jugables)))
    if msg=="TAKE":
        answer=CARTAS_baraja[-1]
    if msg=="GIVEd":
        answer=DEFUSE.pop(-1)
        insertard+=1
    if insertard==4:
        CARTAS_jugables=CARTAS_jugables+DEFUSE
        CARTAS_baraja=CARTAS_jugables+BOMB
    else:
        answer="p"
    conn.send(answer.encode(FORMAT))
    
    
def start(): #espera por conexiones para pasarlas a handle_client
    server.listen()#escucha para las conexiones
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() #cuando una conexion se estabece, guarda la direccion y el conn funciona como un objeto para manejar multiples conexiones facilmente
        thread = threading.Thread(target=handle_client,args=(conn,addr))#genera un nuevo hilo para cada cliente que se conecte, esto para que dos se puedan conectar al mismo tiempo sin uno de los dos ser rechazado
        thread.start()#inicia el hilo anterior
        print(f"[Active connections] {threading.activeCount() - 2}")

print("Server starting...")
start()

#Se encarga de administrar las cartas, los movimientos de los jugadores
#y otros que requieran visualizacion de todos los jugadores

#CARTAS, no se cargan imagenes ya que es irrelevante, solo identificadores
#para los tipos de cartas
NOPE=["NOPE" for x in range(5)]
PASAR=["SKIP" for x in range(4)]
ATAQUE=["ATTACK" for x in range(4)]
DEFUSE=["DEFUSE" for x in range(6)]
COMODIN=["COMODIN1","COMODIN1","COMODIN1","COMODIN1","COMODIN2","COMODIN2","COMODIN2","COMODIN2","COMODIN3","COMODIN3","COMODIN3","COMODIN3","COMODIN4","COMODIN4","COMODIN4","COMODIN4","COMODIN5","COMODIN5","COMODIN5","COMODIN5"]
BOMB=["BOMB" for x in range(4)]
FAVOR=["FAVOR" for x in range(4)]
SHUFFLE=["SHUFFLE" for x in range(4)]#/barajar
STFUTURE=["STFUTURE" for x in range(5)]#/ver el futuro

CARTAS_jugables = COMODIN+STFUTURE+SHUFFLE+ATAQUE+NOPE+FAVOR+PASAR
random.shuffle(CARTAS_jugables)

 
