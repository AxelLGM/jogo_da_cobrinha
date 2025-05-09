import pygame
import time
import random

pygame.init()

# Cores
branco = (255, 255, 255)
amarelo = (255, 255, 102)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Tamanho da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Relógio do jogo
clock = pygame.time.Clock()
tamanho_bloco = 20
velocidade = 15

# Fontes
fonte = pygame.font.SysFont("bahnschrift", 25)

def pontuacao(pontos):
    valor = fonte.render(f"Pontos: {pontos}", True, amarelo)
    tela.blit(valor, [0, 0])

def cobra(tamanho_bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_bloco, tamanho_bloco])

def mensagem(msg_linhas, cor):
    tela.fill(preto)
    fonte_menor = pygame.font.SysFont("bahnschrift", 20)
    for i, linha in enumerate(msg_linhas):
        texto = fonte_menor.render(linha, True, cor)
        rect = texto.get_rect(center=(largura // 2, altura // 2 + i * 30))
        tela.blit(texto, rect)

def jogo():
    fim = False
    sair = False

    x1 = largura // 2
    y1 = altura // 2

    x1_mudanca = 0
    y1_mudanca = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    while not sair:

        while fim:
            mensagem([
                "Game Over!",
                "Pressione Q para sair ou C para jogar novamente"
            ], vermelho)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        sair = True
                        fim = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            fim = True

        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(azul)
        pygame.draw.rect(tela, amarelo, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        lista_cabeca = [x1, y1]
        lista_cobra.append(lista_cabeca)

        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for segmento in lista_cobra[:-1]:
            if segmento == lista_cabeca:
                fim = True

        cobra(tamanho_bloco, lista_cobra)
        pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

jogo()
