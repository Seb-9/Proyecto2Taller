##import socket
##
##s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##s.connect((socket.gethostname(),1234))
##full_msg=""
##while True:
##    msg =  s.recv(8)
##    if len(msg)<=0:
##        break
##    full_msg += msg.decode("utf-8")
##print(full_msg)

import socket
import pygame
import random
from pygame.locals import *

HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
SERVER = "192.168.1.159" 
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # IPv4 y TCP
client.connect(ADDR)
print(f"[Connected]")
thread = threading.Thread(target=handle_Server,args=())#genera un nuevo hilo para cada cliente que se conecte, esto para que dos se puedan conectar al mismo tiempo sin uno de los dos ser rechazado
thread.start()#inicia el hilo anterior
def send(msg):
    message = msg.encode(FORMAT)#Se debe codificar en un formato transferible(utf-8)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))#se rellenan los espacios vacios
                                                     #necesarios para el largo que acepta el server en el mensaje
    client.send(send_length)
    client.send(message)

#while True:
 #   text = input()
  #  send(text)

def handle_server(): #Controla cada instancia de cliente que ingrese
    #print(f"[New connection] {addr} connected.\n")
    connected = True
    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            main(msg)

            #conn.send(msg.encode(FORMAT))
        #send(msg)
            
    conn.close()
FONDO = (0, 0, 0)
BLANCO = (255, 255, 255)
COLOR_TEXTO = (50, 60, 80)

pygame.init()
dimensiones = [1200, 650]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Explodin Kittens")
imagen_panel = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/bgimg.png")
imagen_boton = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/nikeimg.png")
imagen_boton_pressed = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/icono.png")
imagen_boton_cuadro = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/BOMB.png")
imagen_boton_cuadro_pressed = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/DEFUSE.png")
imagen_text = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/NOPE.png")
fuente = pygame.font.SysFont('Courier', 20)
fuente_numero = pygame.font.SysFont('Pacifico Regular', 30)

COMODIN1 = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/COMODIN1.png")
COMODIN2 = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/COMODIN2.png")
COMODIN3 = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/COMODIN3.png")
COMODIN4 = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/COMODIN4.png")
COMODIN5 = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/COMODIN5.png")
NOPE = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/NOPE.png")
FAVOR = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/FAVOR.png")
SKIP = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/SKIP.png")
BOMB = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/BOMB.png")
DEFUSE = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/DEFUSE.png")
SHUFFLE = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/SHUFFLE.png")
STFUTURE = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/SEETHEFUTURE.png")
ATTACK = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/ATTACK.png")

COMODIN1p = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/COMODIN1p.png")
COMODIN2p = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/COMODIN2p.png")
COMODIN3p = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/COMODIN3p.png")
COMODIN4p = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/COMODIN4p.png")
COMODIN5p = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/COMODIN5p.png")
NOPEp = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/NOPEp.png")
FAVORp = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/FAVORp.png")
SKIPp = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/SKIPp.png")
BOMBp = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/BOMBp.png")
DEFUSEp = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/DEFUSEp.png")
SHUFFLEp = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/SHUFFLEp.png")
STFUTUREp = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/SEETHEFUTUREp.png")
ATTACKp = pygame.image.load("C:/Users/sebas/Desktop/Proyecto2Intro/ATTACKp.png")

img_cartas = (ATTACK, DEFUSE, SKIP, SHUFFLE, STFUTURE, FAVOR, NOPE, COMODIN1, COMODIN2, COMODIN3, COMODIN4, COMODIN5)
img_cartas_p = (ATTACKp, DEFUSEp, SKIPp, SHUFFLEp, STFUTUREp, FAVORp, NOPEp, COMODIN1p, COMODIN2p, COMODIN3p, COMODIN4p, COMODIN5p)
img_nombres = ("ATTACK", "DEFUSE", "SKIP", "SHUFFLE", "STFUTURE", "FAVOR", "NOPE", "COMODIN1", "COMODIN2", "COMODIN3", "COMODIN4", "COMODIN5")
cartas_jugador = []

botones=[]

def dibujar_texto(texto, contenedor_imagen, contenedor_rec, fuente_render, color):
    text = fuente_render.render(texto, 1, color)
    centro = text.get_rect()
    diferencia_x = contenedor_imagen.center[0] - centro.center[0]
    diferencia_y = contenedor_imagen.center[1] - centro.center[1]
    pantalla.blit(text, [contenedor_rec.left + diferencia_x, contenedor_rec.top + diferencia_y])


def generar_numero():
    numero = str(random.randint(1, 4)) + str(random.randint(1, 4)) + str(random.randint(1, 4)) + str(random.randint(1, 4))
    return numero


def dibujar_botones_iniciales(lista_botones):
    panel = pygame.transform.scale(imagen_panel, [1160, 610])
    pantalla.blit(panel, [20, 20])
    for boton in botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])
        #dibujar_texto(boton['texto'], boton['imagen'].get_rect(), boton['rect'], fuente, BLANCO)


