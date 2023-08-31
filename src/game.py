from settings import *
from player import Player
import pygame
import os

class Game:
    def run():
        player_speed = 5
        player = Player(400, 300, player_speed)
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        bg = pygame.image.load(os.path.join("assets", "img", "bg", "game_layer.png")).convert()
        scaled_background = pygame.transform.smoothscale(bg, screen.get_size())
        pygame.display.update()
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move_left()
            if keys[pygame.K_RIGHT]:
                player.move_right()
            if keys[pygame.K_UP]:
                player.move_up()
            if keys[pygame.K_DOWN]:
                player.move_down()

            screen.blit(scaled_background, (0, 0))
            screen.blit(player.image, player.rect.topleft)  # Blit player's image at player's position
            clock.tick(30)
            pygame.display.update()