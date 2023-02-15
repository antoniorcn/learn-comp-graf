import pygame

pygame.init()

p1 = [60, 60]

screen = pygame.display.set_mode([800, 600], 0)

while True:
    # Processar os dados

    # Mostrar as coisas na tela

    # Capturar eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()



