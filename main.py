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
azulesc = 0, 34, 255
roxo = 243,33, 33
lar = 255, 128,0 

largura = 1080
altura= 700
tamanho= (largura,altura)
tela=pygame.display.set_mode(tamanho)
pygame.display.set_caption("Atheris")
fonte = pygame.font.SysFont('Cambria',25)
proximafase = 0


def imprimir_texto(texto, linha, x, y,cor):
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
def fase42():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg7.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1='Negreitos:'
    linha1v =''
    linha2 = '- Não fiz nada, amigo. Foram os deuses que, a meu pedido, envelheceram as grades mil anos.'
    linha3 = 'Você fica alegre por ter aquele clérigo a seu lado, você entra no aposento. Tira uma pedra'
    linha4 = 'mágica da mochila, balança, e ela começa a brilhar, iluminando o lugar. Olhando bem'
    linha5='parece que parte dos equipamentos mágicos estão aqui. As paredes têm lanças, alabardas,'
    linha6='tridentes e outras armas de grande porte. Devem ser poderosas nas mãos de guerreiros,'
    linha7='mas não interessam a vocês.'
    linha8='Procurando por algo que valha a pena, você nota 2 objetos que chamam sua atenção.'
    linha9='Um cetro, suspenso na parede, tendo em sua ponta um cristal transparente e uma estátua'#cena 3
    linha10='metálica sobre uma mesinha, no canto do quarto.' #Cena 8
    linha11='Se quiser pegar o cetro, aperte 1.'
    linha12='Se quiser pegar a estáuta, aperte 2.'
    linha13='Se prefere deixar tudo onde está, aperte 3.'#20

    imprimir_texto(linha1, linha1v, 20, 20,vermelho)
    imprimir_texto(linha2, linha1v, 20, 45,vermelho)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,branco)
    imprimir_texto(linha7,linha1v,20,170,branco)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,220,branco)
    imprimir_texto(linha10,linha1v,20,245,branco)
    imprimir_texto(linha11, linha1v, 20, 290,branco)
    imprimir_texto(linha12, linha1v, 20, 335,branco)
    imprimir_texto(linha13,linha1v,20,380,branco)

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_1:
    				a = True
    				proximafase= 3
    			if event.key == pygame.K_2:
    				a = True
    				proximafase = 8
    			if event.key == pygame.K_3:
    				a = True
    				proximafase = 20
def fase40():
	global tela, branco, proximafase
	bg0 = pygame.image.load("Imagens/bg40.jpg")
	bg0 = pygame.transform.scale(bg0,(1080,700))
	tela.blit(bg0,(0,0))
	linha1='Dias depois, os grandes chefes da quadrilha de Kristophania foram convocados para'
	linha1v=''
	linha2='uma reunião extraordinária pelo chefão da Guilda. Na cabeceira da mesa, tendo seus'
	linha3='guardas assassinos a seu lado, ele tem um anúncio surpreendente a fazer.'
	linha4='chefão da Guilda:'
	linha5='- Estou cansado da diretoria. Convoquei esta reunião para declarar quem será o novo' 
	linha6='chefe geral da Guilda de Kristophania. Atheris, o Aranha, será o novo diretor.'
	linha7='E a reunião termina com a saída furiosa dos chefes. Você dispensa os guardas, satisfeito'
	linha8='em ver que em ver que eles cumprem suas ordens. Estão sozinhos agora você e o ex-chfe. Ou'
	linha9='não?'
	linha10='Negreitos:'
	linha11='- Muito bom esse chapéu de disfarce, suas ilusões poderiam enganar a qualquer um.'
	linha12='Atheris:'
	linha13='- Não precisam enganar mais ninguém, se o corpo do chefe for encontrado não fará mais dife-'
	linha14='rença. agora "ele" já passou o cargo para mim, certo?'
	linha15='Sim, foi um bom plano: matar o chefe, e usar o chapéu mágico de Sarah para criar a ilusão'
	linha16='de que Negreitos era ele. Parabéns, você conseguiu. É o novo chefão da Guilda de Ladrôes.'
	linha17='Pelo menos até que alguém apareça com um plano mais astucioso do que o seu!'
	
	imprimir_texto(linha1, linha1v, 20, 20,branco)
	imprimir_texto(linha2, linha1v, 20, 45,branco)
	imprimir_texto(linha3,linha1v, 20, 70,branco)
	imprimir_texto(linha4,linha1v, 20, 95,vermelho)
	imprimir_texto(linha5,linha1v,20, 120,vermelho)
	imprimir_texto(linha6,linha1v,20,145,branco)
	imprimir_texto(linha7,linha1v,20,170,branco)
	imprimir_texto(linha8,linha1v,20,195,branco)
	imprimir_texto(linha9,linha1v,20,220,branco)
	imprimir_texto(linha10,linha1v,20,245,vermelho)
	imprimir_texto(linha11, linha1v, 20, 270,vermelho)
	imprimir_texto(linha12, linha1v, 20, 295,vermelho)
	imprimir_texto(linha13,linha1v, 20, 320,vermelho)
	imprimir_texto(linha14,linha1v, 20, 345,vermelho)
	imprimir_texto(linha15,linha1v,20, 370,branco)
	imprimir_texto(linha16,linha1v,20,395,branco)
	imprimir_texto(linha17,linha1v,20,420,branco)
	time.sleep(5)
	vitoria()

def fase35():
	global tela, branco, proximafase
	bg0 = pygame.image.load("Imagens/bg35.jpg")
	bg0 = pygame.transform.scale(bg0,(1080,700))
	tela.blit(bg0,(0,0))
	linha1='Tendo vencido Sarah. você pode examinar sua coleção com mais calma. Dentre uma infini-'
	linha1v=''
	linha2='dade de itens, você encontra o que parece ser um chapéu vulgar, mas é exatamente o que'
	linha3='procurava.' #fase40
	linha4='Aperte espaço para continuar'
	
	imprimir_texto(linha1, linha1v, 20, 20,branco)
	imprimir_texto(linha2, linha1v, 20, 45,branco)
	imprimir_texto(linha3,linha1v, 20, 70,branco)
	imprimir_texto(linha4,linha1v, 20, 120,branco)

	a = False
	while a == False:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					a = True
					proximafase= 40
