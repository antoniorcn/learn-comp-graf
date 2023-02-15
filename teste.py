import pygame
import math

pygame.init()

p1 = [100, 100]
p2 = [200, 200]

[[0, sin(30), 0],
[1, cos(30), 1],
]

[70, 70]

pontos = [p1, p2]

screen = pygame.display.set_mode([800, 600], 0)

while True:
    # Processar os dados

    # Mostrar as coisas na tela
    for p in pontos:
        x = p[0] * math.cos(30 * math.pi / 180)
        y = p[1] * math.sin(30 * math.pi / 180)
        novo_p = [x, y]
        print(novo_p)
        pygame.draw.circle(screen, (255, 255, 0), p, 10, 0)
        pygame.draw.circle(screen, (0, 255, 0), novo_p, 5, 0)
    pygame.display.update()

    # Capturar eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()


