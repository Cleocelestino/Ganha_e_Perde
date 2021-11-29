import pygame
from pygame.locals import *
from sys import exit

pygame.init()

NOME_JOGO = "Caixas"
LARGURA = 640
ALTURA = 480
TELA = (LARGURA, ALTURA)
COR_PRETA = (0,0,0)

tela = pygame.display.set_mode(TELA)
pygame.display.set_caption(NOME_JOGO)

while True:
    tela.fill(COR_PRETA)

    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (255,0,255), (200,300,40,50))
            
    pygame.display.update()


      

    

