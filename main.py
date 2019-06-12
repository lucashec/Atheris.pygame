import pygame
import sys
import mixer


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
	linha11='Muito bom esse chapéu de disfarce, suas ilusões poderiam enganar a qualquer um.'
	linha12='Atheris:'
	linha13='Não precisam enganar mais ninguém, se o corpo do chefe for encontrado não fará mais dife-'
	linha14='rença. agora "ele" já passou o cargo para mim, certo?'
	linha15='Sim, foi um bom plano: matar o chefe, e usar o chapéu mágico de Sarah para criar a ilusão'
	linha16='de que Negreitos era ele. Parabéns, você conseguiu. É o novo chefão da Guilda de Ladrôes.'
	linha17='-Pelo menos até que alguém apareça com um plano mais astucioso do que o seu!'
	
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

	vitoria()

def fase35():
	global tela, branco, proximafase
	bg0 = pygame.image.load("Imagens/bg35.jpg")
	bg0 = pygame.transform.scale(bg0,(1080,700))
	tela.blit(bg0,(0,0))
	linha1='Tendo vencido Sarah. você pode examinar sua coleção com mais calma. Dentre uma infini-'
	linha1v=''
	linha2='dade de itens, você encontra o que parece ser um chapéu vulgar - mas é exatamente o que'
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
	linha10='no chão, entre seus pés. Como você planejou, o chão não resiste e desaba- levando Sarah'
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

	morte()
		
def fase13():
	global tela, branco, proximafase
	bg0 = pygame.image.load("Imagens/34bg.jpg")
	bg0 = pygame.transform.scale(bg0,(1080,700))
	tela.blit(bg0,(0,0))
	linha1='Você segue num corredor iluminado por tochas e depois da alguns minutos, chega ao fim'
	linha1v=''
	linha2='da linha, uma extensa parede no final do corredor. Você suspeita que possa ter algo'
	linha3='após a parede, e pela sua intuição e experiência, resolve puxar uma tocha que está iso-'
	linha4='lada a esquerda da parede. A parede se movimenta e revela um porão da torre. Vocês so-'
	linha5='bem as escadas, chegam ao saguão e logo alcançam a sala principal da coleção de Sarah.'
	linha6='Desta vez tomam cuidado para evitar o tapete traiçoeiro. Examinando a coleção, encontram' 
	linha7='o cajado e a capa de Negreitos. De repente, após uma explosão como a de um trovão, surge '
	linha8='Sarah, -desta vez armada com seu martelo de guerra.'
	linha9='Sarah:'
	linha10='-Malditos ladrões! Vocês querem minhas armas! Mas não vou permitir que roubem, eu terei'
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
	linha2='no aposento, Negreitos comenta com desdém sobre a lenda dos almas dos prisioneiros mor='
	linha3='tos no castelo que supostamente se transformariam em zumbi. Que azar! sua intuição erra'
	linha4='e a sala não estava vazia como imaginava. Um zumbi desencarndo surge sob as ordens de seu'
	linha5='mestre. O silêncio dos mortos-vivos o enganou. Vocês comprovam da pior forma que a lenda'
	linha6='é verdadeira. As garras dos monstros enterram-se em sua gargante antes que Negreitos consiga'
	linha7='esconjurá-lo.'#morte
	
	imprimir_texto(linha1, linha1v, 20, 20,branco)
	imprimir_texto(linha2, linha1v, 20, 45,branco)
	imprimir_texto(linha3,linha1v, 20, 70,branco)
	imprimir_texto(linha4,linha1v, 20, 95,branco)
	imprimir_texto(linha5,linha1v,20, 120,branco)
	imprimir_texto(linha6,linha1v,20,145,branco)
	imprimir_texto(linha7,linha1v,20,170,branco)

	morte()
def fase29():
    global tela, branco
    bg0 = pygame.image.load("Imagens/bg20.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Você examina a fechadura e começa a cutucá-la com seu estojo de ferramentas. Ao'
    linha1v = ' '
    linha2 = 'seu lado, Negreitos retorna à forma humana com um desabafo.'
    linha3 = 'Negreitos:'
    linha4 = '-Não acredito em meus olhos! Por onde anda sua antiga astúcia, amigo Atheris? Por que está'
    linha5 = 'procurando armadilhas no lado de dentro de uma porta? Francamente...'
    linha6 = 'Irritado com sua momentânea incompetência para o ramo, Negreitos avança e mete o pé na'
    linha7 = 'porta, escancarando-a, sem se preocupar com o que há no outro lado.'
    linha8 = 'E logo se arrepende.'
    linha9 = 'A porta leva para um corredor, que a princípio parece vazio. Apenas a princípio, porque da'
    linha10 = 'escuridão surge um cão enorme, um mastim realmente assustador, com presas demoníacas'
    linha11 = 'curvando-se para fora da boca. Um cão estranhamente silencioso.'
    linha12 = 'Você saca o punhal e prepara-se para a luta, mas... seria só sua imaginação?!'
    linha13 = 'Infelizmente, não era imaginação. Aquilo não era um cão de guarda comum, mas sim um'
    linha14 = 'cadáver animado, certamente invocado por Sarah para proteger seu castelo nesta noite tão'
    linha15 = 'suspeita. Despreparados para uma batalha contra um morto-vivo, você e Negreitos não '
    linha16 = 'conseguem sobreviver ao toque pestilento das garras da fera...' #morte
     
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,roxo)
    imprimir_texto(linha4,linha1v, 20, 95,roxo)
    imprimir_texto(linha5,linha1v,20, 120,roxo)
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
    imprimir_texto(linha16,linha1v,20,395,branco)

    morte()
