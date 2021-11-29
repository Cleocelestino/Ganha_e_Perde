import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

NOME_JOGO = "Caixas"
LARGURA = 640
ALTURA = 480
TELA = (LARGURA, ALTURA)
COR_PRETA = (0, 0, 0)
COR_AZUL = (0, 0, 120)
COR_ROSA = (255, 0, 255)
COR_VERMELHA = (255, 0, 0)

x = LARGURA/2
y = ALTURA/2
x_moeda = randint(0, LARGURA)
y_moeda = randint(0, ALTURA)
y_graniso = 0

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)



tela = pygame.display.set_mode(TELA)
pygame.display.set_caption(NOME_JOGO)
relogio = pygame.time.Clock()



while True:
    relogio.tick(30)
    tela.fill(COR_PRETA)
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()

    teclapressionada = pygame.key.get_pressed()

    if teclapressionada[K_LEFT]:
        x = x - 20

    if teclapressionada[K_RIGHT]:
        x = x + 20

    if teclapressionada[K_UP]:
        y = y - 20

    if teclapressionada[K_DOWN]:
        y = y + 20

    jogador = pygame.draw.rect(tela, COR_AZUL, (x, y, 40, 50))
    graniso = pygame.draw.rect(tela, COR_VERMELHA, (0, y_graniso, 10, 10))
    moeda = pygame.draw.circle(tela, COR_ROSA, (x_moeda, y_moeda), 10)

    if jogador.colliderect(moeda):
        x_moeda = randint(0, LARGURA)
        y_moeda = randint(0, ALTURA)
        pontos = pontos + 1

    if y_graniso >= ALTURA:
        y_graniso = 0
        
    y_graniso = y_graniso + 1

    tela.blit(texto_formatado, (450, 40))

    pygame.display.update()
