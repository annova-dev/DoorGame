import sys
import pygame
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
from game import porta

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
amarelo_claro = (255, 255, 200)

tela.fill(branco)

# IMAGENS

porta1 = pygame.image.load("Porta1.png")
porta2 = pygame.image.load("Porta2.png")
porta3 = pygame.image.load("Porta3.png")
porta1_aberta = pygame.image.load("imagens/Porta1_open.png")
porta2_aberta = pygame.image.load("imagens/Porta2_open.png")
porta3_aberta = pygame.image.load("imagens/Porta3_open.png")
# cats
dottie = pygame.image.load("imagens/dottie.png")
bartolomew = pygame.image.load("imagens/bartolomew.png")
sunny = pygame.image.load("imagens/sunny.png")
#cats on the door
dottie_door = pygame.image.load("imagens/dottiedoor.png")
bart_door = pygame.image.load("imagens/bartdoor.png")
sunny_door = pygame.image.load("imagens/sunnydoor.png")

#variaveis do jogo

# Texto
fonte = pygame.font.SysFont("bahnschrift", 64)
#print(pygame.font.get_fonts())
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
done = True

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bb1.collidepoint(event.pos):
                jogo_quit = False
                menu_done = True

            if bb2.collidepoint(event.pos):
                Tk().wm_withdraw()
                messagebox.showinfo('REGRAS',
                                    'Tente adivinhar a porta! Você terá que adivinhar a porta que seu gato está. Escolha entre 3 portas, depois da primeira escolha, uma das portas em que seu gato NÃO está será removida. Depois você terá que escolher, se troca a porta ou se a mantém. Boa sorte!')

            if bb3.collidepoint(event.pos):
                jogo_quit = 0
                menu_done = True
                pygame.quit()
                sys.exit()

        if event.type == QUIT:
            done = True
            pygame.quit()
            sys.exit()


    # Criterio de parada

    pygame.display.update()

#Variaveis do jogo
porta1_fechada = True
porta2_fechada = True
porta3_fechada = True
# Variar dependendo do gato
cat = {dottie: dottie}

# ------------- Jogo –-------------
while not jogo_quit:
    tela.fill(amarelo_claro)
    mouse = pygame.mouse.get_pos()

    if porta1_fechada:
        porta1_b = porta1.get_rect(topleft=(2 * x / 9, 300))
        tela.blit(porta1, porta1_b)
        pygame.draw.rect(tela, branco, porta1_b, 1)

    if porta2_fechada:
        porta2_b = porta2.get_rect(topleft=(4 * x / 9, 300))
        tela.blit(porta2, porta2_b)
        pygame.draw.rect(tela, preto, porta2_b, 1)

    if porta3_fechada:
        porta3_b = porta3.get_rect(topleft=(6 * x / 9, 300))
        tela.blit(porta3, porta3_b)
        pygame.draw.rect(tela, magenta, porta3_b, 1)

    print(porta1_fechada)
    #Escolha da porta
    if porta1_fechada == False:
        tela.blit(dottie_door, (2.45*x / 9, 430))
        tela.blit(porta1_aberta, (2*x / 9, 270))

    elif porta2_fechada == False:
        tela.blit(porta2_aberta, (4*x / 9, 300))

    elif porta3_fechada == False:
        tela.blit(porta3_aberta, (6*x / 9, 300))

    #Tornando as portas clicaveis

    for event in pygame.event.get():
        if event.type == QUIT:
            jogo_quit = True
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("CLICK")
            if porta1_b.collidepoint(event.pos):
                porta1_fechada = False
            elif porta2_b.collidepoint(event.pos):
                porta2_fechada = False
            elif porta3_b.collidepoint(event.pos):
                porta3_fechada = False

    #porta = porta()


    pygame.display.update()