def fase39():
	global tela, branco, proximafase
	bg0 = pygame.image.load("Imagens/bg20.jpg")
	bg0 = pygame.transform.scale(bg0,(1080,700))
	tela.blit(bg0,(0,0))
	linha1='Com o máximo de cuidado para não fazer ruído, você usa suas ferramentas'
	linha1v=''
	linha2='para tentar localizar armadilhas.E então percebe que há um mecanismo que'
	linha3='seria ativado ao abrir a porta. Logo, decide cortar o arame que servia de'
	linha4='gatilho. A porta leva a um aposento onde Sarah guarda as peças principais'
	linha5='de sua coleção. As parades são adornadas com espadas e armaduras reluzentes.'
	linha6='Vocês voltam a atenção para um grande tapete. Seria este um dos tais tapetes' 
	linha7='mágicos?! Você e Negreitos se aproximam para sentar no tapete... e caem. Vo-'
	linha8='cê acorda numa cela no calabouço da torre de Sarah. A porta da cela se abre, e'
	linha9='por ela entram dois guardas com armaduras, se trata de duas armaduras mágicas.'
	linha10='Elas se posicionam no lado porta e abrem passagem para... Sarah. Usando suas'
	linha11='peças favoritas a Espada Infernal,O Manto das Sombras,cajado e capa de Negreitos'
	linha12='Sarah:'
	linha13='Supreendem-me com sua audácia, seus ratos ladrões.'
	linha14='Ela agita a capa e o cajado diante de vocês. Sarah usa objetos mágicos para ampliar'
	linha15='sua força e mesmo sem armas poderia matá-los sem esforço.'
	linha16='Sarah:'
	linha17='A recompensa por sua tolice será a morte, mas não agora. Vocês interromperam meu sono.'
	linha18='Desejo estar descansada para sobrar seu sofrimento. Aproveitem sua última noite.'
	linha19='Você saca seu estojo de ferramentas que, felizmente, escapou da revista de Sarah e deci-'
	linha20='tentar abrir a fechadura da cela. Ela abre facilmente e Negreitos, de posse de seu símbolo'
	linha21='sagrado, esconjura as armaduras mágicas fazendo-as em pedaços. Vocês seguem por um '
	linha22='corredor e se deparam com uma bifurcação.'
	linha23='Se quiser pegar o caminho da direita, aperte 1.' #fase13
	linha24='Se quiser pegar o caminho da esquerda, aperte 2.' #fase34

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
	imprimir_texto(linha12, linha1v, 20, 295,vermelho)
	imprimir_texto(linha13,linha1v, 20, 320,vermelho)
	imprimir_texto(linha14,linha1v, 20, 345,branco)
	imprimir_texto(linha15,linha1v,20, 370,branco)
	imprimir_texto(linha16,linha1v,20,395,vermelho)
	imprimir_texto(linha17,linha1v,20,420,vermelho)
	imprimir_texto(linha18,linha1v,20,445,vermelho)
	imprimir_texto(linha19, linha1v, 20, 470,branco)
	imprimir_texto(linha20,linha1v,20,495,branco)
	imprimir_texto(linha21, linha1v, 20, 520,branco)
	imprimir_texto(linha22, linha1v, 20, 545,branco)
	imprimir_texto(linha23,linha1v,20,580,branco)
	imprimir_texto(linha24,linha1v,20,620,branco)

	a = False
	while a == False:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					a = True
					proximafase= 1
					if event.key == pygame.K_2:
						a = True
						proximafase = 34

