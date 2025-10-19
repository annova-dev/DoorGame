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
    pygame.draw.rect(tela, branco, popup_rect, 3)
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
                 return True

            if b2.collidepoint(event.pos):
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

# TELA DE ESCOLHA DO GATO - Primeira etapa

# cats - para escolha
bartolomiau = pygame.image.load("imagens/bartolomiau.png")
dottie = pygame.image.load("imagens/dottie.png")
sunny = pygame.image.load("imagens/sunny.png")
cats = {'bartolomiau':bart_door, 'dottie':dottie_door, 'sunny':sunny_door}

def escolha_gato():
    tela.fill(magenta_claro)

    inserir_texto("Escolha um gato para adotar!", fonte, branco, 225, 150)

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
            # Escolha dos gatos
            if bart_choice.collidepoint(event.pos):
                parte1 = True
                gato_escolhido = "bartolomiau"
                return parte1, gato_escolhido

            if sunny_choice.collidepoint(event.pos):
                parte1 = True
                gato_escolhido = 'sunny'
                return parte1, gato_escolhido

            if dottie_choice.collidepoint(event.pos):
                parte1 = True
                gato_escolhido = 'dottie'
                return parte1, gato_escolhido

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


#--------------- Menu ---------------
jogo_done = False
menu_on = True
cat_chosen = True
escolha = 0
next = 0
final = False
begin = 0
#--------------- Jogo ---------------
popup_tempo = 2000
popup_on = False
start_time = 999999999

# Variaveis do jogo - NENHUMA PORTA FOI ESCOLHIDA AINDA
porta1_fechada = True
porta2_fechada = True
porta3_fechada = True

