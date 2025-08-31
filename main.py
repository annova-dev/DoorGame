import sys
import pygame
from pygame.locals import *

pygame.init()

# Tela do jogo
tela = pygame.display.set_mode((1000, 600))
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)
pygame.display.set_caption("DoorGame")

# CORES
branco = (255, 255, 255)
preto = (0, 0, 0)
magenta = (155, 19, 90)

tela.fill(branco)

# Texto
fonte = pygame.font.SysFont("bahnschrift", 64)
print(pygame.font.get_fonts())
label = fonte.render("Bem vindo ao jogo da porta!", 1, preto)

# Criterio de parada
done = False

# ------------- Main –-------------
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
            pygame.quit()
            sys.exit()

        tela.blit(label, (30, 30))

    pygame.display.update()