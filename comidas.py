import pygame
import random

class Comida:  
    def __init__(self, arquivo_imagem, largura_imagem, altura_imagem, y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.posiçãoX = random.randint(1,800)
        self.posiçãoY = y_inicial

        self.mascara = pygame.mask.from_surface(self.imagem)

        self.velocidade = random.randint(1,10)

    def movimenta(self):
        self.posiçãoY = self.posiçãoY + self.velocidade
        if self.posiçãoY < 0:
            self.posiçãoY = 850
            
         
    def desenhar(self, tela):
        tela.blit(self.imagem,(self.posiçãoX, self.posiçãoY))