def fase20():
    global tela, branco, proximafase
    bg0 = pygame.image.load("Imagens/bg20.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Você volta sua atenção para a única porta do aposento, perguntando-se o que'
    linha1v = ' '
    linha2 = 'haverá além dela.'
    linha3 = 'Se você quiser colocar o ouvido à porta e escutar, aperte 1' #cena 39
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
    linha2 = 'Guilda, e facilmente assumir seu lugar. É exatamente o que procurava. Sua mão aproxima-se'
    linha3 = 'do cetro, vacila um pouco... e fecha-se à volta dele.'
    linha4 = 'Seus dedos parecem dormentes, mas pode ser apenas o nervosismo. Abrindo os olhos, para'
    linha5 = 'seu horror, você vê faíscas azuis crepitando sobre seu pulso. Elas ficam maiores e maiores,'
    linha6 = 'queimando os pelos de seu braço, deixando manchas negras na pele, calcinando sua carne...'
    linha7 = 'e matando você.'
    linha8 = 'Diante do punhado de carvão que havia se chamando Atheris, o aranha, Negreitos mexe a'
    linha9 = 'cabeça lamentando.'
    linha10 = 'Negreitos:'
    linha11 = 'sinto muito, amigo Atheris. O deus da trapaça não estava com você. Uma pena.'
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
    linha5 = '-É uma arma mágica.'
    linha6 = 'Ainda na forma de mico.'
    linha7 = 'Negreitos:'
    linha8 = 'Já vi magos utilizando cajados assim para lançar relâmpagos. Mas toma cuidado, antes '
    linha9 = 'de tocá-la, amigo Atheris, o cajado pode ser uma arma formidável nas mãos da pessoa certa,'
    linha10 = 'mas pode matar a pessoa errada.'
    linha11 = 'Atheris:'
    linha12 = '-Como assim?'
    linha13 = 'Negreitos:'
    linha14 = '-É como o cão influenciado pela personalidade do dono. Se o construtor desta arma era ma-,'
    linha15 = 'ligno uma pessoa bondosa não poderá tocá-la sem sofrer dano; se era bom, queimará as mãos de'
    linha16 = 'uma pessoa má.'
    linha17 = 'Você nunca considerou a si mesmo bom ou mal; são apenas estado de espírito. Além disso,'
    linha18 = 'não há cmo saber qual seria a tendência moral do fabricante da arma.'
    linha19 = 'Se quiser correr o risco e tocar o cajado, aperte 1' #cena 11
    linha20 = 'Se ainda não investigou a estatueta e quer fazê-lo agora, aperte 2' #cena 3
    linha21 = 'Se quer sair da sala sem tocar em mais nada, aperte 3' #20

    imprimir_texto(linha1, linha1v, 10, 20,branco)
    imprimir_texto(linha2, linha1v, 10, 45,branco)
    imprimir_texto(linha3,linha1v, 10, 70,branco)
    imprimir_texto(linha4,linha1v, 10, 95,roxo)
    imprimir_texto(linha5,linha1v,10, 120,roxo)
    imprimir_texto(linha6,linha1v,10,145,roxo)
    imprimir_texto(linha7,linha1v,10,170,roxo)
    imprimir_texto(linha8,linha1v,10,195,roxo)
    imprimir_texto(linha9,linha1v,10,220,roxo)
    imprimir_texto(linha10,linha1v,10,245,roxo)
    imprimir_texto(linha11, linha1v, 10, 270,roxo)
    imprimir_texto(linha12, linha1v, 10, 295,roxo)
    imprimir_texto(linha13,linha1v, 10, 320,roxo)
    imprimir_texto(linha14,linha1v, 10, 345,roxo)
    imprimir_texto(linha15,linha1v,10, 370,roxo)
    imprimir_texto(linha16,linha1v,10,395,roxo)
    imprimir_texto(linha17,linha1v,10,420.,roxo)
    imprimir_texto(linha18,linha1v,10,445,roxo)
    imprimir_texto(linha19, linha1v, 10, 470,branco)
    imprimir_texto(linha20,linha1v,10,520,branco)
    imprimir_texto(linha21, linha1v, 10, 570,branco)

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
    linha2 = 'formas delicadas de uma fada com precisão impecável. Você suponha que se for original a'
    linha3 = 'peça chegue a valer uma fortuna, e se for falsa, você quer conhecer esse gênio que a criou '
    linha4 = 'e levá-lo para trabalhar na guilda. Você coloca a estátua na mochila.'
    linha5 = 'Se ainda não investigou o cetro e quer faze-lo agora, aperte 1. '#cena 8
    linha6 = 'Se prefere abandonar a sala, aperte 2' #cena 20
    

    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 140,branco)
    imprimir_texto(linha6,linha1v,20,185,branco)

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
    linha2 = 'mágicos. Ocultos sobre seus disfarces, vocês adentram o portão do castelo e logo chegam'
    linha3 = 'a uma imensa porta de madeira, batem nela, e ouvem o que parece ser o som de passos cheg-'
    linha4 = 'ando perto da porta por dentro. O som parece metálico. Ao abrir a porta, vocês se deparam '
    linha5 = 'ram com a figura de um ser com uma armadura de batalha, mas ao olhar '
    linha6 = 'a face do mesmo veem que está vazia. '
    linha7 = 'Armadura animada:'
    linha8 = '-Quem deseja falar com minha senhora?'
    linha9 = 'Diz a arrepiante armadura com uma voz metálica.'
    linha10 = 'Atheris:'
    linha11 = '-Ouvimos falar da magnífica coleção de Sarah de Saalem, e viemos negociar artefatos.'
    linha12 = '-Por um instante a armadura fica inerte, mas logo se move de lado esticando o braço, '
    linha13 = 'como forma de convidar para entrar.'
    linha14 = 'Armadura animada:'
    linha15 = '-Minha senhora irá recebe-los.'
    linha16 = 'Vocês são instruídos a aguardarem em um saguão de entrada, luxuosamente decorado, '
    linha17 = 'há varias armaduras perfiladas junto as paredes (inanimadas, você espera), e uma grande'
    linha18 = 'lareira ao norte. Então um arrepio pavoroso percorre seus ossos: sobre a lareira você '
    linha19 = 'reconhece um tridente magico, aquele que havia sido levado por Eduardrus Milus, um'
    linha20 = 'gladiador que fazia parte deu seu grupo original de heróis. E você pensa que se ele recupe-'
    linha21 = 'rou o tridente, Eduadrus está morto!'
    linha22 = 'Seus ouvidos começam a escutar passos pesados descendo as escadas, e você pensa que'
    linha23= 'ele irá reconhecer sua capa e o cajado de Negreitos.'
    linha24= 'Atheris'
    linha25= '-Vamos cair fora daqui!'
    linha26= 'Você fala pra Negreitos, enquanto sai correndo, movidos pela adrenalina vocês conseguem'
    linha27= 'abrir a porta pesada e saem correndo para se esconder nas rochas.'#fase26
    
    imprimir_texto(linha1, linha1v, 20, 20,branco)
    imprimir_texto(linha2, linha1v, 20, 45,branco)
    imprimir_texto(linha3,linha1v, 20, 70,branco)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,branco)
    imprimir_texto(linha7,linha1v,20,170,vermelho)
    imprimir_texto(linha8,linha1v,20,195,vermelho)
    imprimir_texto(linha9,linha1v,20,220,branco)
    imprimir_texto(linha10,linha1v,20,245,vermelho)
    imprimir_texto(linha11, linha1v, 20, 270,vermelho)
    imprimir_texto(linha12, linha1v, 20, 295,branco)
    imprimir_texto(linha13,linha1v, 20, 320,branco)
    imprimir_texto(linha14,linha1v, 20, 345,vermelho)
    imprimir_texto(linha15,linha1v,20, 370,vermelho)
    imprimir_texto(linha16,linha1v,20,395,branco)
    imprimir_texto(linha17,linha1v,20,420,branco)
    imprimir_texto(linha18,linha1v,20,445,branco)
    imprimir_texto(linha19, linha1v, 20, 470,branco)
    imprimir_texto(linha20,linha1v,20,495,branco)
    imprimir_texto(linha21, linha1v, 20, 520,branco)
    imprimir_texto(linha22, linha1v, 20, 545,branco)
    imprimir_texto(linha23, linha1v, 20, 570,branco)
    imprimir_texto(linha24,linha1v,20,595,vermelho)
    imprimir_texto(linha25, linha1v, 20, 620,vermelho)
    imprimir_texto(linha26, linha1v, 20, 645,branco)
    imprimir_texto(linha27, linha1v, 20, 670,branco)
    
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
    linha10 = '-Quem deseja falar com minha senhora?'
    linha11 = 'Diz a arrepiante armadura com uma voz metálica.'
    linha12 = 'Você tenta usar sua lábia para convencer a armadura que ela deve liberar sua entrada,'
    linha13 = 'mas ela não parece se interessar.'
    linha14 = 'Armadura animada:'
    linha15 = '-Minha senhora não negocia com ladrões!'
    linha16 = 'Diz a armadura, encerrando a conversa e levando a mão a espada na cintura. Vocês'
    linha17 = 'sem nem pensar, saem correndo, e aliviados percebem que a armadura não os seguiu .'
    linha18 = 'Atheris:'
    linha19 = '-Você e seus disfarces idiotas! Agora vamos esperar o anoitecer.'
    linha20 = 'Negreitos:'
    linha21 = '-Não olhe para mim! Foi sua ideia nada sábia de chamar ela para guilda. Agora ela sabe da'
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
    linha2 = 'experiências de anos de roubos lhes deram, vocês se aproximam do castelo de Sarah.'
    linha3 = 'Decidem que a melhor forma é pular o muro e entrar por uma das janelas do segu-'
    linha4 = 'segundo andar. Você vai primeiro. A capa permite que suas mãos e pés se grudem as '
    linha5 = 'paredes e você escala como se fosse uma aranha. Negreitos se transforma em um mico'
    linha6 = 'e sobe facilmente. '
    linha7 = 'Ao chegar na janela você vê que elas são reforçadas por grossas barras de metal. '
    linha8 = 'Você olha para Negreitos e diz.'
    linha9 = 'Atheris:'
    linha10 = '-Então, Negreitos? Tens aí alguma magia que possa nos ajudar?'
    linha11 = 'Negreitos:'
    linha12 = '-Não sou um mago. Meus poderes são um presente dos deuses por minha devoção.'
    linha13 = 'Mas sim, creio que posso ajudar...'
    linha14 = 'É engraçado ver o mico juntando as mãos e se ajoelhando para rezar, até que os resultados'
    linha15 = 'das preces fazem efeito e as barras começam a brilhar com uma luz fantasmagórica, '
    linha16 = 'e você assiste o metal desmanchar diante de seus olhos.'
    linha17 = 'Atheris:'
    linha18 = '-Como Você fez isso'
    linha19 = 'Negreitos:'
    linha20 = '-Não fiz nada, amigo. Foram os deuses que, a meu pedido, envelheceram as grades mil anos.'
    linha21 = 'Você fica alegre por ter aquele clérigo a seu lado, você entra no aposento. Tira uma pedra'
    linha22 = 'mágica da mochila, balança, e ela começa a brilhar, iluminando o lugar. Olhando bem'
    linha23='parece que parte dos equipamentos mágicos estão aqui. As paredes têm lanças, alabardas,'
    linha24='tridentes e outras armas de grande porte. Devem ser poderosas nas mãos de guerreiros,'
    linha25='mas não interessam a vocês.'
    linha26='Procurando por algo que valha a pena, você nota 2 objetos que chamam sua atenção.'
    linha27='Um cetro, suspenso na parede, tendo em sua ponta um cristal transparente. Se quiser'
    linha28='Se quiser pegá-lo, aperte espaço.' #Cena 8



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
    imprimir_texto(linha14,linha1v, 20, 345,vermelho)
    imprimir_texto(linha15,linha1v,20, 370,vermelho)
    imprimir_texto(linha16,linha1v,20,395,vermelho)
    imprimir_texto(linha17,linha1v,20,420,vermelho)
    imprimir_texto(linha18,linha1v,20,445,vermelho)
    imprimir_texto(linha19, linha1v, 20, 470,vermelho)
    imprimir_texto(linha20,linha1v,20,495,vermelho)
    imprimir_texto(linha21, linha1v, 20, 520,branco)
    imprimir_texto(linha22, linha1v, 20, 545,branco)
    imprimir_texto(linha23,linha1v,20,570,branco)
    imprimir_texto(linha24,linha1v,20,595,branco)
    imprimir_texto(linha25,linha1v,20,620,branco)
    imprimir_texto(linha26, linha1v, 20, 645,branco)
    imprimir_texto(linha27,linha1v,20,670,branco)
    imprimir_texto(linha28, linha1v, 20, 695,branco)

    a = False
    while a == False:
    	for event in pygame.event.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_SPACE:
    				a = True
    				proximafase= 8

