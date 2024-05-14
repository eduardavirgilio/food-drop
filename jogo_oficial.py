import pygame
from personagens import Personagem
from comidas import Comida
import random

pygame.init() #iniciando os módulos básicos do pygame

tela = pygame.display.set_mode((800, 500)) #costruindo a tela
pygame.display.set_caption("★ food drop") #mudando o nome do jogo

clock = pygame.time.Clock() #relogio para controlar o FPS

FUNDO = pygame.image.load("imagens/fundo.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))



# Carregando imagens
# Criando mais personagens
pou = Personagem("imagens/pou.png", 130, 120, 340, 360 )

lista_comida = [Comida("imagens/aspargo.png", 60, 60, 120),
                Comida("imagens/batata.png", 60, 60, 120),]

rodando = True #se enquanto o jogo estiver rodando, ele vai ser verdsdeiro, para sair do while é so por ele = false
while rodando :
    #tudo que for feito fica guardado em uma lista de eventos
    #tratamento de eventos
    for evento in pygame.event.get(): #esse comando da a lista
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("vc clicou")
        if evento.type == pygame.QUIT: #VARIAVEL EM MAIUSCULO SÃO CONSTANTES, OU SEJA, NÃO MUDAM
            rodando = False #fechando o programa se clicar no X
    
    tela.blit(FUNDO,(0,0))

    pou.andar()
    pou.desenhar(tela)

    for comida in lista_comida:
        comida.movimenta()
        comida.desenhar(tela)

        if pou.mascara.overlap(comida.mascara,(comida.posiçãoX-pou.posiçãoX, comida.posiçãoY-pou.posiçãoY)):
            pass

#atualizando a tela
    pygame.display.update()

    clock.tick(80) #regulando o FPS

