import sys
import pygame
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
from game import porta

pygame.init()
clock = pygame.time.Clock()

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
rosa_mais_claro = (255, 153, 153)
amarelo_claro = (255, 255, 200)

tela.fill(branco)

# IMAGENS

porta1 = pygame.image.load("Porta1.png")
porta2 = pygame.image.load("Porta2.png")
porta3 = pygame.image.load("Porta3.png")
lista_portas = ['Porta1', 'Porta2', 'Porta3']

#cats on the door
dottie_door = pygame.image.load("imagens/dottiedoor.png")
bart_door = pygame.image.load("imagens/bartdoor.png")
sunny_door = pygame.image.load("imagens/sunnydoor.png")

#variaveis do jogo

# Texto
fonte = pygame.font.SysFont("bahnschrift", 64)
fonte2 = pygame.font.SysFont("bahnschrift", 32)
fonte3 = pygame.font.SysFont("bahnschrift", 20)
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

def popup():
    popup_rect = pygame.Rect(300, 100, 500, 200)
    pygame.draw.rect(tela, rosa_mais_claro, popup_rect)
    pygame.draw.rect(tela, magenta, popup_rect, 5)
    text = fonte2.render("Jogar novamente?", True, branco)
    tela.blit(text, (popup_rect.x + 50, popup_rect.y + 80))
    #botoes
    botao1 = (popup_rect.x + 290, popup_rect.y + 130, 80, 40)
    botao(magenta, botao1)
    b1 = pygame.Rect(botao1)
    press(b1, botao1)
    sim = fonte3.render("Sim", True, branco)
    tela.blit(sim, (popup_rect.x + 310, popup_rect.y + 140))

    botao2 = (popup_rect.x + 380, popup_rect.y + 130, 80, 40)
    botao(magenta, botao2)
    b2 = pygame.Rect(botao2)
    press(b2, botao2)
    sair = fonte3.render("Não", True, branco)
    tela.blit(sair, (popup_rect.x + 405, popup_rect.y + 140))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b1.collidepoint(event.pos):
                reescolha = False
                menu_done = False

            if b2.collidepoint(event.pos):
                jogo_quit = 0
                reescolha = False
                pygame.quit()
                sys.exit()

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
                cat_chosen = False
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

# TELA DE ESCOLHA DO GATO - Primeira etapa

# cats - para escolha
bartolomiau = pygame.image.load("imagens/bartolomiau.png")
dottie = pygame.image.load("imagens/dottie.png")
sunny = pygame.image.load("imagens/sunny.png")
cats = {'bartolomiau':bart_door, 'dottie':dottie_door, 'sunny':sunny_door}

while not cat_chosen:
    tela.fill(magenta_claro)
    mouse = pygame.mouse.get_pos()

    inserir_texto("Escolha um gato para adotar!", fonte, branco,225,150 )

    # Gato Barto
    bart_choice = bartolomiau.get_rect(topleft=(2 * x / 9, 300))
    tela.blit(bartolomiau, bart_choice)
    # pygame.draw.rect(tela, branco, bart_choice, 1)

    # Gato Sunny
    sunny_choice = sunny.get_rect(topleft=(4 * x / 9, 300))
    tela.blit(sunny, sunny_choice)

    # Gato Dottie
    dottie_choice = dottie.get_rect(topleft=(6 * x / 9, 325))
    tela.blit(dottie, dottie_choice)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:

            #Escolha dos gatos
            if bart_choice.collidepoint(event.pos):
                parte1 = True
                cat = "bartolomiau"
                cat_chosen = True

            if sunny_choice.collidepoint(event.pos):
                parte1 = True
                cat = 'sunny'
                cat_chosen = True

            if dottie_choice.collidepoint(event.pos):
                parte1 = True
                cat = 'dottie'
                cat_chosen = True

        if event.type == QUIT:
            done = True
            pygame.quit()
            sys.exit()
    pygame.display.update()

# Variaveis do jogo - NENHUMA PORTA FOI ESCOLHIDA AINDA // ALOCANDO O GATO ESCOLHIDO A UMA DAS PORTAS
porta1_fechada = True
porta2_fechada = True
porta3_fechada = True

ans,ran = porta(cat)
print(ans,ran)

chosen_cat = cats.pop(str(cat))
print(cats, chosen_cat)

