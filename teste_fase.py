import pygame
import sys
import mixer


pygame.init()


preto=0,0,0
branco=255,255,255
vermelho=255,0,0
verde= 0,255,0
azul=0,0,255
roxo = 243,33, 33



largura = 1080
altura= 700
tamanho= (largura,altura)
tela=pygame.display.set_mode(tamanho)
pygame.display.set_caption("Atheris")
fonte = pygame.font.SysFont('Cambria',25)
keys = pygame.key.get_pressed()

def imprimir_texto(texto, linha, x, y, cor):
    for ch in texto:
        pygame.time.delay(30)
        linha+=ch
        texto= fonte.render(linha,True,cor)
        tela.blit(texto,[x, y])
        pygame.display.update()
def vitoria():
    global tela, branco
    bg0 = pygame.image.load("Imagens/vitoria.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    pygame.display.update()
    pygame.mixer.music.load('Audio/vitoria.mp3')
    pygame.mixer.music.play(1)
    pygame.time.wait(200000)
    sys.exit()


while True:
    bg= pygame.image.load("Imagens/title.jpg")
    bg = pygame.transform.scale(bg, (1080,700))
	
    tela.blit(bg,(0,0))
	

    # press= pygame.image.load("Game/Imagens/press.png")
    # press = pygame.transform.scale(press,(280,100))	  
    # tela.blit(press,(pygame.mouse.get_pos()))
    # print(pygame.mouse.get_pos())
	
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if keys[pygame.K_SPACE]:
            vitoria()
            break
        if keys[pygame.K_ESCAPE]:
            sys.exit()
	# if keys[pygame.K_F12]:
	# 	pygame.display.toggle_fullscreen()
	# 	pygame.display.toggle_fullscreen()
        pygame.display.update()

   