import sys
import pygame
from pygame.font import get_fonts
from pygame.locals import *

pygame.init()

# Tela do jogo
x=1280
y=720
tela = pygame.display.set_mode((x, y))
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)
pygame.display.set_caption("DoorGame")

# CORES
branco = (255, 255, 255)
preto = (0, 0, 0)
magenta = (155, 19, 90)
magenta_claro = (170, 39, 98, 50)
rosa_claro = (200, 39, 98, 50)

tela.fill(branco)

# Texto
fonte = pygame.font.SysFont("bahnschrift", 64)
print(pygame.font.get_fonts())
label = fonte.render("Bem vindo ao jogo da porta!", 1, preto)
titulo = pygame.image.load("Doorgamelogo.png")

def inserir_texto(texto, fonte, cor, x,y):
    tex = fonte.render(texto, 1, cor)
    tela.blit(tex, (x,y))

def botao(cor, tam):
    pygame.draw.rect(tela, cor, tam)

def press(bo, tamanho):
    mouse = pygame.mouse.get_pos()
    if bo.collidepoint(mouse):
        botao(rosa_claro, tamanho)
    else:
        botao(magenta_claro, tamanho)

#MENU

b1 = (3*x/7, 345, 208, 55)
b2 = (3*x/7, 435, 208, 55)
b3 = (3*x/7, 525, 208, 55)
esc_font = pygame.font.SysFont('Verdana', 20)

jogo = esc_font.render("INICIAR", True, branco)
regras = esc_font.render("REGRAS", True, branco)
sair = esc_font.render("  SAIR", True, branco)

#--------------- Menu ---------------
menu_done = False

while not menu_done:
    tela.fill(magenta)
    mouse = pygame.mouse.get_pos()

    tela.blit(titulo, (x/3-5, 100))
    bb1 = pygame.Rect(b1)
    botao(preto, b1)
    bb2 = pygame.Rect(b2)
    botao(preto, b2)
    bb3 = pygame.Rect(b3)
    botao(preto, b3)

    press(bb1, b1)
    press(bb2, b2)
    press(bb3, b3)

    tela.blit(jogo, (3*x/7+62, 360))
    tela.blit(regras, (3*x/7+62, 450))
    tela.blit(sair, (3*x/7+65, 540))

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
            pygame.quit()
            sys.exit()

    #tela.blit(label, (30, 30))

    # Criterio de parada
    done = False
    pygame.display.update()
"""
# ------------- Jogo –-------------
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
            pygame.quit()
            sys.exit()

        tela.blit(label, (30, 30))
"""
