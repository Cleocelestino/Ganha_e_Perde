import pygame
from pygame.locals import *
from sys import exit

pygame.init()

LARGURA = 640
ALTURA = 480
COR_PRETA = (0,0,0)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Caixas")

while True:
    tela.fill(COR_PRETA)

    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()

            

    