def fase33():
	global tela, branco, proximafase
	bg0 = pygame.image.load("Imagens/33bg.jpg")
	bg0 = pygame.transform.scale(bg0,(1080,700))
	tela.blit(bg0,(0,0))
	linha1='Você agarra o colar de contas, reconhecendo-o como sendo parecido com aquele usado'
	linha1v=''
	linha2='por um guerreiro amigo seu. As contas do colar são explosivas. Você arranca a maior e'
	linha3='e arremessa contra Sarah, cobrindo os olhos para proteger-se da explosão. Quando olha'
	linha4='novamente descobre que ela ainda de pé.'
	linha5='Sarah:'
	linha6='Pobre tolo! É preciso muito mais do que isso para acabar comigo.' 
	linha7='Atheris: '
	linha8='Será mesmo?!'
	linha9='Você toma outra conta do coalr e arremessa... mas não contra Sarah. Desta vez você mira '
	linha10='no chão, entre seus pés. Como você planejou, o chão não resiste e desaba levando Sarah'
	linha11='consigo.'
	linha12='Negreitos:'
	linha13='Muito engenhoso, amigo Atheris, isso provavelmente não vai matar ela, mas irá detê-la até'
	linha14='que estajamos longe.'
	linha15='Aperte espaço para continuar.'#fase35
	
	imprimir_texto(linha1, linha1v, 20, 20,branco)
	imprimir_texto(linha2, linha1v, 20, 45,branco)
	imprimir_texto(linha3,linha1v, 20, 70,branco)
	imprimir_texto(linha4,linha1v, 20, 95,branco)
	imprimir_texto(linha5,linha1v,20, 120,vermelho)
	imprimir_texto(linha6,linha1v,20,145,vermelho)
	imprimir_texto(linha7,linha1v,20,170,vermelho)
	imprimir_texto(linha8,linha1v,20,195,vermelho)
	imprimir_texto(linha9,linha1v,20,220,branco)
	imprimir_texto(linha10,linha1v,20,245,branco)
	imprimir_texto(linha11, linha1v, 20, 270,branco)
	imprimir_texto(linha12, linha1v, 20, 295,vermelho)
	imprimir_texto(linha13,linha1v, 20, 320,vermelho)
	imprimir_texto(linha14,linha1v, 20, 345,vermelho)
	imprimir_texto(linha15,linha1v,20, 390,branco)

	a = False
	while a == False:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					a = True
					proximafase= 35

def fase19():
	global tela, branco
	bg0 = pygame.image.load("Imagens/bg33.jpg")
	bg0 = pygame.transform.scale(bg0,(1080,700))
	tela.blit(bg0,(0,0))
	linha1='A lança, infelizmente, não foi uma escolha sábia: é uma arma mágica especialmente'
	linha1v=''
	linha2='criada para matar dragões, e mostra-se desajeitada contra Sarah. Ela vence a luta e'
	linha3='esmaga vocês com seu martelo...'

	imprimir_texto(linha1, linha1v, 20, 20,branco)
	imprimir_texto(linha2, linha1v, 20, 45,branco)
	imprimir_texto(linha3,linha1v, 20, 70,branco)
	time.sleep(15)
	morte()
		
def fase13():
    global tela, branco, proximafase
    bg0 = pygame.image.load("Imagens/34bg.jpg")
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1='Você segue num corredor iluminado por tochas e depois de alguns minutos, chega ao fim da'
    linha1v=''
    linha2='linha, uma extensa parede no final do corredor. Você suspeita que possa ter algo após a pare'
    linha3='de, e pela sua intuição e experiência, resolve puxar uma tocha que está isolada a sua esquer-'
    linha4='da. A parede se movimenta e revela um porão da torre. Vocês sobem as escadas, chegam ao'
    linha5='saguão e logo alcançam a sala principal da coleção de Sarah. Desta vez tomam cuidado para'
    linha6='evitar o tapete traiçoeiro. Examinando a coleção, encontram o cajado e a capa de Negreitos.' 
    linha7='De repente, após uma explosão como a de um trovão, surge Sarah, -desta vez armada com '
    linha8='seu martelo de guerra.'
    linha9='Sarah:'
    linha10='- Malditos ladrões! Vocês querem minhas armas! Mas não vou permitir que roubem, eu terei'
    linha11='todas as armas mágicas do mundo.'
    linha12='Ela avança disposta a esmagar vocês dois, e a espada que você tem em mão não será sufici-'
    linha13='ente para detê-la. Você olha à volta, deseperado para encontrar algo que possa ser usado'
    linha14='contra ela. Dois objetos estão ao seu alcance:'
    linha15='Uma lança prateada com dragões esculpidos e um colar de contas vermelhas.'
    linha16='Para pegar a lança, aperte 1.'#fase19 
    linha17='Para pegar o colar, aperte 2'#fase33
    
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,branco)
    imprimir_texto(linha7,linha1v,20,170,branco)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,220,vermelho)
    imprimir_texto(linha10,linha1v,20,245,vermelho)
    imprimir_texto(linha11, linha1v, 20, 270,vermelho)
    imprimir_texto(linha12, linha1v, 20, 295,branco)
    imprimir_texto(linha13,linha1v, 20, 320,branco)
    imprimir_texto(linha14,linha1v, 20, 345,branco)
    imprimir_texto(linha15,linha1v,20, 370,branco)
    imprimir_texto(linha16,linha1v,20,420,branco)
    imprimir_texto(linha17,linha1v,20,460,branco)
    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_1:
    				a = True
    				proximafase= 19
    				if event.key == pygame.K_2:
    					a = True
    				proximafase = 33

