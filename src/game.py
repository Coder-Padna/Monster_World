from settings import *
from player import Player
import pygame, os, sys

from levels.level_1 import Map


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
        sprinting = False
        moving = False
        general_direction = "right"
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
                moving = True
                general_direction = "left"
                player.move_left(sprinting)
                if sprinting:
                    general_direction = "sprinting_sprites_left"
                else:
                    general_direction = "running_sprites_left"
            elif keys[pygame.K_RIGHT]:
                moving = True
                general_direction = "right"
                player.move_right(sprinting)
                if sprinting:
                    general_direction = "sprinting_sprites_right"
                else:
                    general_direction = "running_sprites_right"
            elif keys[pygame.K_UP]:
                player.move_up()
            elif keys[pygame.K_DOWN]:
                player.move_down()
            else:
                player.stand(general_direction)
                moving = False

            if moving:
                # player.update_animation(animation_direction)
                player.update_animation()
            screen.blit(scaled_background, (0, 0))
            screen.blit(player.image, player.rect.topleft)  # Blit player's image at player's position
            clock.tick(30)
            pygame.display.update()