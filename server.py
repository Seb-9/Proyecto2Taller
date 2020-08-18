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

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr): #Controla cada instancia de cliente que ingrese
    print(f"[New connection] {addr} connected.\n")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
            print(f"[{addr}] {msg}")
            #conn.send(msg.encode(FORMAT))
            if msg == "STFUTURE":

            if msg == "DEFUSE"
        send(msg,conn)
            
    conn.close()

def send(msg,conn):
    message = msg.encode(FORMAT)#Se debe codificar en un formato transferible(utf-8)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))#se rellenan los espacios vacios
                                                     #necesarios para el largo que acepta el cliente en el mensaje
    conn.send(send_length)
    conn.send(message)
    
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

####Parte del juego###
#Se encarga de administrar las catas, los movimientos de los jugadores
#y otros que requieran visualizacion de todos los jugadores

#CARTAS, no se cargan imagenes ya que es irrelevante, solo identificadores
#para los tipos de cartas
NOPE=[n1,n2,n3,n4,n5]
PASAR=[p1,p2,p3,p4]
ATAQUE=[a1,a2,a3,a4]
DEFUSE=[d1,d2,d3,d4,d5,d6]
COMODIN=[c11,c12,c13,c14,c21,c22,c23,c24,c31,c32,c33,c34,c41,c42,c43,c44,c51,c52,c53,c54]
BOMB=[b1,b2,b3,b4]
FAVOR=[f1,f2,f3,f4]
SHUFFLE=[s1,s2,s3,s4]#/barajar
STFUTURE=[stf1,stf2,stf3,stf4,stf5]#/ver el futuro

CARTAS_baraja = DEFUSE+COMODIN+BOMB+FAVOR+SHUFFLE+STFUTURE
CARTAS_jugables = DEFUSE+COMODIN
#cuando cada cliente se conecte, y se inicie el juego, se hacen los ajustes
#a la cantidad de cartas que se repartiran en el mazo
#se le dad a cada uno una respuesta con cartas

#for jugador in jugadores:
    # reparticion de cartas
#while limite>0:
	#i=random.randint(0,10)
        #j=random.randint(0,10)
        #jcartas.append(cartas[i][j])
	#limite-=1
#mezcla de la baraja
    #random.shuffle(baraja)

 