def fase32():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg32.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'As ideias de Negreitos sempre são boas e divertidas. Ele é bom de disfarces. Caberá'
    linha1v = ''
    linha2 = 'a você inventar uma boa história convincente antes de bater na porta de Sarah.'
    linha3 = 'Se quiser apresenta-se como negociante de artefatos mágicos, aperte 1.'#cena7
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
    linha7 = '-Eu tenho uma ideia! podemos nos disfarçar e entrar no castelo para verificarmos o'
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
    imprimir_texto(linha10,linha1v,20,245,branco)
    imprimir_texto(linha11, linha1v, 20, 270,branco)

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
    linha3 = 'saco. Várias moedas, uma pérola valiosa e um pergaminho que detinha ordens reais '
    linha4 = 'para prisão do “O Aranha”. Capturado vivo ou morto. Negreitos fica com as moedas e'
    linha5 = 'você fica com a pérola.'
    linha6 = 'Negreitos:'
    linha7 = '-Imagina os problemas que ele vai ter ao chegar na cidade sem as ordens.'
    linha8 = 'Vocês gargalham e decidem seguir viagem.'#fase2
    linha9 = 'Aperte Espaço para continuar'

    imprimir_texto(linha1, linha1v, 20, 20,preto)
    imprimir_texto(linha2, linha1v, 20, 45,preto)
    imprimir_texto(linha3,linha1v, 20, 70,preto)
    imprimir_texto(linha4,linha1v, 20, 95,preto)
    imprimir_texto(linha5,linha1v,20, 120,preto)
    imprimir_texto(linha6,linha1v,20,145,vermelho)
    imprimir_texto(linha7,linha1v,20,170,vermelho)
    imprimir_texto(linha8,linha1v,20,195,preto)
    imprimir_texto(linha9,linha1v,20,240,preto)

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
    pygame.time.wait(200000)
    sys.exit()