while not jogo_done:
    if begin == 1:
        jogo_done = False
        menu_on = True
        cat_chosen = True
        escolha = 0
        next = 0
        final = False
        popup_tempo = 2000
        popup_on = False
        start_time = 999999999
        porta1_fechada = True
        porta2_fechada = True
        porta3_fechada = True
        cats = {'bartolomiau': bart_door, 'dottie': dottie_door, 'sunny': sunny_door}
        begin = 0

    if menu_on:
        tela.fill(magenta)
        tela.blit(titulo, (x / 3 - 5, 100))
        bb1 = pygame.Rect(b1)
        botao(preto, b1)
        bb2 = pygame.Rect(b2)
        botao(preto, b2)
        bb3 = pygame.Rect(b3)
        botao(preto, b3)
        press(bb1, b1)
        press(bb2, b2)
        press(bb3, b3)

        tela.blit(jogo, (3 * x / 7 + 62, 360))
        tela.blit(regras, (3 * x / 7 + 62, 450))
        tela.blit(sair, (3 * x / 7 + 65, 540))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bb1.collidepoint(event.pos):
                    cat_chosen = False
                    menu_on = False

                if bb2.collidepoint(event.pos):
                    Tk().wm_withdraw()
                    messagebox.showinfo('REGRAS',
                                        'Tente adivinhar a porta! Você terá que adivinhar a porta que seu gato está. Escolha entre 3 portas, depois da primeira escolha, uma das portas em que seu gato NÃO está será removida. Depois você terá que escolher, se troca a porta ou se a mantém. Boa sorte!')

                if bb3.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    # ETAPA DO JOGO - ESCOLHER O SEU GATO
    elif cat_chosen == False:
        resultado = escolha_gato()

        if resultado is not None:
            next, gato_escolhido = resultado
            # ALEATORIZAÇÃO DA PORTA DO GATO
            ordem_portas, porta_certa = porta(gato_escolhido)
            # print(ordem_portas, porta_certa)
            outros_gatos = cats.pop(str(gato_escolhido))
            # print(cats, outros_gatos)
            # Gato foi escolhido, ira para o proximo estagio
            cat_chosen = True
            escolha = 1

    # ETAPA DO JOGO - ESCOLHER E RE-ESCOLHER A PORTA
    elif next == 1:
        lista_fechadas = [porta1_fechada, porta2_fechada, porta3_fechada]

        # ------------- Jogo –-------------
        # ESCOLHER - Primeira escolha, entre as 3 portas

        if escolha == 1:
            tela.fill(amarelo_claro)
        else:
            tela.fill(magenta)
        mouse = pygame.mouse.get_pos()
    
        inserir_texto("Seu gato irá com você se adivinhar em que porta ele está!", fonte2, magenta, 225, 150)
    
        # Portas fechadas para escolha
        if porta1_fechada:
            porta1_b = porta1.get_rect(topleft=(2 * x / 9, 300))
            tela.blit(porta1, porta1_b)
            # pygame.draw.rect(tela, branco, porta1_b, 1)
    
        if porta2_fechada:
            porta2_b = porta2.get_rect(topleft=(4 * x / 9, 300))
            tela.blit(porta2, porta2_b)
            # pygame.draw.rect(tela, preto, porta2_b, 1)
    
        if porta3_fechada:
            porta3_b = porta3.get_rect(topleft=(6 * x / 9, 300))
            tela.blit(porta3, porta3_b)
            # pygame.draw.rect(tela, magenta, porta3_b, 1)

        if escolha == 2:
            inserir_texto("Tem certeza que vai escolher essa porta?", fonte2, branco, 365, 550)
            inserir_texto("Vou te dar uma dica.", fonte2, branco, 485, 590)

            if gato_escolhido not in ordem_portas["Porta1"] and portaescolhida != "Porta1":
                tela.blit(cats[list(cats)[0]], (2 * x / 9, 390))
                inserir_texto("Seu gato não está aqui...", fonte3, rosa_claro, 2 * x / 9, 390)
                porta1_fechada = False
            elif gato_escolhido not in ordem_portas["Porta2"] and portaescolhida != "Porta2":
                tela.blit(cats[list(cats)[0]], (4 * x / 9, 390))
                inserir_texto("Seu gato não está aqui...", fonte3, rosa_claro, 4 * x / 9, 390)
                porta2_fechada = False
            elif gato_escolhido not in ordem_portas["Porta3"] and portaescolhida != "Porta3":
                tela.blit(cats[list(cats)[0]], (6 * x / 9, 390))
                inserir_texto("Seu gato não está aqui...", fonte3, rosa_claro, 6 * x / 9, 390)
                porta3_fechada = False


        elif final:
            cont = 0
            cont_gatos = 0
            porta1_fechada = False
            porta2_fechada = False
            porta3_fechada = False

            for i in (lista_portas):
                cont = cont + 1
                if i:
                    if porta_certa == portaescolhida:
                        inserir_texto("PARABÉNS!", fonte2, branco, 555, 550)
                        inserir_texto("Você escolheu o gato certo.", fonte2, branco, 455, 590)
                        acertou = 1

                    else:
                        inserir_texto("Opa! Errou o gato", fonte2, branco, 505, 550)
                        inserir_texto("Agora seu gato vai viver uma vida nova sem você.", fonte2, branco, 295, 590)
                        acertou = 0

                    if porta_certa == i:
                        tela.blit(outros_gatos, (2 * cont * x / 9, 390))

                        if acertou == 1:
                            inserir_texto("<<33", fonte2, branco, 2 * cont * x / 9, 390)
                        else:
                            inserir_texto("UAAAAA", fonte2, branco, 2 * cont * x / 9, 390)
                    else:
                        tela.blit(cats[list(cats)[cont_gatos]], (2 * cont * x / 9, 390))
                        cont_gatos = cont_gatos + 1

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= popup_tempo:
            popup_on = True

        if popup_on:
            menu_on = popup()
            if menu_on:
                begin = 1
                next = 0
    
        #Tornando as portas clicaveis e passando a porta escolhida
        for event in pygame.event.get():
            if event.type == QUIT:
                jogo_done = True
                pygame.quit()
                sys.exit()
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if porta1_fechada:
                    if porta1_b.collidepoint(event.pos):
                        if escolha == 1:
                            portaescolhida = "Porta1"
                            escolha = 2
                        elif escolha == 2:
                            porta1_fechada = False
                            portaescolhida = "Porta1"
                            escolha = 0
                            final = True
                            start_time = pygame.time.get_ticks()
        
                if porta2_fechada:
                    if porta2_b.collidepoint(event.pos):
                        if escolha == 1:
                            portaescolhida = "Porta2"
                            escolha = 2
                        
                        elif escolha == 2:
                            porta2_fechada = False
                            portaescolhida = "Porta2"
                            escolha = 0
                            final = True
                            start_time = pygame.time.get_ticks()

                if porta3_fechada:
                    if porta3_b.collidepoint(event.pos):
                        if escolha == 1:
                            portaescolhida = "Porta3"
                            escolha = 2

                        elif escolha == 2:
                            porta3_fechada = False
                            portaescolhida = "Porta3"
                            escolha = 0
                            final = True
                            start_time = pygame.time.get_ticks()
    
        #porta = porta()
    pygame.display.update()
    clock.tick(60)

