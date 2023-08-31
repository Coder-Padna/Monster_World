import os
import pygame

class Player:
    def __init__(self, x, y, speed):
        self.image = pygame.image.load(os.path.join("assets", "img", "hero", "hero_stand_left.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def move_right(self):
        self.rect.x += self.speed
        self.image = pygame.image.load(os.path.join("assets", "img", "hero", "hero_speed_right_0.png")).convert_alpha()

    def move_left(self):
        self.rect.x -= self.speed
        self.image = pygame.image.load(os.path.join("assets", "img", "hero", "hero_run_left_1.png")).convert_alpha()

    def move_up(self):
        self.rect.y -= self.speed
        
    def move_down(self):
        self.rect.y += self.speed * 2

    def stand(self):
        self.image = pygame.image.load(os.path.join("assets", "img", "hero", "hero_stand_left.png")).convert_alpha()
        return self.image
    
    def dead(self):
        self.image = pygame.image.load(os.path.join("assets", "img", "hero", "hero_dead.png")).convert_alpha()
        return self.image



