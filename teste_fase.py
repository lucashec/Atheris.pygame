import pygame
import sys
import mixer
import time

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
proximafase = 0

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
    time.sleep(20)
    sys.exit()
def morte():
    global tela, branco
    bg0 = pygame.image.load("Imagens/morte.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    pygame.display.update()
    pygame.mixer.music.load('Audio/morte.mp3')
    pygame.mixer.music.play(1)
    time.sleep(5)
def fase21():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg10.png") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Vocês descem dos cavalos e reparam que ele faz parte da guarda real.'
    linha1v = ''
    linha2 = 'Negreitos:'
    linha3 = '- Que os deuses o abençoem, viajante. O que um oficial da guarda real faz por aqui tão'
    linha4 = 'distante do palácio?'
    linha5 = 'Cavaleiro:'
    linha6 = '- Salve, sacerdote. Estou a procura de um famigerado ladrão que invadiu a biblioteca'
    linha7 = 'central e roubou um tomo muito importante para o reino. Alguns o chamam de "o Aranha"'
    linha8 = '.Temos algumas poucas descrições dele, mas nenhuma com muitos detalhes.'
    linha9 = 'Enquanto conversam, Negreitos consegue roubar o saco de moedas dele e você vê '
    linha10 = 'em sua cintura o que parece ser uma bela adaga com várias pedras e gemas valiosas. '
    linha11 = 'Parecem ser mágicas!'
    linha12 = 'Se quiser roubar a adaga, aperte 1.'#cena17
    linha13 = 'Se está satisfeito com o saco de moedas, aperte 2.'#cena18
    
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,vermelho)
    imprimir_texto(linha3,linha1v, 20, 70,vermelho)
    imprimir_texto(linha4,linha1v, 20, 95,vermelho)
    imprimir_texto(linha5,linha1v,20, 120,vermelho)
    imprimir_texto(linha6,linha1v,20,145,vermelho)
    imprimir_texto(linha7,linha1v,20,170,vermelho)
    imprimir_texto(linha8,linha1v,20,195,vermelho)
    imprimir_texto(linha9,linha1v,20,220,branco)
    imprimir_texto(linha10,linha1v,20,245,branco)
    imprimir_texto(linha11, linha1v, 20, 270,branco)
    imprimir_texto(linha12, linha1v, 250, 310,branco)
    imprimir_texto(linha13,linha1v, 250, 355,branco)

    time.sleep(15)
def fase24():
    global tela, branco, proximafase
    bg0 = pygame.image.load("Imagens/bg24.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Você dirige-se até o templo escondido de Negreitos onde ele convida os seguidores a '
    linha1v = ''
    linha2 = 'doarem os seus bens para a seita. Ao chegar lá, não encontra ninguém. E ao sair da '
    linha3 = 'sala você escuta uma voz baixa.'
    linha4 = 'Negreitos:'
    linha5 = '- Procurando por alguém, Atheris?'
    linha6 = 'Você se assusta e procura ao redor quem poderia ter dito aquilo. Não vê ninguém,'
    linha7 = 'volta seu olhar para o mico e vê um pequeno sorriso naquele rosto peludo.'
    linha8 = 'Atheris:'
    linha9 = '- Negreitos, é você?!'
    linha10 = 'Você grita e o mico pula do seu ombro. Como num passe de mágica, aquele corpo pequeno'
    linha11 = 'e peludo ganha feições conhecidas. Nesse mesmo instante, você lembra que os clérigos'
    linha12 = 'do Deus dos ladrões tinham esse poder e vê Negreitos em roupa de sacerdote dos deuses.'
    linha13 = 'Depois de passado o susto, você explica seu plano e ele parece concordar.'
    linha14 = 'Negreitos:'
    linha15 = '- Não se preocupe, com certeza os deuses vão abençoar nossa jornada. Mas ela seria'
    linha16 = 'ainda mais abençoada se um líder de Guilda fizesse oferendas ao Deus da trapaça!'
    linha17 = 'Entendendo bem a mensagem, você presume que se o ajudar, o Deus da trapaça terá várias'
    linha18 = 'oferendas quando você for o novo líder. Você se pergunta o que terá acontecido com o'
    linha19 = 'outro mico e se Negreitos esteve em seu ombro esse tempo todo. Então, chega a conclu-'
    linha20 = 'são que é melhor nem o questioná-lo.'
    linha21 = 'Aperte espaço para continuar.'

    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,vermelho)
    imprimir_texto(linha5,linha1v,20, 120,vermelho)
    imprimir_texto(linha6,linha1v,20,145,branco)
    imprimir_texto(linha7,linha1v,20,170,branco)
    imprimir_texto(linha8,linha1v,20,195,vermelho)
    imprimir_texto(linha9,linha1v,20,220,vermelho)
    imprimir_texto(linha10,linha1v,20,245,branco)
    imprimir_texto(linha11, linha1v, 20, 270,branco)
    imprimir_texto(linha12, linha1v, 20, 295,branco)
    imprimir_texto(linha13,linha1v, 20, 320,branco)
    imprimir_texto(linha14,linha1v, 20, 345,branco)
    imprimir_texto(linha15,linha1v,20, 370,vermelho)
    imprimir_texto(linha16,linha1v,20,395,vermelho)
    imprimir_texto(linha17,linha1v,20,420,branco)
    imprimir_texto(linha18,linha1v,20,445,branco)
    imprimir_texto(linha19, linha1v, 20, 470,branco)
    imprimir_texto(linha20,linha1v,20,495,branco)
    imprimir_texto(linha21, linha1v, 20, 545,branco)

    
