import pygame
import sys

pygame.init()

preto=0,0,0
branco=255,255,255
vermelho=255,0,0
verde= 0,255,0
azul=0,0,255

largura = 640
altura= 480
tamanho= (largura,altura)
tela=pygame.display.set_mode(tamanho)
pygame.display.set_caption("Random Game")

while True:
	bg= pygame.image.load("bg.jpg")
	bg = pygame.transform.scale(bg, (640,480))

	fonte = pygame.font.SysFont(None,55)

	tela.blit(bg,(0,0))
	texto = fonte.render('Start Game', True, preto)
	tela.blit(texto, [250,200])
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	if keys[pygame.K_TAB]:
		break
	if keys[pygame.K_ESCAPE]:
		sys.exit()
	if keys[pygame.K_F12]:
		pygame.display.toggle_fullscreen()
		pygame.display.toggle_fullscreen()
	pygame.display.update()


sys.exit()