def fase34():
    global tela, branco
    bg0 = pygame.image.load("Imagens/34bg.jpg")
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1='O caminho da esquerda conduz vocês a uma sala vazia. Convecido de que não há ninguém'
    linha1v=''
    linha2='no aposento, Negreitos comenta com desdém sobre a lenda dos almas dos prisioneiros mor-'
    linha3='tos no castelo que supostamente se transformariam em zumbi. Que azar! sua intuição erra'
    linha4='e a sala não estava vazia como imaginava. Um zumbi desencarndo surge sob as ordens de seu'
    linha5='mestre. O silêncio dos mortos-vivos o enganou. Vocês comprovam da pior forma que a lenda'
    linha6='é verdadeira. As garras dos monstros enterram-se em sua gargante antes que Negreitos con-'
    linha7='siga esconjurá-lo.'#morte
    
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,branco)
    imprimir_texto(linha7,linha1v,20,170,branco)
    time.sleep(15)
    morte()
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
    time.sleep(15)
    morte()
def fase39():
    global tela, branco, proximafase
    bg0 = pygame.image.load("Imagens/bg20.jpg")
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1='Com o máximo de cuidado para não fazer ruído, você mexe nas tochas. E então percebe que'
    linha1v=''
    linha2='que há um mecanismo de alavanca em umas das tochas. Ao puxar a tocha para baixo, a porta'
    linha3='se abre e um círculo mágico se apaga no centro da sala. A porta leva ao aposento onde Sarah'
    linha4='guarda as peças principais de sua coleção. As parades são adornadas com espadas e armadu-'
    linha5='ras reluzentes. Vocês notam um corpo enorme de um cachorro morto no canto da sala.'
    linha6='Negreitos averigua o corpa do animal e faz sinal de que ele relamente está morto.'
    linha7='Vocês voltam a atenção para um grande tapete. Seria este um dos tais tapetes mágicos?!' 
    linha8='Você e Negreitos se aproximam para sentar no tapete... e caem. Você acorda numa cela no'
    linha9='calabouço da torre de Sarah. A porta da cela se abre, e por ela entram dois guardas com'
    linha10='armaduras, se tratam de duas armaduras mágicas. Elas se posicionam no lado porta e abrem'
    linha11='passagem para... Sarah. Usando suas peças favoritas a Espada Infernal, o Manto das Som-'
    linha12='bras, cajado e capa de Negreitos.'
    linha13='Sarah:'
    linha14='- Supreendem-me com sua audácia, seus ratos ladrões.'
    linha15='Ela agita a capa e o cajado diante de vocês. Sarah usa objetos mágicos para ampliar sua'
    linha16='força e mesmo sem armas poderia matá-los sem esforço.'
    linha17='Sarah:'
    linha18='- A recompensa por sua tolice será a morte, mas não agora. Vocês interromperam meu sono.'
    linha19='Desejo estar descansada para sobrar seu sofrimento. Aproveitem sua última noite.'
    linha20='Você saca seu estojo de ferramentas que, felizmente, escapou da revista de Sarah e decide'
    linha21='tentar abrir a fechadura da cela. Ela abre facilmente e Negreitos, de posse de seu símbolo'
    linha22='sagrado, esconjura as armaduras mágicas fazendo-as em pedaços. Vocês seguem por um '
    linha23='corredor e se deparam com uma bifurcação.'
    linha24='Se quiser pegar o caminho da direita, aperte 1.' #fase13
    linha25='Se quiser pegar o caminho da esquerda, aperte 2.' #fase34

    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,branco)
    imprimir_texto(linha7,linha1v,20,170,branco)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,220,branco)
    imprimir_texto(linha10,linha1v,20,245,branco)
    imprimir_texto(linha11,linha1v,20,270,branco)
    imprimir_texto(linha12,linha1v,20,295,branco)
    imprimir_texto(linha13, linha1v, 20, 320,vermelho)
    imprimir_texto(linha14, linha1v, 20, 345,vermelho)
    imprimir_texto(linha15,linha1v, 20, 370,branco)
    imprimir_texto(linha16,linha1v, 20, 395,branco)
    imprimir_texto(linha17,linha1v,20, 420,vermelho)
    imprimir_texto(linha18,linha1v,20,445,vermelho)
    imprimir_texto(linha19,linha1v,20,470,vermelho)
    imprimir_texto(linha20,linha1v,20,495,branco)
    imprimir_texto(linha21, linha1v, 20, 520,branco)
    imprimir_texto(linha22,linha1v,20,545,branco)
    imprimir_texto(linha23, linha1v, 20, 570,branco)
    imprimir_texto(linha24, linha1v, 20, 595,branco)
    imprimir_texto(linha25,linha1v,20,620,branco)
    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_1:
    				a = True
    				proximafase= 13
    			if event.key == pygame.K_2:
    				a = True
    				proximafase = 34
def fase20():
    global tela, branco, proximafase
    bg0 = pygame.image.load("Imagens/bg20.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Você volta sua atenção para a única porta do aposento, que fica após 2 tochas,'
    linha1v = ' '
    linha2 = 'uma de cada lado da porta, e pergunta-se o que haverá depois da porta.'
    linha3 = 'Se você quiser verificar as tochas, aperte 1' #cena 39
    linha4 = 'Se você acha que pode haver uma armadilha na porta, aperte 2.' #Cena 29

    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 90,branco)
    imprimir_texto(linha4,linha1v, 20, 135,branco)

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_1:
    				a = True
    				proximafase= 39
    			if event.key == pygame.K_2:
    				a = True
    				proximafase = 29