def set_text(campo, texto):
    dibujar_texto(texto, campo['imagen'].get_rect(), campo['rect'], fuente_numero, COLOR_TEXTO)

def reajuste(x, largo):
    x -= 45*largo
    for boton in botones:
        carta = img_cartas.index(cartas_jugador[boton-1])
        carta_cuadro = pygame.transform,scale(img_cartas[carta], [90,90])
        carta_cuadro_p = pygame.transfrom.scale(img_cartas_p[carta], [90,90])
        rect_carta = carta_cuadro.get_rect()
        rect_carta.topleft = [x,520]
        x += 90 # se le suma el largo de la carta para posicionar la siguiente carta a la par
        botones[boton]=({'texto': "", 'imagen': carta_cuadro, 'imagen_pressed': carta_cuadro_p, 'rect': rect_carta, 'on_click': False}) # la info de esa carta se debe actualizar
        

def nueva_carta(carta, cartap, x, y):
    carta_cuadro = pygame.transform.scale(carta, [90,90]) # se hace un ajuste de la imagen al cuadro
    carta_cuadro_p = pygame.transfrom.scale(cartap, [90,90]) # lo mismo pero para la imagen presionada respectiva
    boton = carta_cuadro.get_rect() # toma las dimensiones de la caja de la imagen 
    boton.topleft = [x,y] #se pone aqui temporalmente, reajuste() la ajusta con todas las demas cartas para lograr una simetria en la pantalla
    botones.append({"texto":"","imagen":carta,"imagen_pressed":cartap, "rect": boton, "on_cick": False})
    cartas_jugador.append(carta)
    #reajuste(botones, x, len(botones))

##def entrada(msg):
    ##se descompone el mensaje del servidor
    ##index

def main(carta):
    game_over = False ##si
    clock = pygame.time.Clock() ##si

    boton_cuadro = pygame.transform.scale(imagen_boton_cuadro, [90, 90]) ##si
    boton_cuadro_pressed = pygame.transform.scale(imagen_boton_cuadro_pressed, [90, 90]) ##si
    input_text = pygame.transform.scale(imagen_text, [440, 50]) ##si

##------activar esto------##
    if carta!="":
        indice = img_nombres.index(carta) # el argumento "carta" viene del mensaje del servidor
        nueva_carta(img_cartas[indice],img_cartas_p[indice],1000, 520)
        reajuste(600, len(botones))
##---------:3---------##


    
##    r_boton_1_1 = imagen_boton.get_rect()
##    r_boton_1_2 = imagen_boton.get_rect()
##    r_boton_2_1 = boton_cuadro.get_rect()
##    r_boton_2_2 = boton_cuadro.get_rect()
##    r_boton_2_3 = boton_cuadro.get_rect()
##    r_boton_2_4 = boton_cuadro.get_rect()
##
##    input_text_rect = input_text.get_rect() ##si
    
    #input_text_rect.topleft = [80, 360] ##si
    #campo_texto = {'imagen': input_text, 'rect': input_text_rect} ##si
    
##    r_boton_1_1.topleft = [0, 0]
##    botones.append({'texto': "Nuevo número", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_1, 'on_click': False})
##    r_boton_1_2.topleft = [330, 80]
##    botones.append({'texto': "Confirmar", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_2, 'on_click': False})
##    r_boton_2_1.topleft = [80, 80]
##    botones.append({'texto': "1", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_1, 'on_click': False})
##    r_boton_2_2.topleft = [200, 180]
##    botones.append({'texto': "2", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_2, 'on_click': False})
##    r_boton_2_3.topleft = [320, 180]
##    botones.append({'texto': "3", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_3, 'on_click': False})
##    r_boton_2_4.topleft = [430, 180]
##    botones.append({'texto': "4", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_4, 'on_click': False})


    click = False
   # mostrar_numero = 0
   # numero_aleatorio = 0
    #texto_entrada = ""
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
                send(DISCONNECT_MESSAGE)
                
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
                
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False

        if botones[0]['on_click'] and click:
            numero_aleatorio = generar_numero()
            texto_entrada = ""
            mostrar_numero = 10
            click = False

        pantalla.fill(FONDO)
        dibujar_botones_iniciales(botones)
        pantalla.blit(input_text, campo_texto['rect'].topleft)

        if click and botones[1]['on_click']:
            if texto_entrada == numero_aleatorio:
                texto_entrada = "Congratulations!"
            else:
                texto_entrada = "Error!"
            click = False
        if click:
            for i in range(2, 6):
                if botones[i]['on_click'] and len(texto_entrada) < 4:
                    texto_entrada += botones[i]['texto']
            click = False
        #if mostrar_numero > 0:
         #   dibujar_texto(numero_aleatorio, pygame.Surface([100, 40]).get_rect(), pygame.Rect([260, 300, 102, 42]), fuente_numero, COLOR_TEXTO)
          #  mostrar_numero -= 1

        #set_text(campo_texto, texto_entrada)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()    
    
#se declaran todas las cartas