def prologo():
    global tela, branco, keys, proximafase
    bg0 = pygame.image.load("Imagens/ladino.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))

    pygame.display.update()
    linha1 = 'Seu nome é Atheris, um renomado ladrão profissional. Depois de uma vida de roubos você '
    linha1v = ''
    linha2 = 'decidiu se estabelecer em uma metrópole calma para descansar, acabando por associar-se a'
    linha3 = 'Guilda de Ladrões local, uma espécie de sindicato do crime que detém o monopólio das '
    linha4 = 'atividades criminosas  na cidade. Depois de algum tempo, você decide que está na hora de'
    linha5 = 'de virar líder da guilda. E a melhor forma de conseguir isso seria coletando itens mági-'
    linha6 = 'cos poderosos. Lhe vem a cabeça que a alguns anos atrás você costumava andar com um gru-'
    linha7 = 'po de aventureiros, e que eles invadiram a fortaleza de uma feiticeira muito poderosa.'
    linha8 = 'Conhecida como Sarah de Saalem. foi lá onde conseguiu o manto que o nomeou como '
    linha9 = 'Atheris, "o Aranha". E é lá onde você conseguirá itens para se tornar o novo líder da Guilda.'
    linha10 = 'Aperte espaço'
    
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,branco)
    imprimir_texto(linha7,linha1v,20,170,branco)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,220,branco)
    imprimir_texto(linha10,linha1v,650,450,branco)
    
    a = False
    while a == False :
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    a = True
    proximafase = 24   

def fase29():
    global tela, branco
    bg0 = pygame.image.load("Imagens/bg20.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Você examina a fechadura e começa a cutucá-la com seu estojo de ferramentas. Ao seu lado,'
    linha1v = ' '
    linha2 = 'Negreitos retorna a forma humana com um desabafo.'
    linha3 = 'Negreitos:'
    linha4 = '- Não acredito em meus olhos! Por onde anda sua antiga astúcia, amigo Atheris? Por que está'
    linha5 = 'procurando armadilhas no lado de dentro de uma porta? Francamente...'
    linha6 = 'Irritado com sua momentânea incompetência para o ramo, Negreitos avança e mete o pé na'
    linha7 = 'porta, escancarando-a, sem se preocupar com o que há no outro lado e logo se arrepende.'
    linha8 = 'A porta leva para um corredor, que a princípio parece vazio. Apenas parece, porque da'
    linha9 = 'escuridão surge um cão enorme. Um mastim realmente assustador com presas demoníacas'
    linha10 = 'curvando-se para fora da boca. Um cão estranhamente silencioso.'
    linha11 = 'Você saca o punhal e prepara-se para a luta, mas... seria só sua imaginação?! Infelizmente,'
    linha12 = 'não era imaginação. Aquilo não era um cão de guarda comum, mas sim um cadáver animado.'
    linha13 = 'Certamente invocado por Sarah para proteger seu castelo nesta noite tão suspeita. Despre-'
    linha14 = 'parados para uma batalha contra um morto-vivo, você e Negreitos não conseguem sobrevi-'
    linha15 = 'ver ao toque pestilento das garras da fera...' #morte
    
     
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,vermelho)
    imprimir_texto(linha4,linha1v, 20, 95,vermelho)
    imprimir_texto(linha5,linha1v,20, 120,vermelho)
    imprimir_texto(linha6,linha1v,20,145,branco)
    imprimir_texto(linha7,linha1v,20,170,branco)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,220,branco)
    imprimir_texto(linha10,linha1v,20,245,branco)
    imprimir_texto(linha11, linha1v, 20, 270,branco)
    imprimir_texto(linha12, linha1v, 20, 295,branco)
    imprimir_texto(linha13,linha1v, 20, 320,branco)
    imprimir_texto(linha14,linha1v, 20, 345,branco)
    imprimir_texto(linha15,linha1v,20, 370,branco)
    time.sleep(10)
    morte()
    vitoria()
pygame.mixer.music.load('Audio/title.mp3')
pygame.mixer.music.play(-1)
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
            prologo()
            fase21()
            fase29()
            break
        if keys[pygame.K_ESCAPE]:
            sys.exit()
	# if keys[pygame.K_F12]:
	# 	pygame.display.toggle_fullscreen()
	# 	pygame.display.toggle_fullscreen()
        pygame.display.update()

   