def fase11():
    global tela, branco
    bg0 = pygame.image.load("Imagens/bg7.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Uma arma capaz de disparar relâmpagos... com ela você poderia fulminar a diretoria da'
    linha1v = ' '
    linha2 = 'Guilda e facilmente assumir seu lugar. É exatamente o que procurava. Sua mão aproxima-se'
    linha3 = 'do cetro, vacila um pouco e fecha-se em volta dele.'
    linha4 = 'Seus dedos parecem dormentes, mas pode ser apenas o nervosismo. Abrindo os olhos, para'
    linha5 = 'seu horror, você vê faíscas azuis crepitando sobre seu pulso. Elas ficam maiores e maiores,'
    linha6 = 'queimando os pelos de seu braço, deixando manchas negras na pele, calcinando sua carne...'
    linha7 = 'e matando você.'
    linha8 = 'Diante do punhado de carvão que havia se chamando Atheris, o Aranha, Negreitos mexe a'
    linha9 = 'cabeça lamentando.'
    linha10 = 'Negreitos:'
    linha11 = 'sinto muito, amigo Atheris. O Deus da trapaça não estava com você. Uma pena.'
    linha12 = 'E o macaquinho foge pela janela, de volta à cidade.' #morte

    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,branco)
    imprimir_texto(linha7,linha1v,20,170,branco)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,220,branco)
    imprimir_texto(linha10,linha1v,20,245,branco)
    imprimir_texto(linha11, linha1v, 20, 270,branco)
    imprimir_texto(linha12, linha1v, 20, 295,branco)
    time.sleep(15)
    morte()

def fase8():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg7.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'O cetro está na parede, suspenso na horizontal por dois suportes, como as demais armas. '
    linha1v = ' '
    linha2 = 'Olhando mais de perto, você percebe que o cristal está preso por uma peça metálica em '
    linha3 = 'forma de mão.'
    linha4 = 'Negreitos:'
    linha5 = '- É uma arma mágica.'
    linha6 = 'Ainda na forma de mico.'
    linha7 = 'Negreitos:'
    linha8 = '- Já vi magos utilizando cajados assim para lançar relâmpagos. Mas tome cuidado antes '
    linha9 = 'de tocá-la, amigo Atheris. O cajado pode ser uma arma formidável nas mãos da pessoa certa,'
    linha10 = 'mas pode matar a pessoa errada.'
    linha11 = 'Atheris:'
    linha12 = '- Como assim?'
    linha13 = 'Negreitos:'
    linha14 = '- É como um cão, influenciado pela personalidade do dono. Se o construtor desta arma era,'
    linha15 = 'maligno uma pessoa bondosa não poderá tocá-la sem sofrer dano. se era bom, queimará as'
    linha16 = 'mãos de uma pessoa má.'
    linha17 = 'Você nunca considerou a si mesmo bom ou mal, são apenas estado de espírito. Além disso,'
    linha18 = 'não há como saber qual seria a tendência moral do fabricante da arma.'
    linha19 = 'Se quiser correr o risco e tocar o cajado, aperte 1' #cena 11
    linha20 = 'Se ainda não investigou a estatueta e quer fazê-lo agora, aperte 2' #cena 3
    linha21 = 'Se quer sair da sala sem tocar em mais nada, aperte 3' #20

    imprimir_texto(linha1, linha1v, 10, 20,branco)
    imprimir_texto(linha2, linha1v, 10, 45,branco)
    imprimir_texto(linha3,linha1v, 10, 70,branco)
    imprimir_texto(linha4,linha1v, 10, 95,vermelho)
    imprimir_texto(linha5,linha1v,10, 120,vermelho)
    imprimir_texto(linha6,linha1v,10,145,branco)
    imprimir_texto(linha7,linha1v,10,170,vermelho)
    imprimir_texto(linha8,linha1v,10,195,vermelho)
    imprimir_texto(linha9,linha1v,10,220,vermelho)
    imprimir_texto(linha10,linha1v,10,245,vermelho)
    imprimir_texto(linha11, linha1v, 10, 270,vermelho)
    imprimir_texto(linha12, linha1v, 10, 295,vermelho)
    imprimir_texto(linha13,linha1v, 10, 320,vermelho)
    imprimir_texto(linha14,linha1v, 10, 345,vermelho)
    imprimir_texto(linha15,linha1v,10, 370,vermelho)
    imprimir_texto(linha16,linha1v,10,395,vermelho)
    imprimir_texto(linha17,linha1v,10,420.,branco)
    imprimir_texto(linha18,linha1v,10,445,branco)
    imprimir_texto(linha19, linha1v, 10, 500,branco)
    imprimir_texto(linha20,linha1v,10,550,branco)
    imprimir_texto(linha21, linha1v, 10, 600,branco)

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_1:
    				a = True
    				proximafase= 11
    			if event.key == pygame.K_2:
    				a = True
    				proximafase = 3
    			if event.key == pygame.K_3:
    				a = True
    				proximafase = 20

def fase3():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg7.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'A estátua é de ouro, com quase trinta centímetros de altura. É belíssima, representando as'
    linha1v = ' '
    linha2 = 'formas delicadas de uma fada com precisão impecável. Você suponha que se for original, a'
    linha3 = 'peça chegue a valer uma fortuna, e se for falsa, você quer conhecer esse gênio que a criou '
    linha4 = 'e levá-lo para trabalhar na guilda. Após a investigação, a põe em sua mochila.'
    linha5 = 'Se ainda não investigou o cetro e quer faze-lo agora, aperte 1. '#cena 8
    linha6 = 'Se prefere abandonar a sala, aperte 2' #cena 20
    

    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 140,branco)
    imprimir_texto(linha6,linha1v,20,200,branco)

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_1:
    				a = True
    				proximafase= 8
    			if event.key == pygame.K_2:
    				a = True
    				proximafase = 20

