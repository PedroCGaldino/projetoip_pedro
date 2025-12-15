import pygame
from pygame.locals import *
from sys import exit
import os

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

pygame.init()

largura = 1280
altura = 960

PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Caramelo: A Saga do Bolo de Rolo Dourado")

# Fullscreen toggle state
is_fullscreen = False
windowed_size = (largura, altura)

# plataforma (formato retangulo)

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((120, 120, 120))
        self.rect = self.image.get_rect(topleft=(x, y))


class Caramelo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.sprites.append(pygame.image.load(os.path.join(
            diretorio_principal, 'sprites', 'sprite_latido0.png')))
        self.sprites.append(pygame.image.load(os.path.join(
            diretorio_principal, 'sprites', 'sprite_latido1.png')))
        self.sprites.append(pygame.image.load(os.path.join(
            diretorio_principal, 'sprites', 'sprite_latido2.png')))
        self.sprites.append(pygame.image.load(os.path.join(
            diretorio_principal, 'sprites', 'sprite_latido3.png')))
        self.sprites.append(pygame.image.load(os.path.join(
            diretorio_principal, 'sprites', 'sprite_latido4.png')))

        self.andando_sprites = []
        spritesheet_andando = pygame.image.load(os.path.join(
            diretorio_principal, 'sprites', 'caramelo_andando.png'))
        frame_width = spritesheet_andando.get_width() // 3
        frame_height = spritesheet_andando.get_height()

        for i in range(3):
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            self.andando_sprites.append(spritesheet_andando.subsurface(rect))

        self.pulando_sprites = []
        spritesheet_pulando = pygame.image.load(os.path.join(
            diretorio_principal, 'sprites', 'caramelo_pulando.png'))
        frame_width_p = spritesheet_pulando.get_width() // 8
        frame_height_p = spritesheet_pulando.get_height()

        for i in range(7):
            rect = pygame.Rect(i * frame_width_p, 0,
                               frame_width_p, frame_height_p)
            self.pulando_sprites.append(spritesheet_pulando.subsurface(rect))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (120, 120))

        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 785)

        self.animar_latir = False  # Controla a animação de latido
        self.andando = False       # Controla a animação de andar
        self.pulando = False       # Controla a animação de pulo
        self.direcao = 0           # Direção do movimento
        self.velocidade = 5
        self.facing = 1            # 1 para direita, -1 para esquerda
        self.velocity_y = 0
        self.gravity = 0.6
        self.jump_strength = 14
        self.on_ground = False
        # antigo chão: self.ground_level = 785 + 120

    def latir(self):
        self.animar_latir = True

    def andar(self, direcao):
        self.andando = True
        self.direcao = direcao
        self.facing = direcao

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

        if self.animar_latir == True:  # Animação de latido
            self.atual = self.atual + 0.1  # Velocidade do latido
            if self.atual >= len(self.sprites):  # Se a animação terminou
                self.atual = 0  # Reseta o frame atual
                self.animar_latir = False
            self.image = self.sprites[int(self.atual)]  # Atualiza a imagem
            if self.facing < 0:
                self.image = pygame.transform.flip(
                    self.image, True, False)  # Flip horizontal
            self.image = pygame.transform.scale(
                self.image, (120, 120))  # Escala a imagem

        elif self.pulando:  # Animação de pulo
            self.atual = self.atual + 0.1  # Velocidade do pulo
            if self.atual >= len(self.pulando_sprites):  # Se a animação terminou
                self.atual = len(self.pulando_sprites) - \
                    1  # Fica no último frame
            # Pega a imagem do pulo
            img = self.pulando_sprites[int(self.atual)]
            if self.facing < 0:  # Se estiver virado para a esquerda
                img = pygame.transform.flip(
                    img, True, False)  # Flip horizontal
            self.image = pygame.transform.scale(
                img, (120, 120))  # Escala a imagem

        elif self.andando:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.andando_sprites):
                self.atual = 0
            img = self.andando_sprites[int(self.atual)]
            if self.direcao < 0:
                img = pygame.transform.flip(img, True, False)
            self.image = pygame.transform.scale(
                img, (120, 120))  # Escala a imagem
            # andando inicialmente (sem puder pular e andar) self.rect.x += self.direcao * self.velocidade

        else:
            img = self.sprites[0]
            if self.facing < 0:
                img = pygame.transform.flip(img, True, False)
            self.image = pygame.transform.scale(img, (120, 120))

        # Se mover independente do que acontece
        if self.andando:
            self.rect.x += self.direcao * self.velocidade

        # Física do pulo
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        self.on_ground = False  # assume que está no ar até encostar em algo

        # colisoes com plataformas(o chão virou plataforma)
        # (antigo codigo do chão)
        # if self.rect.bottom >= self.ground_level:
        #     self.rect.bottom = self.ground_level
        #     self.velocity_y = 0
        #     self.on_ground = True
        #     self.pulando = False

        if self.velocity_y > 0:  # só checa cão quando está descendo
            colisoes = pygame.sprite.spritecollide(self, plataformas, False)
            for plat in colisoes:
                # caindo encontou em cima
                if self.velocity_y > 0 and old_bottom <= plat.rect.top:
                    self.rect.bottom = plat.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                    self.pulando = False
                elif self.velocity_y < 0 and self.rect.top <= plat.rect.bottom:
                    self.rect.top = plat.rect.bottom
                    self.velocity_y = 0


# Plataformas e Sprites--------------
todas_as_sprites = pygame.sprite.Group()
caramelo = Caramelo()
todas_as_sprites.add(caramelo)

plataformas = pygame.sprite.Group()

# chão
plataformas.add(Plataforma(0, 905, 1280, 60))

# plataformas
plataformas.add(Plataforma(650, 760, 150, 30))
plataformas.add(Plataforma(350, 660, 150, 30))
plataformas.add(Plataforma(650, 560, 150, 30))
plataformas.add(Plataforma(420, 460, 150, 30))
plataformas.add(Plataforma(725, 360, 150, 30))
plataformas.add(Plataforma(125, 360, 150, 30))

imagem_fundo_original = pygame.image.load(os.path.join(
    diretorio_principal, 'sprites', 'background.jpg')).convert()
imagem_fundo = pygame.transform.scale(imagem_fundo_original, (largura, altura))

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
    else:
        title_surf = font_title.render('CARAMELO', True, (255, 200, 60))
        trect = title_surf.get_rect(center=(largura // 2, altura // 4))
        tela.blit(title_surf, trect)
        y_pos = int(altura * 0.65)
        start_rect.center = (largura // 2 - btn_w - 20, y_pos)
        exit_rect.center = (largura // 2 + btn_w + 20, y_pos)

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
        if event.type == KEYDOWN and event.key == K_w:
            caramelo.pular()
        # Toggle fullscreen with F11 or F
        if event.type == KEYDOWN and (event.key == K_F11 or event.key == K_f):
            is_fullscreen = not is_fullscreen
            if is_fullscreen:
                info = pygame.display.Info()
                largura, altura = info.current_w, info.current_h
                tela = pygame.display.set_mode(
                    (largura, altura), pygame.FULLSCREEN)
            else:
                largura, altura = windowed_size
                tela = pygame.display.set_mode(windowed_size)
            imagem_fundo = pygame.transform.scale(
                imagem_fundo_original, (largura, altura))

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
    todas_as_sprites.draw(tela)      # Desenha todas as sprites

    # mudanças
    todas_as_sprites.update(plataformas)  # Atualiza todas as sprites
    pygame.display.flip()                 # Atualiza o display