# ------------- Jogo –-------------
# Primeira escolha, entre as 3 portas
while parte1:

    tela.fill(amarelo_claro)
    mouse = pygame.mouse.get_pos()

    inserir_texto("Opa! Seu gato será seu se adivinhar em que porta ele está!", fonte2, magenta, 225, 150)

    # Portas fechadas para escolha
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

    '''
    #Abertura da porta escolhida
    if porta1_fechada == False:
        tela.blit(porta1_aberta, (2*x / 9, 270))

    if porta2_fechada == False:
        tela.blit(porta2_aberta, (4*x / 9, 300))

    elif porta3_fechada == False:
        tela.blit(porta3_aberta, (6*x / 9, 300))
    '''

    #Tornando as portas clicaveis e passando a porta escolhida
    for event in pygame.event.get():
        if event.type == QUIT:
            jogo_quit = True
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("CLICK")
            if porta1_b.collidepoint(event.pos):
                reescolha = True
                portaescolhida = "Porta1"
                parte1 = False

            elif porta2_b.collidepoint(event.pos):
                reescolha = True
                portaescolhida = "Porta2"
                parte1 = False

            elif porta3_b.collidepoint(event.pos):
                reescolha = True
                portaescolhida = "Porta3"
                parte1 = False

    #porta = porta()
    pygame.display.update()

#TELA DE RE-ESCOLHA DE PORTA ----------------------------------------------
# parte 2 do jogo!
popup_tempo = 3000
popup_on = False
start_time = 999999999

while reescolha:
    tela.fill(rosa_claro)
    mouse = pygame.mouse.get_pos()
    lista_fechadas = [porta1_fechada, porta2_fechada, porta3_fechada]

    # Exibindo as portas não escolhidas como fechadas, e abrindo uma das que não foram escolhidas mas que não contem o gato certo
    if porta1_fechada:
        porta1_b = porta1.get_rect(topleft=(2 * x / 9, 300))
        tela.blit(porta1, porta1_b)

    if porta2_fechada:
        porta2_b = porta2.get_rect(topleft=(4 * x / 9, 300))
        tela.blit(porta2, porta2_b)

    if porta3_fechada:
        porta3_b = porta3.get_rect(topleft=(6 * x / 9, 300))
        tela.blit(porta3, porta3_b)

    if sum(lista_fechadas) >= 2:
        inserir_texto("Tem certeza que vai escolher essa porta?", fonte2, branco, 365, 550)
        inserir_texto("Vou facilitar para você.", fonte2, branco, 485, 590)

        if cat not in ans["Porta1"] and portaescolhida != "Porta1":
            tela.blit(cats[list(cats)[0]], (2 * x / 9, 390))
            porta1_fechada = False
        elif cat not in ans["Porta2"] and portaescolhida != "Porta2":
            tela.blit(cats[list(cats)[0]], (4 * x / 9, 390))
            porta2_fechada = False
        elif cat not in ans["Porta3"] and portaescolhida != "Porta3":
            tela.blit(cats[list(cats)[0]], (6 * x / 9, 390))
            porta3_fechada = False

    else:
        cont = 0
        cont_gatos = 0
        porta1_fechada = False
        porta2_fechada = False
        porta3_fechada = False

        for i in (lista_portas):
            cont = cont+1
            if i:
                if ran == portaescolhida:
                    inserir_texto("PARABÉNS!", fonte2, branco, 555, 550)
                    inserir_texto("Você escolheu o gato certo.", fonte2, branco, 455, 590)

                else:
                    inserir_texto("Opa! Errou o gato", fonte2, branco, 505, 550)
                    inserir_texto("Agora seu gato vai viver uma vida nova sem você.", fonte2, branco, 295, 590)

                if ran == i:
                    tela.blit(chosen_cat, (2 * cont * x / 9, 390))
                else:
                    tela.blit(cats[list(cats)[cont_gatos]], (2 * cont * x / 9, 390))
                    cont_gatos = cont_gatos + 1

    current_time = pygame.time.get_ticks()
    print(start_time)
    if current_time - start_time >= popup_tempo:
        popup_on = True
    if popup_on:
        popup()
    #Tornando as portas restantes clicaveis

    for event in pygame.event.get():
        if event.type == QUIT:
            jogo_quit = True
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if porta1_fechada:
                if porta1_b.collidepoint(event.pos):
                    porta1_fechada = False
                    portaescolhida = "Porta1"
                    start_time = pygame.time.get_ticks()

            if porta2_fechada:
                if porta2_b.collidepoint(event.pos):
                    porta2_fechada = False
                    portaescolhida = "Porta2"
                    start_time = pygame.time.get_ticks()

            if porta3_fechada:
                if porta3_b.collidepoint(event.pos):
                    porta3_fechada = False
                    portaescolhida = "Porta3"
                    start_time = pygame.time.get_ticks()


    #porta = porta()
    pygame.display.update()
    clock.tick(60)