def fase7():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg12.png") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Sarah é reclusa, mas dificilmente resistiria a uma conversa com negociantes de objetos'
    linha1v = ''
    linha2 = 'mágicos. Ocultos sob seus disfarces, vocês adentram o portão do castelo e logo chegam'
    linha3 = 'a uma imensa porta de madeira, batem nela, e ouvem o que parece ser o som de passos cheg-'
    linha4 = 'ando perto da porta por dentro. O som parece metálico. Ao abrir a porta, vocês se deparam'
    linha5 = 'ram com a figura de um ser com uma armadura de batalha, mas ao olhar a face do mesmo'
    linha6 = 'veem que está vazia. '
    linha7 = 'Armadura animada:'
    linha8 = '- Quem deseja falar com a minha senhora?'
    linha9 = 'Atheris:'
    linha10 = '- Ouvimos falar da magnífica coleção de Sarah de Saalem e vimos negociar artefatos.'
    linha11 = 'Por um instante a armadura fica inerte, mas logo se move de lado esticando o braço, '
    linha12 = 'como forma de convidar para entrar.'
    linha13 = 'Armadura animada:'
    linha14 = '- Minha senhora irá recebê-los.'
    linha15 = 'Vocês são instruídos a aguardarem em um saguão de entrada, luxuosamente decorado, '
    linha16 = 'há varias armaduras perfiladas junto as paredes (inanimadas, você espera), e uma grande'
    linha17 = 'lareira ao norte. Então, um arrepio pavoroso percorre seus ossos. sobre a lareira, você '
    linha18 = 'reconhece um tridente mágico. Aquele que havia sido levado por Eduardrus Milus, um'
    linha19 = 'gladiador que fazia parte deu seu grupo original de heróis. E você pensa, se ela recuperou'
    linha20 =  'o tridente, Eduadrus está morto!'
    linha21 = 'Seus ouvidos começam a escutar passos pesados descendo as escadas, você pensa que ela'
    linha22= 'pode reconhecer sua capa e o cajado de Negreitos.'
    linha23= 'Atheris:'
    linha24= '- Vamos cair fora daqui!'
    linha25= 'Você fala pra Negreitos, enquanto sai correndo, movidos pela adrenalina vocês conseguem'
    linha26= 'abrir a porta pesada e saem correndo para se esconder nas rochas.'#fase26
    linha27='Aperte espaço para continuar'
    
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,branco)
    imprimir_texto(linha7,linha1v,20,170,vermelho)
    imprimir_texto(linha8,linha1v,20,195,vermelho)
    imprimir_texto(linha9,linha1v,20,220,vermelho)
    imprimir_texto(linha10,linha1v,20,245,vermelho)
    imprimir_texto(linha11, linha1v, 20, 270,branco)
    imprimir_texto(linha12, linha1v, 20, 295,branco)
    imprimir_texto(linha13,linha1v, 20, 320,vermelho)
    imprimir_texto(linha14,linha1v, 20, 345,vermelho)
    imprimir_texto(linha15,linha1v,20, 370,branco)
    imprimir_texto(linha16,linha1v,20,395,branco)
    imprimir_texto(linha17,linha1v,20,420,branco)
    imprimir_texto(linha18,linha1v,20,445,branco)
    imprimir_texto(linha19, linha1v, 20, 470,branco)
    imprimir_texto(linha20,linha1v,20,495,branco)
    imprimir_texto(linha21, linha1v, 20, 520,branco)
    imprimir_texto(linha22, linha1v, 20, 545,branco)
    imprimir_texto(linha23, linha1v, 20, 570,vermelho)
    imprimir_texto(linha24,linha1v,20,595,vermelho)
    imprimir_texto(linha25, linha1v, 20, 620,branco)
    imprimir_texto(linha26, linha1v, 20, 645,branco)
    imprimir_texto(linha27, linha1v, 250, 670,branco)
    
    a = False
    while a == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    a = True
                    proximafase=26 
def fase12():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg12.png") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Você imagina que uma proposta de adesão a Guilda dos Ladrões possa interessar a Sarah.'
    linha1v = ''
    linha2 = 'E até não há problemas em se apresentar como membro da guilda porque realmente você'
    linha3 = 'é dela. A guilda não sabe dessa nova proposta, mas você pode resolver isso quando'
    linha4 = 'for líder.'
    linha5 = 'Logo adentram o portão do castelo e chegam a uma imensa porta de madeira. '
    linha6 = 'batem nela e ouvem o que parece ser o som de passos chegando perto da porta por dentro.'
    linha7 = 'O som parece um pouco metálico. Ao abrir a porta, vocês se deparam com a figura de um ser'
    linha8 = 'com uma armadura de batalha, mas ao olhar a face do mesmo veem que esta vazia.'
    linha9 = 'Armadura animada:'
    linha10 = '- Quem deseja falar com a minha senhora?'
    linha11 = 'Diz a arrepiante armadura com uma voz metálica.'
    linha12 = 'Você tenta usar sua lábia para convencer a armadura que ela deve liberar sua entrada,'
    linha13 = 'mas ela não parece se interessar.'
    linha14 = 'Armadura animada:'
    linha15 = '- Minha senhora não negocia com ladrões!'
    linha16 = 'Diz a armadura, encerrando a conversa e levando a mão a espada na cintura. Vocês'
    linha17 = 'sem nem pensar, saem correndo, e aliviados percebem que a armadura não os seguiu .'
    linha18 = 'Atheris:'
    linha19 = '-Você e seus disfarces idiotas! Agora vamos esperar o anoitecer.'
    linha20 = 'Negreitos:'
    linha21 = '-Não olhe para mim, foi sua ideia nada sábia de chamar ela para guilda. Agora ela sabe da'
    linha22 = 'presença de ladrões rondando o castelo dela.'
    linha23 = 'Aperte espaço para continuar'#cena26
    
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,branco)
    imprimir_texto(linha7,linha1v,20,170,branco)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,220,vermelho)
    imprimir_texto(linha10,linha1v,20,245,vermelho)
    imprimir_texto(linha11, linha1v, 20, 270,branco)
    imprimir_texto(linha12, linha1v, 20, 295,branco)
    imprimir_texto(linha13,linha1v, 20, 320,branco)
    imprimir_texto(linha14,linha1v, 20, 345,vermelho)
    imprimir_texto(linha15,linha1v,20, 370,vermelho)
    imprimir_texto(linha16,linha1v,20,395,branco)
    imprimir_texto(linha17,linha1v,20,420,branco)
    imprimir_texto(linha18,linha1v,20,445,vermelho)
    imprimir_texto(linha19, linha1v, 20, 470,vermelho)
    imprimir_texto(linha20,linha1v,20,495,vermelho)
    imprimir_texto(linha21, linha1v, 20, 520,vermelho)
    imprimir_texto(linha22, linha1v, 20, 545,vermelho)
    imprimir_texto(linha23, linha1v, 250, 585,branco)

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_SPACE:
    				a = True
    				proximafase=26

