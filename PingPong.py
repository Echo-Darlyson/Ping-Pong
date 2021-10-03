import pygame, random, os
from pygame.constants import K_UP

pygame.init()

# Cores
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

l1_start = 180 # Coord Y do início da linha 1
l1_end = 220 # Coord Y do final da linha 1

l2_start = 180 # Coord Y do início da linha 2
l2_end = 220 # Coord Y do final da linha 2

c_pos = [400, random.randint(90, 300)] # Coords da bola

vel_y = 1 # Velocidade Y das plataformas

vel_c = 0.3 # Velocidade da bola

screen = pygame.display.set_mode((800, 400)) # Tela
pygame.display.set_caption("Ping Pong") 

diretorio = os.path.dirname(__file__) # Diretório do script
file_path = os.path.join(diretorio, "./MKHm5N.jpg") # Junção do diretório do script com o script
back = pygame.image.load(file_path).convert() # Imagem de fundo

fonte = pygame.font.SysFont('Impact', 60) # Fonte dos textos

cont = True # Variável que controla o loop

maior_x = False # Maior que o eixo X
maior_y = False # Maior que o eixo Y

score_l1 = 0 # Ponto da linha 1
score_l2 = 0 # Ponto da linha 2

while cont:
    texto1 = fonte.render(f"{score_l1}", True, white) # Texto com o score da linha 1
    texto2 = fonte.render(f"{score_l2}", True, white) # Texto com o score da linha 2
    textorect1 = texto1.get_rect()
    textorect2 = texto2.get_rect()
    textorect1.center = (200, 40) # Coordenadas do texto1
    textorect2.center = (600, 40) # Coordenadas do texto2

    screen.blit(back, (0, 0)) # Desenha a imagem de fundo na janela
    screen.blit(texto1, textorect1) # Desenha o texto1 na janela
    screen.blit(texto2, textorect2) # Desenha o texto2 na janela

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            cont = False # Fecha a janela
        
    if pygame.key.get_pressed()[pygame.K_UP]: # l2 Tecla UP pressionada = Para Cima
        if l2_start > 0: # Apenas se o começo da linha 2 > 0
            l2_start -= vel_y
            l2_end -= vel_y

    elif pygame.key.get_pressed()[pygame.K_DOWN]: # l2 Tecla Down pressionada = Para Baixo
        if l2_end < 400: # Apenas se o final da linha 2 < 400
            l2_start += vel_y
            l2_end += vel_y
    
    elif pygame.key.get_pressed()[pygame.K_w]: # l1 Tecla W pressionada = Para Cima
        if l1_start > 0: # Apenas se o final da linha 1 > 0
            l1_start -= vel_y
            l1_end -= vel_y

    elif pygame.key.get_pressed()[pygame.K_s]: # l1 Tecla S pressionada = Para Baixo
        if l1_end < 400: # Apenas se o final da linha 1 < 400
            l1_start += vel_y
            l1_end += vel_y

    if c_pos[0] >= 800 or c_pos[0] <= 0: # Fecha a janela se a bola colidir com a lateral vertical
        vel_c = 0
        cont = False
    
    if c_pos[1] >= 400: # Verifica se a coord y colidiu com a lateral horizontal
        maior_y = True
    elif c_pos[1] <= 0:
        maior_y = False

    if maior_x == True: # Se colidiu com a plataforma direita subtrai a velocidade
        c_pos[0] -= vel_c
    else:               # Se colidiu com a platafroma esquerda soma a velocidade
        c_pos[0] += vel_c
    
    if maior_y == True: # Se colidiu com a de baixo subtrai a velocidade
        c_pos[1] -= vel_c
    else:               # Se colidiu com a de cima soma a velocidade
        c_pos[1] += vel_c

    if l1_start < c_pos[1] < l1_end - 20 and c_pos[0] <= 19: # (Parte de cima) Verifica se a bola colidiu com as plataforma esquerda
        maior_x = False
        maior_y = True
        vel_c += 0.1
        score_l1 += 1
    
    elif l1_start + 20 < c_pos[1] < l1_end and c_pos[0] <= 19: # (Parte de baixo) Verifica se a bola colidiu com as plataforma esquerda
        maior_x = False
        maior_y = False
        vel_c += 0.1
        score_l1 += 1
    
    if l2_start < c_pos[1] < l2_end - 20 and c_pos[0] >= 787 - 6: # (Parte de cima) Verifica se a bola colidiu com as plataforma direita
        maior_x = True
        maior_y = True
        vel_c += 0.1
        score_l2 += 1
    
    elif l2_start + 20 < c_pos[1] < l2_end and c_pos[0] >= 787 - 6: # (Parte de baixo) Verifica se a bola colidiu com as plataforma direita
        maior_x = True
        maior_y = False
        vel_c += 0.1
        score_l2 += 1
       
    pygame.draw.line(screen, white, (13, l1_start), (13, l1_end), width = 6) # linha 1
    pygame.draw.line(screen, white, (787, l2_start), (787, l2_end), width = 6) # linha 2
    pygame.draw.line(screen, white, (400, 0), (400, 400), width = 2)
    pygame.draw.circle(screen, blue, c_pos, 7, width = 0) # Bola
    pygame.display.flip() # Atualiza a tela

pygame.quit() # Fecha a janela