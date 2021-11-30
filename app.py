import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

NOME_JOGO = "Pega e Ganha"
LARGURA = 640
ALTURA = 480
TELA = (LARGURA, ALTURA)
COR_PRETA = (0, 0, 0)
COR_AZUL = (0, 0, 120)
COR_ROSA = (255, 0, 255)
COR_BRANCA = (255, 255, 255)
COR_VERMELHA = (255, 0, 0)
FPS = 30
JOGADOR_LARGURA = 40
JOGADOR_ALTURA = 50
MOVIMENTO = 20
OPACIDADE = 50

def qualquerLargura():
    return randint(0, LARGURA)

def qualquerAltura():
    return randint(0, ALTURA)

x_jogador = LARGURA/2
y_jogador = ALTURA/2
x_moeda = qualquerLargura()
y_moeda = qualquerAltura()
x_graniso = qualquerLargura()
y_graniso = 0
velocidade_graniso = 1
almenta_velocidade = False
pontos = 0
maior_pontuacao = 0

fonte = pygame.font.SysFont('arial', 30, True, True)

tela = pygame.display.set_mode(TELA)
pygame.display.set_caption(NOME_JOGO)

relogio = pygame.time.Clock()

while True:
    relogio.tick(FPS)
    tela.fill(COR_PRETA)

    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()

    teclapressionada = pygame.key.get_pressed()

    if teclapressionada[K_LEFT] and x_jogador > 0:
        x_jogador -= MOVIMENTO

    if teclapressionada[K_RIGHT] and x_jogador < LARGURA - JOGADOR_LARGURA:
        x_jogador += MOVIMENTO

    if teclapressionada[K_UP] and y_jogador > 0:
        y_jogador -= MOVIMENTO

    if teclapressionada[K_DOWN] and y_jogador < ALTURA - JOGADOR_ALTURA:
        y_jogador += MOVIMENTO

    jogador = pygame.draw.rect(tela, COR_AZUL, (x_jogador, y_jogador, JOGADOR_LARGURA, JOGADOR_ALTURA))
    graniso = pygame.draw.rect(tela, COR_VERMELHA, (x_graniso, y_graniso, JOGADOR_LARGURA/2, JOGADOR_ALTURA/2))
    moeda = pygame.draw.circle(tela, COR_ROSA, (x_moeda, y_moeda), 10)

    if jogador.colliderect(moeda):
        x_moeda = qualquerLargura()
        y_moeda = qualquerAltura()
        pontos += 1
        almenta_velocidade = True

        if pontos > maior_pontuacao:
            maior_pontuacao = pontos

    if jogador.colliderect(graniso):
        pontos -= 1
        y_graniso = 0
        x_graniso = qualquerLargura()

    if y_graniso >= ALTURA:
        y_graniso = 0
        x_graniso = qualquerLargura()

    if pontos % 5 == 0 and pontos > 0 and pontos >= maior_pontuacao - 1 and almenta_velocidade:
        velocidade_graniso += 1
        almenta_velocidade = False

    y_graniso += velocidade_graniso

    mensagem = f'Pontos: {pontos}, Maior Pontuação: {maior_pontuacao}'
    texto_formatado = fonte.render(mensagem, True, COR_BRANCA)
    texto_formatado.set_alpha(OPACIDADE)

    tela.blit(texto_formatado, (100, 40))

    mensagem = f'Velocidade: {velocidade_graniso}'
    texto_formatado = fonte.render(mensagem, True, COR_BRANCA)
    texto_formatado.set_alpha(OPACIDADE)

    tela.blit(texto_formatado, (100, 400))

    pygame.display.update()