def fase26():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg7.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Ocultos entre as rochas, vocês esperam a noite chagar.Usando as habilidades que as'
    linha1v = ' '
    linha2 = 'experiências que anos de roubos lhes deram, vocês se aproximam do castelo de Sarah.'
    linha3 = 'Decidem que a melhor forma é pular o muro e entrar por uma das janelas do segundo'
    linha4 = 'andar. Você vai primeiro. A capa permite que suas mãos e pés se grudem as paredes'
    linha5 = 'e você escala como se fosse uma aranha. Negreitos se transforma em um mico e sobe'
    linha6 = 'facilmente. Ao chegar na janela, você vê que elas são reforçadas por grossas barras'
    linha7 = 'de metal.'
    linha8 = 'Você olha para Negreitos e diz.'
    linha9 = 'Atheris:'
    linha10 = '- Negreitos, tens alguma magia que possa nos ajudar?'
    linha11 = 'Negreitos:'
    linha12 = '- Não sou um mago. Meus poderes são um presente dos deuses por minha devoção.'
    linha13 = 'Mas sim, creio que posso ajudar...'
    linha14 = 'É engraçado ver o mico juntando as mãos e se ajoelhando para rezar, até que os resultados'
    linha15 = 'das preces fazem efeito e as barras começam a brilhar com uma luz fantasmagórica, '
    linha16 = 'e você assiste o metal desmanchar diante de seus olhos.'
    linha17 = 'Atheris:'
    linha18 = '- Como você fez isso?'
    linha19='Aperte espaço para continuar.' #Cena 8

    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,branco)
    imprimir_texto(linha7,linha1v,20,170,branco)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,220,vermelho)
    imprimir_texto(linha10,linha1v,20,245,vermelho)
    imprimir_texto(linha11, linha1v, 20, 270,vermelho)
    imprimir_texto(linha12, linha1v, 20, 295,vermelho)
    imprimir_texto(linha13,linha1v, 20, 320,vermelho)
    imprimir_texto(linha14,linha1v, 20, 345,branco)
    imprimir_texto(linha15,linha1v,20, 370,branco)
    imprimir_texto(linha16,linha1v,20,395,branco)
    imprimir_texto(linha17,linha1v,20,420,vermelho)
    imprimir_texto(linha18,linha1v,20,445,vermelho)
    imprimir_texto(linha19, linha1v, 250, 490,branco)

    a = False
    while a == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    a = True
                    proximafase= 42
    			

def fase32():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg32.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'As ideias de Negreitos sempre são boas e divertidas. Ele é bom de disfarces. Caberá'
    linha1v = ''
    linha2 = 'a você inventar uma história convincente antes de bater na porta de Sarah.'
    linha3 = 'Se quiser apresentar-se como negociante de artefatos mágicos, aperte 1.'#cena7
    linha4 = 'Se prefere agir sob o disfarce de emissário da Guilda, aperte 2.'#cena12
   
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 120,branco)
    imprimir_texto(linha4,linha1v, 20, 165,branco)

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_1:
    				a = True
    				proximafase= 7
    			if event.key == pygame.K_2:
    				a = True
    				proximafase = 12

def fase2():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg32.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Vocês seguem viagem sem maiores incidentes. Então, por entre as montanhas surge o'
    linha1v = ''
    linha2 = 'castelo que serve de habitação a colecionadora de itens mágicos. Você se lembra que'
    linha3 = 'da outra vez que o invadiu estava acompanhado de bárbaros e poderosos magos. E que'
    linha4 = 'mesmo com eles, foi extremante difícil. O que o faz pensar que a situação merece'
    linha5 = 'um pouco mais cuidado.'
    linha6 = 'Negreitos:'
    linha7 = '- Eu tenho uma ideia! podemos nos disfarçar e entrar no castelo para verificarmos o'
    linha8 = 'interior antes de realizar o assalto.'
    linha9 = 'Você por outro lado pensa em esperar o cair da noite para a invasão.'
    linha10 = 'Se quiser seguir o conselho de Negreitos, aperte 1.'#cena32
    linha11 = 'Se prefere usar sua estratégia, aperte 2. '#cena26 

    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,vermelho)
    imprimir_texto(linha7,linha1v,20,170,vermelho)
    imprimir_texto(linha8,linha1v,20,195,vermelho)
    imprimir_texto(linha9,linha1v,20,220,branco)
    imprimir_texto(linha10,linha1v,20,260,branco)
    imprimir_texto(linha11, linha1v, 20, 290,branco)

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_1:
    				a = True
    				proximafase= 32
    			if event.key == pygame.K_2:
    				a = True
    				proximafase = 26

