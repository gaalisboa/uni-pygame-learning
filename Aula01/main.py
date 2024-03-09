import pygame

WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324

# Inincializar o pygame
pygame.init()

window = pygame.display.set_mode(size=(WINDOW_WIDTH, 324))

bg_surface = pygame.image.load("./asset/bg_image.png").convert_alpha()
player1_surface = pygame.image.load("./asset/player_ship.png").convert_alpha()

bg_rect = bg_surface.get_rect(left=0, top=0)
player1_rect = player1_surface.get_rect(left=100, top=100)

pygame.mixer_music.load("./asset/fase1.mp3")
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.1)

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    window.blit(source=bg_surface, dest=bg_rect)
    window.blit(source=player1_surface, dest=player1_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1
