#Importamos la librería
import pygame

#Inicializamos
pygame.init()


class Personaje(pygame.sprite.Sprite):#se crea la clase personaje y esta heredando de la clase sprite
    def __init__(self):#metodo constructor
        pygame.sprite.Sprite.__init__(self)#metodo constructor de la clase sprite

        #Carga la imagen de la plantilla del sprite
        self.image = pygame.image.load('D:/Descargas/sprite2.png')
        self.rect = self.image.get_rect()#obtine las dimenciones de la imagen y la guarda en un rectaculo
        self.frame_actual = 0#frame actual (mono)
        self.frames = 6#total de frames que hay
        self.frame_ancho = 104#ancho del frame
        self.frame_alto = 140#alto del frame.

    #metodo actual paara hacer el movimiento del frame
    def actualizar(self, window, accion):
        #inicia el frame cero y avanza a los frame que generan movimiento
        if self.frame_actual >= self.frames - 1:
            self.frame_actual = 0
        else:
            self.frame_actual += 1
        
        # Se crea la instancia nueva_area que contendrá la imagen que corresponda de la animación según le corresponda
        nueva_area = pygame.Rect((self.frame_actual * self.frame_ancho, accion, self.frame_ancho, self.frame_alto))
        #el primer dato es la posicion x de los frame, la segunda el frame en y, los ultimos son el ancho y alto de la imagen
                                                     
        #metodo blit para poner imagen en la pantalla
        #Se coloca la imagen en la pantalla en la posición x and y, como el salto aumenta o disminuye su posicion en y se reduce en uno
        if(accion==280 or accion==840):#para saber si se esta saltando o no
            window.blit(self.image.subsurface(nueva_area), (300, 150))
            self.area = self.image.subsurface(nueva_area).get_rect()
            self.area.left = 300
            self.area.top = 150
        else:#sino pasa el if anterior significa que no esta saltando osea sigue en la misma linea del eje x and y 
            window.blit(self.image.subsurface(nueva_area), (300, 300))
            self.area = self.image.subsurface(nueva_area).get_rect()
            self.area.left = 300
            self.area.top = 300



class Obstaculo():
    def __init__(self):
        self.imagen = pygame.transform.scale(pygame.image.load('D:/Descargas/roca.png'),(50,50))
        self.area = self.imagen.get_rect()

    def actualizar(self, pantalla, x, y):
        pantalla.blit(self.imagen, (x, y))
        self.area.left = x +50
        self.area.top = y
            
        



#Definimos una estructura para el tamaño de la pantalla
tamanio = 800, 600
#Instanciamos para crear el objeto de la pantalla
pantalla1 = pygame.display.set_mode(tamanio)

#Título de la ventana
pygame.display.set_caption("Primer Juego")

#Definimos estructuras con los valores de diferentes colore en RGB
blanco = 255, 255, 255
negro = 0, 0, 0
rojo = 255, 0, 0
verde = 0, 255, 0
azul = 0, 0, 255
amarillo = 255, 255, 0
colorx = 144, 155, 120

#Define en cuantos pixeles se moverá el objeto tanto en X como en Y
velocidad = [0, 0]

#Se crea un objeto a partir de una imagen
imagenFondo = pygame.image.load("D:/Descargas/fondo1.jpg").convert()


#Creamos la instancia al personaje
personaje = Personaje()
#Creamos la instancia al obstaculo (roca)
obstaculo = Obstaculo()


#Posición del fondo
px = 0
direccion = 0
upx = px
py=0
#Bandera de ejecución
ejecucion = True
pygame.key.set_repeat(1, 10)
#Se define el loop principal
while ejecucion:
    #Se programa un retardo para darle ritmo al juego
    pygame.time.delay(48)

    #Captura de eventos
    for evento in pygame.event.get():
        #Si ocurre el evento QUIT la bandera pasa a Falso
        if evento.type == pygame.QUIT:
            ejecucion = False

       #Identifica la tecla presionada y muve el fondo.
        if evento.type == pygame.KEYDOWN:       
            #Se rellena la pantalla con un color 
            pantalla1.fill(negro)

            #coloca en la posición X = 0 y Y = 0 la imagen que servirá de fondo
            pantalla1.blit(imagenFondo, (px, 0))


            upx = px

            
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                px -= 1
                direccion = 1
                personaje.actualizar(pantalla1, 140)
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                if direccion == 1:
                    personaje.actualizar(pantalla1, 280)
                    px -= 1
                else:
                    personaje.actualizar(pantalla1, 840)
                    px += 1
            if evento.key == pygame.K_SPACE:
                if direccion == 1:
                    px -= 1
                    personaje.actualizar(pantalla1, 0)
                else:
                    px += 1
                    personaje.actualizar(pantalla1, 560)
                
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                px += 1
                direccion = 0
                personaje.actualizar(pantalla1, 700)

            obstaculo.actualizar(pantalla1, px + 700, 380)
            if obstaculo.area.colliderect(personaje.area):
                px = upx    


    #Se aplican los cambios en pantalla
    pygame.display.flip()

pygame.quit()