def fase18():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg10.png") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Você acha melhor não abusar da sorte e decide se afastar. Pode ser que dessa vez ele'
    linha1v = ''
    linha2 = 'perceba. Depois de um tempo, o cavaleiro vai embora e vocês investigam o que tinha no'
    linha3 = 'saco. Havia várias moedas, uma pérola valiosa e um pergaminho que detinha ordens reais'
    linha4 = 'para prisão do “o Aranha”, capturado vivo ou morto. Negreitos fica com as moedas e'
    linha5 = 'você fica com a pérola.'
    linha6 = 'Negreitos:'
    linha7 = '-Imagina os problemas que ele vai ter ao chegar na cidade sem as ordens.'
    linha8 = 'Vocês gargalham e decidem seguir viagem.'#fase2
    linha9 = 'Aperte Espaço para continuar'

    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,vermelho)
    imprimir_texto(linha7,linha1v,20,170,vermelho)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,240,branco)

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_SPACE:
    				a = True
    				proximafase= 2
def morte():
    global tela, branco
    bg0 = pygame.image.load("Imagens/morte.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    pygame.display.update()
    pygame.mixer.music.load('Audio/morte.mp3')
    pygame.mixer.music.play(1)
    time.sleep(180)
    sys.exit()
def fase17():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg17.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Sua mão desliza silenciosamente na direção do cabo da adaga. No exato momento em que'
    linha1v = ''
    linha2 = 'iria pegá-la, um punho fecha-se veloz sobre seu pulso e aperta com a força de um gigante,'
    linha3 = 'esmigalhando seus ossos.'
    linha4 = 'Cavaleiro:'
    linha5 = '- Ah larápio! Agora percebo! Sua descrição combina com a do maldito Aranha. Pagará por'
    linha6 = 'seus crimes, bandido!'
    linha7 = 'A lâmina desce com força e você sucumbe à explosão de dor. Só voltando a abrir os'
    linha8 = 'olhos novamente no outro dia e descobre que está em um acampamento aquecido por uma'
    linha9 = 'fogueira. Negreitos está a seu lado entoando preces de cura.'
    linha10 = 'Atheris:'
    linha11 = '- O que aconteceu?'
    linha12 = 'Negreitos:'
    linha13 = '- Você abusou da sorte. E abusou dos deuses. foi o que aconteceu. Meu cajado esmagou o'
    linha14 = 'crânio do maldito guarda antes que o pior acontecesse. Mas creio que seus dias como'
    linha15 = 'o Aranha chegaram ao fim.'
    linha16 = 'Atheris:'
    linha17 = '- Do que você está falando?'
    linha18 = 'Você entende as palavras de Negreitos e ao tentar segurar seu braço, nota que ele'
    linha19 = 'foi cortado na altura do ombro. Sim, sua carreira acaba aqui.'#morte
    																			
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,vermelho)
    imprimir_texto(linha5,linha1v,20, 120,vermelho)
    imprimir_texto(linha6,linha1v,20,145,vermelho)
    imprimir_texto(linha7,linha1v,20,170,branco)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,220,branco)
    imprimir_texto(linha10,linha1v,20,245,vermelho)
    imprimir_texto(linha11, linha1v, 20, 270,vermelho)
    imprimir_texto(linha12, linha1v, 20, 295,vermelho)
    imprimir_texto(linha13,linha1v, 20, 320,vermelho)
    imprimir_texto(linha14,linha1v, 20, 345,vermelho)
    imprimir_texto(linha15,linha1v,20, 370,vermelho)
    imprimir_texto(linha16,linha1v,20,395,vermelho)
    imprimir_texto(linha17,linha1v,20,420,vermelho)
    imprimir_texto(linha18,linha1v,20,445,branco)
    imprimir_texto(linha19, linha1v, 20, 470,branco)
    time.sleep(15)
    morte()
      
def fase4():
    global tela, branco, proximafase
    bg0 = pygame.image.load("Imagens/bg10.png") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Por mais tentador que seja a ideia de voltar aos velhos tempos, a prudência recomenda que'
    linha1v = ''
    linha2 = 'deixem o viajante seguir. Afinal, ele usa armadura da guarda real. Demonstrando que'
    linha3 = 'ele não era um cavaleiro qualquer.'
    linha4 = 'Vocês passam pelo cavaleiro encobrindo o rosto e murmurando cumprimentos. Quando ele '
    linha5 = 'está longe, Negreitos diz.'
    linha6 = 'Negreitos:'
    linha7 = '- Desperdiçamos uma chance de agradar o meu Deus, isso desapontará Ele.'
    linha8 = 'Mas você prefere contrariar a fé de Negreitos do que enfrentar um guarda real e'
    linha9 = 'possivelmente um exército deles depois.'
    linha10= 'Aperte espaço para continuar.'

    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,vermelho)
    imprimir_texto(linha7,linha1v,20,170,vermelho)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,220,branco)
    imprimir_texto(linha10,linha1v,20,260,branco)

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_SPACE:
    				a = True
    				proximafase=2
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

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_1:
    				a = True
    				proximafase=17
    			if event.key == pygame.K_2:
    				a = True
    				proximafase = 18
def fase10():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg10.png") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Depois de comprar suprimentos e 2 cavalos, vocês partem para a montanha onde fica o caste-'
    linha1v = ''
    linha2 = 'lo da feiticeira Sarah de Saalem. Em 7 dias de viagem vocês chegam a floresta dos galhos'
    linha3 = 'partidos, última parada antes da montanha e algo surpreende vocês. Um cavaleiro de arma-'
    linha4 = 'dura sobre o lombo de um majestoso cavalo branco. Suas vestes são luxuosas e fazem'
    linha5 = 'com que você e Negreitos troquem olhares sorrateiros.'
    linha6 = 'Negreitos:'
    linha7 = '- Que tal fazermos uma oferenda ao Deus da trapaça?'
    linha8 = 'Propõe Negreitos assaltar esse cavaleiro. Pode ser perigoso, mas por outro lado, ele pode'
    linha9 = 'estar carregando alguns itens ou até jóias valiosas.'
    linha10 = 'Se você aceita o convite de Negreitos para um assalto, aperte 1.' #cena21
    linha11 = 'Se você prefere deixar o homem seguir em paz, aperte 2.' #cena4
    
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,vermelho)
    imprimir_texto(linha7,linha1v,20,170,vermelho)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,220,branco)
    imprimir_texto(linha10,linha1v,250,255,branco)
    imprimir_texto(linha11, linha1v, 250, 295,branco)

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_1:
    				a = True
    				proximafase=21
    			if event.key == pygame.K_2:
    				a = True
    				proximafase = 4
