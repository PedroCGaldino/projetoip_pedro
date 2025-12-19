import pygame
from pygame.locals import *
from sys import exit
import os

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

pygame.init()

largura = 1280
altura = 720

PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
pygame.display.set_caption("Caramelo: A Saga do Bolo de Rolo Dourado")

# plataforma (formato retangulo)

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((222, 184, 135))
        self.rect = self.image.get_rect(topleft=(x, y))

# coletáveis
class Bolo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        spritesheet = pygame.image.load(
            os.path.join(diretorio_principal, 'imagens', 'bolo_spritesheet.png')
        ).convert_alpha()

        #tamanho de cada bolo
        largura_bolo = spritesheet.get_width() // 5
        altura_bolo = spritesheet.get_height()

        # pegar apenas o primeiro bolo
        self.image = spritesheet.subsurface(
            pygame.Rect(0,0,largura_bolo, altura_bolo)
        )

        #redimensionar
        self.image = pygame.transform.scale(self.image, (70,70))

        #posição do bolo

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

class Juliete(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        spritesheet = pygame.image.load(
            os.path.join(diretorio_principal, 'imagens', 'juliet_spritesheet.png')
        ).convert_alpha()

        largura_juliete = spritesheet.get_width() // 5
        altura_juliete = spritesheet.get_height()

        self.image = spritesheet.subsurface(
            pygame.Rect(0,0,largura_juliete, altura_juliete)
        )

        self.image = pygame.transform.scale(self.image, (70,70))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

class Osso(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        spritesheet = pygame.image.load(
            os.path.join(diretorio_principal, 'imagens', 'osso_spritesheet.png')
        ).convert_alpha()

        largura_osso = spritesheet.get_width() // 6
        altura_osso = spritesheet.get_height()

        self.image = spritesheet.subsurface(
            pygame.Rect(0,0,largura_osso, altura_osso)
        )

        self.image = pygame.transform.scale(self.image, (70,70))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

class Caramelo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # --- 1. CARREGAMENTO SPRITES NORMAIS ---
        self.latido_normal = []
        sheet_lj = pygame.image.load(os.path.join(diretorio_principal, 'sprites', 'caramelo_latindo.png')).convert_alpha()
        fw_lj = sheet_lj.get_width() // 4
        for i in range(4):
            self.latido_normal.append(pygame.transform.scale(sheet_lj.subsurface(pygame.Rect(i*fw_lj, 0, fw_lj, sheet_lj.get_height())), (120, 120)))        
        
        # Andar Normal
        self.andando_normal = []
        sheet_n = pygame.image.load(os.path.join(diretorio_principal, 'sprites', 'caramelo_andando.png')).convert_alpha()
        fw_n = sheet_n.get_width() // 3
        for i in range(3):
            self.andando_normal.append(pygame.transform.scale(sheet_n.subsurface(pygame.Rect(i*fw_n, 0, fw_n, sheet_n.get_height())), (120, 120)))

        # Pulo Normal
        self.pulando_normal = []
        sheet_p = pygame.image.load(os.path.join(diretorio_principal, 'sprites', 'caramelo_pulando.png')).convert_alpha()
        fw_p = sheet_p.get_width() // 8
        for i in range(7):
            self.pulando_normal.append(pygame.transform.scale(sheet_p.subsurface(pygame.Rect(i*fw_p, 0, fw_p, sheet_p.get_height())), (120, 120)))

        # --- 2. CARREGAMENTO SPRITES JULIETE (COM ÓCULOS) ---
        # Andar Juliete (4 frames)
        self.andando_juliete = []
        sheet_j = pygame.image.load(os.path.join(diretorio_principal, 'sprites', 'cachorro_andando_juliete.png')).convert_alpha()
        fw_j = sheet_j.get_width() // 4
        for i in range(4):
            self.andando_juliete.append(pygame.transform.scale(sheet_j.subsurface(pygame.Rect(i*fw_j, 0, fw_j, sheet_j.get_height())), (120, 120)))

        # Latido Juliete (arquivos: sprite_latido0_j.png, etc)
        self.latido_juliete = []
        sheet_lj = pygame.image.load(os.path.join(diretorio_principal, 'sprites', 'cachorro_latindo_juliete.png')).convert_alpha()
        fw_lj = sheet_lj.get_width() // 4
        for i in range(4):
            self.latido_juliete.append(pygame.transform.scale(sheet_lj.subsurface(pygame.Rect(i*fw_lj, 0, fw_lj, sheet_lj.get_height())), (120, 120)))

        # Pulo Juliete (arquivo: pulando_juliete.png)
        self.pulando_juliete = []
        sheet_pj = pygame.image.load(os.path.join(diretorio_principal, 'sprites', 'cachorro_pulando_juliete.png')).convert_alpha()
        fw_pj = sheet_pj.get_width() // 4
        for i in range(4):
            self.pulando_juliete.append(pygame.transform.scale(sheet_pj.subsurface(pygame.Rect(i*fw_pj, 0, fw_pj, sheet_pj.get_height())), (120, 120)))

        # --- 3. CONFIGURAÇÃO DE ESTADO ---
        self.tem_juliete = False
        self.sprites = self.latido_normal 
        self.andando_sprites = self.andando_normal
        self.pulando_sprites = self.pulando_normal
        
        self.atual = 0
        self.image = self.sprites[0]
        self.rect = self.image.get_rect(topleft=(100, 785))
        
        self.animar_latir = False
        self.andando = False
        self.pulando = False
        self.direcao = 0
        self.velocidade = 5
        self.facing = 1
        self.velocity_y = 0
        self.gravity = 0.6
        self.jump_strength = 14
        self.on_ground = False

    def usar_juliete(self):
        """Troca todas as listas de animação para a versão com óculos"""
        self.tem_juliete = True
        self.sprites = self.latido_juliete
        self.andando_sprites = self.andando_juliete
        self.pulando_sprites = self.pulando_juliete

    def latir(self):
        self.animar_latir = True
        self.atual = 0 # Reinicia animação ao latir

    def andar(self, dir):
        self.andando = True
        self.direcao = dir
        self.facing = dir

    def pular(self):
        if self.on_ground:
            self.velocity_y = -self.jump_strength
            self.on_ground = False
            self.pulando = True
            self.atual = 0

    def parar(self):
        self.andando = False

    def update(self, plataformas):
        old_bottom = self.rect.bottom

        # Seleção de Frame
        if self.animar_latir:
            self.atual += 0.15
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar_latir = False
            img = self.sprites[int(self.atual)]
        elif self.pulando:
            self.atual += 0.1
            if self.atual >= len(self.pulando_sprites):
                self.atual = len(self.pulando_sprites) - 1
            img = self.pulando_sprites[int(self.atual)]
        elif self.andando:
            self.atual += 0.1
            if self.atual >= len(self.andando_sprites):
                self.atual = 0
            img = self.andando_sprites[int(self.atual)]
        else:
            img = self.sprites[0] # Frame parado

        # Espelhamento
        if self.facing < 0:
            img = pygame.transform.flip(img, True, False)
        
        self.image = img

        # Movimentação e Física
        if self.andando:
            self.rect.x += self.direcao * self.velocidade

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Colisão com Chão/Plataformas
        if self.velocity_y > 0:
            colisoes = pygame.sprite.spritecollide(self, plataformas, False)
            for plat in colisoes:
                if old_bottom <= plat.rect.top:
                    self.rect.bottom = plat.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                    self.pulando = False


# Plataformas, Sprites e Coletavel--------------
todas_as_sprites = pygame.sprite.Group()
caramelo = Caramelo()
caramelo.rect.x = 100
caramelo.rect.y = altura - 120
todas_as_sprites.add(caramelo)

plataformas = pygame.sprite.Group()
coletavel_bolo = pygame.sprite.Group()  
coletavel_juliete = pygame.sprite.Group()
coletavel_osso = pygame.sprite.Group()


plataformas.add(Plataforma(0, altura, largura, 60))

# --- PLATAFORMAS ---
# Em vez de posições fixas, vamos usar a 'altura' como base e subtrair valores.
# Assim, elas sempre subirão a partir do chão, não importa o tamanho da tela.

distancia_entre_plataformas = 100 # Espaço vertical entre elas

plataformas.add(Plataforma(650, altura - 130, 150, 30))  # Primeira (acima do chão)
plataformas.add(Plataforma(350, altura - 230, 150, 30))  # Segunda
plataformas.add(Plataforma(650, altura - 330, 150, 30))  # Terceira
plataformas.add(Plataforma(420, altura - 430, 150, 30))  # Quarta
plataformas.add(Plataforma(725, altura - 530, 150, 30))  # Quinta
plataformas.add(Plataforma(125, altura - 530, 150, 30))  # Sexta (mesmo nível da anterior)

#imagem de fundo principal

imagem_fundo_original = pygame.image.load(os.path.join(
    diretorio_principal, 'sprites', 'background.jpg')).convert()
imagem_fundo = pygame.transform.scale(imagem_fundo_original, (largura, altura))

#coletavel

# Supondo largura = 1280 e altura = 720

# Bolo (perto de uma plataforma alta)
bolo = Bolo(1200, altura - 670) 
coletavel_bolo.add(bolo)

# Juliete (perto do início)
juliet = Juliete(150, altura - 600)
juliet2 = Juliete(1200, altura - 150)
coletavel_juliete.add(juliet, juliet2)

# Ossos espalhados
# Usamos (altura - valor) para que, se você aumentar a tela, 
# eles subam junto com as plataformas.
osso1 = Osso(800, altura - 600)
osso2 = Osso(470, altura - 500)
osso3 = Osso(700, altura - 400)
osso4 = Osso(400, altura - 300)
osso5 = Osso(200, altura - 200)
osso6 = Osso(700, altura - 200)

coletavel_osso.add(osso1, osso2, osso3, osso4, osso5, osso6)

pontuacao_osso = 0
pontuacao_juliete = 0
pontuacao_bolos = 0


fonte_pontos = pygame.font.SysFont(None, 48)


def carregar_slides():
    # IMPORTANTE: Use os nomes reais dos seus arquivos
    nomes_hist = [os.path.join(diretorio_principal, 'imagens', 'historia1.jpeg'),
                os.path.join(diretorio_principal, 'imagens', 'historia2.jpeg'),
                os.path.join(diretorio_principal, 'imagens', 'historia3.jpeg'), 
                os.path.join(diretorio_principal, 'imagens', 'historia4.jpeg'), 
                os.path.join(diretorio_principal, 'imagens', 'historia5.jpeg')]
    slides_carregados = []
    
    for nome in nomes_hist:
        try:
            imagem = pygame.image.load(nome).convert()
            imagem_escala = pygame.transform.scale(imagem, (largura, altura))
            slides_carregados.append(imagem_escala)
        except pygame.error as e:
            print(f"Erro ao carregar a imagem {nome}. Usando placeholder: {e}")
            # Placeholder em caso de erro para não travar o jogo
            placeholder = pygame.Surface((largura, altura))
            placeholder.fill((255, 0, 0))
            slides_carregados.append(placeholder)

    return slides_carregados

SLIDES = carregar_slides()
NUM_SLIDES = len(SLIDES)

# --- Menu inicial ---

def _draw_button(surface, rect, text, font, hover=False):
    color = (200, 160, 60) if not hover else (255, 200, 70)
    pygame.draw.rect(surface, color, rect, border_radius=8)
    txt = font.render(text, True, (10, 10, 10))
    txt_rect = txt.get_rect(center=rect.center)
    surface.blit(txt, txt_rect)


menu_img = None
mrect = None
# try possible locations for menu image
possible_menu_paths = [
    os.path.join(diretorio_principal, 'assets', 'menu.jpeg'),
    os.path.join(diretorio_principal, 'sprites', 'menu.jpeg'),
    os.path.join(diretorio_principal, 'sprites', 'menu.jpg'),
]
for menu_path in possible_menu_paths:

    if os.path.exists(menu_path):
        try:
            menu_img = pygame.image.load(menu_path).convert()
            mw, mh = menu_img.get_size()
            scale = max(largura / mw, altura / mh)
            new_w, new_h = int(mw * scale), int(mh * scale)
            if (new_w, new_h) != (mw, mh):
                menu_img = pygame.transform.smoothscale(
                    menu_img, (new_w, new_h))
            mrect = menu_img.get_rect()
            mrect.center = (largura // 2, altura // 2)
            break
        except Exception:
            menu_img = None
            mrect = None

font_title = pygame.font.SysFont(None, 72)
font_btn = pygame.font.SysFont(None, 48)
btn_w, btn_h = 220, 64
start_rect = pygame.Rect((0, 0), (btn_w, btn_h))
exit_rect = pygame.Rect((0, 0), (btn_w, btn_h))

menu_clock = pygame.time.Clock()
in_menu = True
while in_menu:
    
    mx, my = pygame.mouse.get_pos()
    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                in_menu = False
                break
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    tela.fill((20, 20, 30))
    if menu_img and mrect:
        tela.blit(menu_img, mrect)
        y_pos = mrect.centery + int(mrect.height * 0.25)
        spacing = 140
        start_rect.center = (largura // 2 - spacing, y_pos)
        exit_rect.center = (largura // 2 + spacing, y_pos)

    hover_start = start_rect.collidepoint((mx, my))
    hover_exit = exit_rect.collidepoint((mx, my))
    _draw_button(tela, start_rect, 'Start', font_btn, hover_start)
    _draw_button(tela, exit_rect, 'Exit', font_btn, hover_exit)

    if hover_start and click:
        in_menu = False
        break
    if hover_exit and click:
        pygame.quit()
        exit()

    pygame.display.flip()
    menu_clock.tick(60)

slide_atual_indice = 0
tempo_ultima_troca = pygame.time.get_ticks() 
historia_rodando = True

# Entra no loop da história SÓ SE o menu terminou por 'Start' ou 'Enter'
# Se o menu terminou por 'Exit', o programa já terá saído.
if not in_menu:
    
    while historia_rodando:
        
        # 1. Eventos (Apenas QUIT é permitido)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_SPACE:
                # Pula para o próximo slide imediatamente
                slide_atual_indice += 1
                if slide_atual_indice >= NUM_SLIDES:
                    historia_rodando = False
                else:
                    tempo_ultima_troca = pygame.time.get_ticks()
        
        # 2. Atualização Lógica (Controle de Tempo)
        tempo_agora = pygame.time.get_ticks()
        
        TEMPO_POR_SLIDE = 10000  # 10 segundos por slide
        if tempo_agora - tempo_ultima_troca >= TEMPO_POR_SLIDE:
            
            slide_atual_indice += 1
            tempo_ultima_troca = tempo_agora
            
            # Fim da história
            if slide_atual_indice >= NUM_SLIDES:
                historia_rodando = False
                
                
        # 3. Desenho
        tela.fill((0, 0, 0)) # Fundo preto
        # Desenha o slide atual
        if slide_atual_indice < NUM_SLIDES:
             tela.blit(SLIDES[slide_atual_indice], (0, 0))
             
        pygame.display.flip()
        menu_clock.tick(60)

relogio = pygame.time.Clock()

while True:  # Loop principal
    relogio.tick(60)  # Controla a taxa de frames
    tela.fill(PRETO)

    for event in pygame.event.get():  # Loop de eventos
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            caramelo.latir()
            pygame.mixer.music.load(os.path.join(diretorio_principal, 'audio', 'latidocaramelo.mp3'))
            pygame.mixer.music.play(1)
        if event.type == KEYDOWN and event.key == K_w:
            caramelo.pular()

    keys = pygame.key.get_pressed()
    if keys[K_a]:
        caramelo.andar(-1)
    elif keys[K_d]:
        caramelo.andar(1)
    else:
        caramelo.parar()

    # desenhos
    tela.blit(imagem_fundo, (0, 0))  # Desenha o fundo
    plataformas.draw(tela)           # Desenha as plataformas
    coletavel_bolo.draw(tela)           # Desenha os coletaveis
    coletavel_osso.draw(tela)
    coletavel_juliete.draw(tela)
    todas_as_sprites.draw(tela)      # Desenha todas as sprites
    
    #desenhar pontuação dos coletaveis

    texto_pontos_bolos = fonte_pontos.render(
        f"Bolos : {pontuacao_bolos}", True, (255, 255, 255)
    )
    tela.blit(texto_pontos_bolos,(20,20))

    texto_pontos_ossos = fonte_pontos.render(
        f"Ossos : {pontuacao_osso}", True, (255, 255, 255)
    )
    tela.blit(texto_pontos_ossos,(20,60))

    texto_pontos_juliete = fonte_pontos.render(
        f"Juliete : {pontuacao_juliete}", True, (255, 255, 255)
    )
    tela.blit(texto_pontos_juliete,(20,100))

    # MUDANÇAS(UPDATE)
    todas_as_sprites.update(plataformas)  # Atualiza todas as sprites

    #COLETA DE BOLOS (#uso de função para colidir)
    bolos_coletados = pygame.sprite.spritecollide(
        caramelo,       # jogador
        coletavel_bolo,     #grupo de coletaveis
        True            #True = remove o bolo ao coletar
    )  

    ossos_coletados = pygame.sprite.spritecollide(
        caramelo,
        coletavel_osso,
        True
    )

    juliete_coletados = pygame.sprite.spritecollide(
        caramelo,   
        coletavel_juliete,
        True
    )

    # 1. Itens comuns: Apenas somam na pontuação geral
    if ossos_coletados:
        pontuacao_osso += len(ossos_coletados)
        pygame.mixer.music.load(os.path.join(diretorio_principal, 'audio', 'pegando_osso.mp3'))
        pygame.mixer.music.play(1)

    if juliete_coletados:
        pontuacao_juliete += len(juliete_coletados)
        caramelo.usar_juliete() # Chama a função que troca todos os sprites
        pygame.mixer.music.load(os.path.join(diretorio_principal, 'audio', 'musica_fundo.mp3'))
        pygame.mixer.music.play(-1)

    # 2. O BOLO: Soma na pontuação E ativa a tela de vitória
    if bolos_coletados:
        pontuacao_bolos += len(bolos_coletados)
        
        if pontuacao_bolos >= 1 and pontuacao_juliete >= 2:
            # Aciona a vitória imediatamente ao coletar o bolo
            vitoria = os.path.join(diretorio_principal, 'imagens', 'vitoria.jpeg')
            imagem_vitoria = pygame.image.load(vitoria).convert()
            imagem_vitoria = pygame.transform.scale(imagem_vitoria, (largura, altura))
            pygame.mixer.music.load(os.path.join(diretorio_principal, 'audio', 'somvitoria.mp3'))
            pygame.mixer.music.play(1)

            vitoria_ativa = True
            while vitoria_ativa:
                mx, my = pygame.mouse.get_pos()
                click = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        click = True
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_ESCAPE, pygame.K_RETURN):
                            pygame.quit()
                            exit()

                # Desenha o fundo e o botão
                tela.blit(imagem_vitoria, (0, 0))
                
                hover_exit = exit_rect.collidepoint((mx, my))
                _draw_button(tela, exit_rect, 'Sair', font_btn, hover_exit)
                

                if hover_exit and click:
                    pygame.quit()
                    exit()

                pygame.display.update()

        else: 
            derrota = os.path.join(diretorio_principal, 'imagens', 'derrota.jpeg')
            imagem_derrota = pygame.image.load(derrota).convert()
            imagem_derrota = pygame.transform.scale(imagem_derrota, (largura, altura))
            pygame.mixer.music.load(os.path.join(diretorio_principal, 'audio', 'somderrota.mp3'))
            pygame.mixer.music.play(1)

            derrota_ativa = True
            while derrota_ativa:
                mx, my = pygame.mouse.get_pos()
                click = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        click = True
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_ESCAPE, pygame.K_RETURN):
                            pygame.quit()
                            exit()

                # Desenha o fundo e o botão
                tela.blit(imagem_derrota, (0, 0))
                
                hover_exit = exit_rect.collidepoint((mx, my))
                _draw_button(tela, exit_rect, 'Sair', font_btn, hover_exit)
                

                if hover_exit and click:
                    pygame.quit()
                    exit()

                pygame.display.update()

        #MUDANÇA(DISPLAY)
    pygame.display.flip()                 # Atualiza o display
