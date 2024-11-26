import pygame as py
import random, time
py.init()

#Configuraciones
ANCHO, ALTO = 800, 600
SCREEN = py.display.set_mode((ANCHO, ALTO))
py.display.set_caption("Ochento´s Pong")
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
FUENTE = py.font.Font(None, 56)  # Fuente para los puntos

#CLASES:
class Player:
    def __init__(self, init_x):
        self.position = ALTO / 2 - 50
        self.paleta = py.Rect(init_x, self.position, 20, 100)
        self.speed = 0
        self.color = BLANCO
        self.score = 0  # Puntos del jugador

    def draw(self, score_ubication_x, score_ubication_y):
        py.draw.rect(SCREEN, self.color, self.paleta)
        #Puntaje
        score_text = FUENTE.render(f"{self.score}", True, BLANCO)
        SCREEN.blit(score_text, (score_ubication_x, score_ubication_y))

    def move(self):
        self.position += self.speed
        if self.position <= 0:
            self.position = 0
        elif self.position >= 500:
            self.position = 500
        self.paleta.y = self.position

class Ball:
    def __init__(self):
        self.ball = py.Rect(ANCHO / 2 - 10, ALTO / 2 - 10, 20, 20)
        self.color = BLANCO
        self.reset_ball() #ANDA? 

    def reset_ball(self):
        self.ball.x = ANCHO / 2 - 10
        self.ball.y = ALTO / 2 - 10
        #Direcciones iniciales
        dx = random.choice([-2, 2])
        dy = random.choice([-2, -1, 1, 2])
        #Asegurar que dx y dy no resulten en un movimiento puramente horizontal o vertical
        while dx == 0 or dy == 0 or (dx == dy):
            dx = random.choice([-2, 2])
        dy = random.choice([-2, -1, 1, 2])
        self.direction = [dx, dy]

    def draw(self):
        py.draw.rect(SCREEN, self.color, self.ball)

    def move(self, player1, player2):
        #Posicion
        self.ball.x += self.direction[0]
        self.ball.y += self.direction[1]

        #Rebote en bordes
        if self.ball.y <= 0 or self.ball.y >= ALTO - 20:
            self.direction[1] = -self.direction[1]

        #Rebote en paletas
        if self.ball.colliderect(player1.paleta) or self.ball.colliderect(player2.paleta):
            self.direction[0] = -self.direction[0]

        #Punto para Player2
        if self.ball.x <= 0:
            player2.score += 1
            self.reset_ball()

        #Punto para Player1
        if self.ball.x >= ANCHO - self.ball.width:
            player1.score += 1
            self.reset_ball()


#Bucle principal del juego
player1 = Player(50)
player2 = Player(700)
ball = Ball()
reloj = py.time.Clock()
running = True
while running:
    SCREEN.fill(NEGRO)  

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

        #Comandos:
        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                player1.speed = -3
            elif event.key == py.K_s:
                player1.speed = 3
            if event.key == py.K_UP:
                player2.speed = -3
            elif event.key == py.K_DOWN:
                player2.speed = 3
                
            if event.key == py.K_r: #RESETEO
                player1.score = 0
                player2.score = 0
                reset_text = FUENTE.render("RESETEANDO", True, BLANCO)
                SCREEN.blit(reset_text, (ANCHO/ 3, ALTO / 2 - 15))
                py.display.flip()
                time.sleep(1)

        if event.type == py.KEYUP:
            if event.key in [py.K_w, py.K_s]:
                player1.speed = 0
            if event.key in [py.K_UP, py.K_DOWN]:
                player2.speed = 0

    #GANADOR ?
    if player1.score == 10:
            ganador_text = FUENTE.render(f"WINNER PLAYER 1", True, BLANCO)
            SCREEN.blit(ganador_text, (ANCHO/ 3, ALTO / 2 - 15))
            py.display.flip()
            time.sleep(2)
            SCREEN.fill(NEGRO)  
            game_over = FUENTE.render(f"GAME OVER", True, BLANCO)
            SCREEN.blit(game_over, (ANCHO/ 3, ALTO / 2 - 15))
            py.display.flip()
            time.sleep(2)
            SCREEN.fill(NEGRO)  
            
    elif player2.score == 10:
            ganador_text = FUENTE.render(f"WINNER PLAYER 2", True, BLANCO)
            SCREEN.blit(ganador_text, (ANCHO/ 3, ALTO / 2 - 15))
            py.display.flip()
            time.sleep(2)
            SCREEN.fill(NEGRO)  
            game_over = FUENTE.render(f"GAME OVER", True, BLANCO)
            SCREEN.blit(game_over, (ANCHO/ 3, ALTO / 2 - 15))
            py.display.flip()
            time.sleep(2)
            SCREEN.fill(NEGRO)  
            break
    
    #Actualizar y dibujar objetos
    player1.move()
    player2.move()
    ball.move(player1, player2)
    #LOS PARAMETREOS SON PARA UBICAR EL SCORE EN PANTALLA
    player1.draw(50, 10)
    player2.draw(ANCHO - 200, 10)
    ball.draw()
    #py.draw.line(SCREEN, BLANCO, (ANCHO // 2, 0), (ANCHO // 2, ALTO), 2) #RED? como hacerla punteada?
    
    py.display.flip()
    reloj.tick(160)

py.quit()