def fase37():
    global tela, branco, proximafase
    bg0 = pygame.image.load("Imagens/37bg.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    
    linha1 = 'Ao sair da cidade, você chega a conclusão que realmente não seria bom levar Negreitos'
    linha1v = ''
    linha2 = 'com você e que ele poderia não estar de acordo com suas ambições. Depois de alguns'
    linha3 = 'minutos de viagem, você escuta uma susurro ao pé do ouvido.'
    linha4 = 'Negreitos:'
    linha5 = '- Partindo para uma aventura sem seu colega, Aranha?'
    linha6 = 'Você se assusta, e procura ao redor quem poderia ter dito aquilo. Não vê ninguém,'
    linha7 = 'volta seu olhar para o mico e vê um pequeno sorriso naquele rosto peludo.'
    linha8 = 'Atheris:'
    linha9 = '- Negreitos, é você!?'
    linha10 = 'Você grita e o mico pula do seu ombro. Como num passe de mágica, aquele corpo pequeno'
    linha11 = 'e peludo ganha feições conhecidas. Nesse mesmo instante, você lembra que os clérigos'
    linha12 = 'do Deus dos ladrões tinham esse poder e vê Negreitos em roupa de sacerdote dos deuses.'
    linha13 = 'Negreitos:'
    linha14 = '- Meio bem útil de seguir algumas pessoas, não?! Mas não se preocupe, estou aqui'
    linha15 = 'apenas para ajudar. E sim, irei com você. Nem precisa insistir. Hahahahaha'
    linha16 = 'Você se pergunta o que terá acontecido com o outro mico e se Negreitos esteve em seu '
    linha17 = 'ombro esse tempo todo. Então, chega a conclusão que é melhor nem o questioná-lo.'
    linha18 = 'Aperte espaço para continuar.'
   
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
    imprimir_texto(linha13,linha1v, 20, 320,vermelho)
    imprimir_texto(linha14,linha1v, 20, 345,vermelho)
    imprimir_texto(linha15,linha1v,20, 370,vermelho)
    imprimir_texto(linha16,linha1v,20,395,vermelho)
    imprimir_texto(linha17,linha1v,20,420,branco)
    imprimir_texto(linha18,linha1v,20,465,branco)
    

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_SPACE:
    				a = True
    				proximafase=10


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

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_SPACE:
    				a = True
    				proximafase=10
    			

def fase1():
    global tela, branco, proximafase
    bg0 = pygame.image.load("Imagens/bg1.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Decidido a penetrar novamente o castelo da bruxa Sarah de Saalem, você chega à conclusão'
    linha1v = ''
    linha2 = 'que precisará de 2 coisas: Um macaco treinado para furtos, que será fácil conseguir;'
    linha3 = 'e de seu antigo e habilidoso companheiro de furtos, Negreitos, clérigo do Deus da'
    linha4 = 'trapaça e dos ladrões. Mas a dúvida se ele seria confiável ou não se instaura em '
    linha5 = 'sua cabeça. Depois de conseguir o mico, só falta uma decisão a tomar.'
    linha6 = 'Se você deseja convidar Negreitos para participar do roubo, aperte 1.' #fase24
    linha7 = 'Se não confia no clérigo e prefere agir sozinho, aperte 2.' #fase37
    
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,250,450,branco)
    imprimir_texto(linha7,linha1v,250,500,branco)

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_1:
    				a = True
    				proximafase=24
    			if event.key == pygame.K_2:
    				a = True
    				proximafase = 37
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
	proximafase = 1		
	
	# pygame.mixer.music.stop()
	
pygame.mixer.music.load('Audio/title.mp3')
pygame.mixer.music.play(-1)

#Loop do Menu
b = True
while b == True:
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
            b =  False
        if keys[pygame.K_SPACE]:
            prologo()
            fase1()
        if proximafase == 24:
        	fase24()
        if proximafase == 37:
        	fase37()
        if proximafase == 10:
        	fase10()
        if proximafase == 21:
        	fase21()
        if proximafase == 17:
        	fase17()
       	if proximafase == 18:
        	fase18()
        if proximafase == 4:
        	fase4()
        if proximafase == 2:
        	fase2()
        if proximafase == 32:
        	fase32()
        if proximafase == 12:
        	fase12()
        if proximafase == 7:
        	fase7()
        if proximafase == 26:
        	fase26()
        if proximafase == 3:
        	fase3()
        if proximafase == 8:
        	fase8()
        if proximafase == 11:
        	fase11()
        if proximafase == 20:
        	fase20()
        if proximafase == 29:
        	fase29()
        if proximafase == 39:
        	fase39()
        if proximafase == 34:
        	fase34()
        if proximafase == 23:
        	fase23()
        if proximafase == 13:
        	fase13()
        if proximafase == 19:
        	fase19()
        if proximafase == 33:
        	fase33()
        if proximafase == 35:
        	fase35()
        if proximafase == 40:
        	fase40()
        if proximafase == 42:
        	fase42()
        if keys[pygame.K_ESCAPE]:
        	b = False
        	sys.exit()
	# if keys[pygame.K_F12]:
	# 	pygame.display.toggle_fullscreen()
	# 	pygame.display.toggle_fullscreen()
        pygame.display.update()



