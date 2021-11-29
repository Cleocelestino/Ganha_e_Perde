import pygame
from pygame.locals import *
from sys import exit

pygame.init()

NOME_JOGO = "Caixas"
LARGURA = 640
ALTURA = 480
TELA = (LARGURA, ALTURA)
COR_PRETA = (0,0,0)
COR_AZUL = (0,0,120)
COR_ROSA = (255,0,255)

tela = pygame.display.set_mode(TELA)
pygame.display.set_caption(NOME_JOGO)

while True:
    tela.fill(COR_PRETA)

    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, COR_AZUL, (200,300,40,50))
    pygame.draw.circle(tela, COR_ROSA, (100, 130), 10)


    pygame.display.update()
      

    

