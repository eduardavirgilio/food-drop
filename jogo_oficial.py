import pygame
from personagens import Personagem

pygame.init()
#Construindo a tela
tela = pygame.display.set_mode((800, 500))
pygame.display.set_caption("food drop")
tela.fill((117, 75, 19))

# Carregando imagens
# Criando mais personagens
pou = Personagem("imagem/pou.png", 90, 80, 80, 10 )