def fase17():
    global tela, branco,proximafase
    bg0 = pygame.image.load("Imagens/bg17.jpg") 
    bg0 = pygame.transform.scale(bg0,(1080,700))
    tela.blit(bg0,(0,0))
    linha1 = 'Sua mão desliza silenciosamente na direção do cabo da adaga. No exato momento em que'
    linha1v = ''
    linha2 = 'iria pegá-la, um punho fecha-se veloz sobre seu pulso e aperta com a força de um gigante'
    linha3 = 'esmigalhando seus ossos.'
    linha4 = 'Cavaleiro:'
    linha5 = '-Ah larápio! Agora percebo! Sua descrição combina com a do maldito Aranha. Pagará por'
    linha6 = 'seus crimes, bandido!'
    linha7 = 'A lâmina desce com força e você sucumbe à explosão de dor. Só voltando a abrir os'
    linha8 = 'olhos novamente no outro dia, e descobre que está em um acampamento aquecido por uma'
    linha9 = 'fogueira. Negreitos está a seu lado entoando preces de cura.'
    linha10 = 'Atheris:'
    linha11 = '-O que aconteceu? - Você pergunta.'
    linha12 = 'Negreitos:'
    linha13 = '-Você abusou da sorte. E abusou dos deuses. foi o que aconteceu. Meu cajado esmagou o'
    linha14 = 'crânio do maldito guarda antes que o pior acontecesse. Mas creio que seus dias como'
    linha15 = 'o Aranha chegaram ao fim.'
    linha16 = 'Atheris:'
    linha17 = '-Do que você está falando?'
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
    linha7 = '-Desperdiçamos uma chance de agradar o meu Deus, isso desagradará Ele.'
    linha8 = 'Mas você prefere contrariar a fé de Negreitos do que enfrentar um guarda real e'
    linha9 = 'possivelmente um exército deles depois.'
    linha10= 'Aperte espaço para continuar'

    imprimir_texto(linha1, linha1v, 20, 20,preto)
    imprimir_texto(linha2, linha1v, 20, 45,preto)
    imprimir_texto(linha3,linha1v, 20, 70,preto)
    imprimir_texto(linha4,linha1v, 20, 95,preto)
    imprimir_texto(linha5,linha1v,20, 120,preto)
    imprimir_texto(linha6,linha1v,20,145,vermelho)
    imprimir_texto(linha7,linha1v,20,170,vermelho)
    imprimir_texto(linha8,linha1v,20,195,preto)
    imprimir_texto(linha9,linha1v,20,220,preto)
    imprimir_texto(linha10,linha1v,20,260,preto)

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
    linha3 = '-Que os deuses o abençoem, viajante. O que um oficial da guarda real faz por aqui tão'
    linha4 = ' distante do palácio?'
    linha5 = 'Cavaleiro:'
    linha6 = '-Salve, sacerdote. Estou à procura de um famigerado ladrão que invadiu a biblioteca'
    linha7 = 'central e roubou um tomo muito importante para o reino. Alguns o chamam de "o Aranha"'
    linha8 = '. Temos algumas poucas descrições dele, mas nenhuma com muitos detalhes.'
    linha9 = 'Enquanto conversam, Negreitos consegue roubar o saco de moedas dele e você vê '
    linha10 = 'em sua cintura o que parece ser uma bela adaga com várias pedras e gemas valiosas. '
    linha11 = 'parece ser mágica!'
    linha12 = 'Se quiser roubar a adaga, aperte 1.'#cena17
    linha13 = 'Se está satisfeito com o saco de moedas, aperte 2.'#cena18
    

    imprimir_texto(linha1, linha1v, 20, 20,preto)
    imprimir_texto(linha2, linha1v, 20, 45,vermelho)
    imprimir_texto(linha3,linha1v, 20, 70,vermelho)
    imprimir_texto(linha4,linha1v, 20, 95,vermelho)
    imprimir_texto(linha5,linha1v,20, 120,vermelho)
    imprimir_texto(linha6,linha1v,20,145,vermelho)
    imprimir_texto(linha7,linha1v,20,170,vermelho)
    imprimir_texto(linha8,linha1v,20,195,vermelho)
    imprimir_texto(linha9,linha1v,20,220,preto)
    imprimir_texto(linha10,linha1v,20,245,preto)
    imprimir_texto(linha11, linha1v, 20, 270,preto)
    imprimir_texto(linha12, linha1v, 250, 310,preto)
    imprimir_texto(linha13,linha1v, 250, 355,preto)

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
    linha3 = 'partidos, última parada antes da montanha, e algo surpreende vocês. Um cavaleiro de arma-'
    linha4 = 'dura sobre o lombo de um majestoso cavalo branco. Suas vestes são luxuosas e fazem'
    linha5 = 'com que você e Negreitos troquem olhares sorrateiros.'
    linha6 = 'Negreitos:'
    linha7 = '-Que tal fazermos uma oferenda ao Deus da trapaça?'
    linha8 = 'Propõe Negreitos assaltar esse cavaleiro. Pode ser perigoso, mas por outro lado, ele pode'
    linha9 = 'esta carregando alguns itens ou até jóias valiosas.'
    linha10 = 'Se você aceita o convite de Negreitos para um assalto, aperte 1.' #cena21
    linha11 = 'Se você prefere deixar o homem seguir em paz, aperte 2.' #cena4
    
    imprimir_texto(linha1, linha1v, 20, 20,preto)
    imprimir_texto(linha2, linha1v, 20, 45,preto)
    imprimir_texto(linha3,linha1v, 20, 70,preto)
    imprimir_texto(linha4,linha1v, 20, 95,preto)
    imprimir_texto(linha5,linha1v,20, 120,preto)
    imprimir_texto(linha6,linha1v,20,145,vermelho)
    imprimir_texto(linha7,linha1v,20,170,vermelho)
    imprimir_texto(linha8,linha1v,20,195,preto)
    imprimir_texto(linha9,linha1v,20,220,preto)
    imprimir_texto(linha10,linha1v,250,255,preto)
    imprimir_texto(linha11, linha1v, 250, 295,preto)

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
    
    linha1 = 'Ao sair da cidade, você e chega à conclusão que realmente não seria bom levar Negreitos'
    linha1v = ''
    linha2 = 'com você, e que ele poderia não estar de acordo com suas ambições. Depois de alguns'
    linha3 = 'minutos de viagem, você escuta uma susurro ao pé do ouvido.'
    linha4 = 'Negreitos:'
    linha5 = '-Partindo para uma aventura sem seu colega, Aranha?'
    linha6 = 'Você se assusta, e procura ao redor quem poderia ter dito aquilo. Ao não ver ninguém,'
    linha7 = 'volta seu olhar para o mico e vê um pequeno sorriso naquele rosto peludo.'
    linha8 = 'Atheris:'
    linha9 = '-Negreitos é você!?'
    linha10 = 'Você grita, o mico pula do seu ombro e como num passe de mágica, aquele corpo pequeno'
    linha11 = 'e peludo ganha feições e formas conhecidas. E nesse mesmo instante você lembra que'
    linha12 = 'os clérigos do Deus dos ladrões tinham esse poder. E vê Negreitos em roupa de sacer-'
    linha13 = 'dote dos deuses.'
    linha14 = 'Negreitos:'
    linha15 = '-Meio bem útil de seguir algumas pessoas não? Mas não se preocupe, estou aqui apenas'
    linha16 = 'para ajudar. E sim irei com você nem precisa insistir! Hahahahaha.'
    linha17 = 'Você se pergunta o que terá acontecido com o outro mico, ou se Negreitos esteve eu seu '
    linha18 = 'ombro esse tempo todo, e chega à conclusão que é melhor nem o questiona-lo.'
    linha19 = 'Aperte espaço para continuar'

   
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
    imprimir_texto(linha14,linha1v, 20, 345,vermelho)
    imprimir_texto(linha15,linha1v,20, 370,vermelho)
    imprimir_texto(linha16,linha1v,20,395,vermelho)
    imprimir_texto(linha17,linha1v,20,420,branco)
    imprimir_texto(linha18,linha1v,20,445,branco)
    imprimir_texto(linha19, linha1v, 250, 550,branco)

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
    linha1 = 'Você dirige-se até o templo escondido de Negreitos, onde ele convida os seguidores a '
    linha1v = ''
    linha2 = 'doarem os seus bens para a seita, ao chegar lá não encontra ninguém. E ao sair da '
    linha3 = 'sala você escuta uma voz baixa.'
    linha4 = 'Negreitos:'
    linha5 = '-Procurando por alguém Atheris?'
    linha6 = 'Você se assusta, e procura ao redor quem poderia ter dito aquilo. Ao não ver ninguém,'
    linha7 = ', você volta seu olhar para o mico e ver um pequeno sorriso naquele rosto peludo.'
    linha8 = 'Atheris:'
    linha9 = '-Negreitos é você!?'
    linha10 = 'Você grita, o mico pula do seu ombro e como num passe de mágica, aquele corpo pequeno'
    linha11 = 'e peludo se ganha feições e formas conhecidas. E nesse mesmo instante você lembra que'
    linha12 = 'os clérigos do deus dos ladrões tinham esse poder. E vê Negreitos em roupa de sacer-'
    linha13 = 'dote dos deuses.'
    linha14 = 'Depois de passado o susto você explica seu plano a ele e ele parece concordar.'
    linha15 = 'Negreitos:'
    linha16 = '-Não se preocupe amigo, com certeza os deuses vão abençoar nossa jornada. Mas seria'
    linha17 = 'ainda mais abençoada se um líder de Guilda fizesse oferendas ao deus da trapaça!'
    linha18 = 'Entendendo bem a mensagem, você garante que se o ajudar o deus da trapaça terá várias'
    linha19 = 'oferendas quando você for o novo líder. Você se pergunta o que terá acontecido com o'
    linha20 = 'outro mico, ou se Negreitos esteve eu seu ombro esse tempo todo, e chega à conclusão'
    linha21 = 'que é melhor nem o questiona-lo.'
    linha22 = 'Aperte espaço para continuar'

    


    imprimir_texto(linha1, linha1v, 20, 20,roxo)
    imprimir_texto(linha2, linha1v, 20, 45,roxo)
    imprimir_texto(linha3,linha1v, 20, 70,roxo)
    imprimir_texto(linha4,linha1v, 20, 95,branco)
    imprimir_texto(linha5,linha1v,20, 120,branco)
    imprimir_texto(linha6,linha1v,20,145,roxo)
    imprimir_texto(linha7,linha1v,20,170,roxo)
    imprimir_texto(linha8,linha1v,20,195,branco)
    imprimir_texto(linha9,linha1v,20,220,branco)
    imprimir_texto(linha10,linha1v,20,245,roxo)
    imprimir_texto(linha11, linha1v, 20, 270,roxo)
    imprimir_texto(linha12, linha1v, 20, 295,roxo)
    imprimir_texto(linha13,linha1v, 20, 320,roxo)
    imprimir_texto(linha14,linha1v, 20, 345,roxo)
    imprimir_texto(linha15,linha1v,20, 370,branco)
    imprimir_texto(linha16,linha1v,20,395,branco)
    imprimir_texto(linha17,linha1v,20,420,branco)
    imprimir_texto(linha18,linha1v,20,445,roxo)
    imprimir_texto(linha19, linha1v, 20, 470,roxo)
    imprimir_texto(linha20,linha1v,20,495,roxo)
    imprimir_texto(linha21, linha1v, 20, 525,roxo)
    imprimir_texto(linha22, linha1v, 250, 565,roxo)

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
    linha1 = 'Decidido a penetrar novamente o castelo da bruxa Sarah de Salem, você chega à conclusão'
    linha1v = ''
    linha2 = 'que precisará de 2 coisas: Um macaco treinado para furtos, que será fácil conseguir,'
    linha3 = 'e de seu antigo companheiro de furtos quase tão habilidoso quanto você. Negreitos,'
    linha4 = 'clérigo do Deus da trapaça e dos ladrões. Mas a dúvida se ele seria confiável se '
    linha5 = 'instaura em sua cabeça. Depois de conseguir o mico, só falta uma decisão a tomar.'
    linha6 = 'Se você deseja convidar Negreitos para participar do roubo, aperte 1.' #fase24
    linha7 = 'Se não confia no clérigo e prefere agir sozinho, aperte 2.' #fase37
    



    imprimir_texto(linha1, linha1v, 20, 20,lar)
    imprimir_texto(linha2, linha1v, 20, 45,lar)
    imprimir_texto(linha3,linha1v, 20, 70,lar)
    imprimir_texto(linha4,linha1v, 20, 95,lar)
    imprimir_texto(linha5,linha1v,20, 120,lar)
    imprimir_texto(linha6,linha1v,250,450,lar)
    imprimir_texto(linha7,linha1v,250,500,lar)

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
	linha2 = 'decidiu se estabelecer em uma metrópole calma para descançar, acabando por associar-se à'
	linha3 = 'Guilda de Ladrões local. Uma espécie de sindicato do crime que detém o monopólio das '
	linha4 = 'atividades criminosas  na cidade. Depois de algum tempo você decide que está na hora de'
	linha5 = 'de virar líder da guilda, e a melhor forma de conseguir isso seria conseguindo itens mági-'
	linha6 = 'cos poderosos. Lhe vem a cabeça que a alguns anos atrás você costumava andar com um gru-'
	linha7 = 'po de aventureiros, e que eles invadiram a fortaleza de uma feiticeira muito poderosa,'
	linha8 = 'conhecida como Sarah de Saalem, lá foi onde conseguiu o manto que o nomeou como '
	linha9 = 'Atheris, "o Aranha". E é la onde você conseguirá itens para se tornar o novo lider da guilda.'
	linha10 = 'Aperte Espaço'


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
        if keys[pygame.K_ESCAPE]:
            sys.exit()
	# if keys[pygame.K_F12]:
	# 	pygame.display.toggle_fullscreen()
	# 	pygame.display.toggle_fullscreen()
        pygame.display.update()



