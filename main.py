import pygame as py
import random
py.init()

# Configuración de la pantalla 
screen = py.display.set_mode((800, 600))
py.display.set_caption("Ochento´s Pong")



# CLASES:
class Player1:
    def __init__(self):
        # Dibujar PALETA IZQUIERDA
        self.dimentions_x = 20
        self.dimentions_y = 100
        self.x = 50 # Posicion inicial en x
        self.y = 250 # Posicion inicial en y
        self.y_change = 0 # Cambio de posición por movimiento 
        self.color = (255, 255, 255)

    def draw(self):
        # Dibujar PALETA IZQUIERDA:
        self.image = py.draw.rect(screen, self.color, (self.x, self.y, self.dimentions_x, self.dimentions_y)) 

    def move(self):
        # Actualizar la posición
        self.y += self.y_change
        # Limitar el movimiento dentro de los limites de la pantalla
        if self.y <= 0:
            self.y = 0
        elif self.y >= 500: # 600 menos el largo de la paleta
            self.y = 500

class Player2:
    def __init__(self):
        # Dibujar PALETA IZQUIERDA
        self.dimentions_x = 20
        self.dimentions_y = 100
        self.x = 750 # Posicion inicial en x
        self.y = 250 # Posicion inicial en y
        self.y_change = 0 # Cambio de posición por movimiento 
        self.color = (255, 255, 255)

    def draw(self):
        # Dibujar PALETA IZQUIERDA:
        self.image = py.draw.rect(screen, self.color, (self.x, self.y, self.dimentions_x, self.dimentions_y)) 

    def move(self):
        # Actualizar la posición
        self.y += self.y_change
        # Limitar el movimiento dentro de los limites de la pantalla
        if self.y <= 0:
            self.y = 0
        elif self.y >= 500: # 600 menos el largo de la paleta
            self.y = 500

class Ball:
    def __init__(self):
        # Dibujar PALETA IZQUIERDA
        self.dimentions_x = 20
        self.dimentions_y = 20
        self.x = 390 # Posicion inicial en x
        self.y = 290 # Posicion inicial en y
        self.x_change = 0 # Cambio de posición por movimiento 
        self.y_change = 0 # Cambio de posición por movimiento 
        self.color = (255, 255, 255)

    def draw(self):
        self.image = py.draw.rect(screen, self.color, (self.x, self.y, self.dimentions_x, self.dimentions_y)) 

    def move(self):
        self.x += self.x_change
        # Cambiar de dirección
        if self.x <= 0 or self.x >= 736:
            self.x_change *= -1 # Cambio de dirección
            self.y += self.y_change # Bajar al cambiar de dirección
        
    """ def reset_posicion(self, speed):
        # Reiniciar posición aleatoria para simular un nuevo enemigo
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        self.x_change = speed """

player1 = Player1()
player2 = Player2()
ball = Ball()

# Bucle principal del juego
running = True
while running:
    # Rellenar la pantalla con un color
    screen.fill((0, 0, 0))  # Negro
    
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False 
            
        # Detectar si se presiona un tecla
        if event.type == py.KEYDOWN: # Solo teclas
            if event.key == py.K_w:
                player1.y_change = -1 # Valor de velocidad
            elif event.key == py.K_s:
                player1.y_change = 1 # Velocidad de jugador
            if event.key == py.K_UP:
                player2.y_change = -1 # Valor de velocidad
            elif event.key == py.K_DOWN:
                player2.y_change = 1 # Velocidad de jugador

        # Detectar si se suelta la tecla
        if event.type == py.KEYUP:
            if event.key == py.K_w or event.key == py.K_s:
                player1.y_change = 0
            if event.key == py.K_UP or event.key == py.K_DOWN:
                player2.y_change = 0
                
            
    #if True: #not game_over:
        # Mover y dibujar el jugador
    player1.move()
    player2.move()        
    player1.draw()        
    player2.draw()        
    ball.draw()

    # Actualizar la pantalla
    py.display.flip()

# Salir de Pygame
py.quit()

