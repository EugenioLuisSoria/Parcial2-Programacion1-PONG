import pygame

# Inicializar Pygame
pygame.init()

# Crear la ventana
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi primer cuadrado")

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rellenar la pantalla con un color
    screen.fill((255, 255, 255))  # Blanco

    # Dibujar el cuadrado
    pygame.draw.rect(screen, (0, 0, 255), (100, 100, 20, 20))  # Azul, en la posición (100, 100)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()