import os
import pygame

class Player(pygame.sprite.Sprite):



    def __init__(self, x, y, speed):
        self.image = pygame.image.load(os.path.join("assets", "img", "hero", "hero_stand_left.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.x_vel = 0
        self.y_vel = 0
        self.direction = "right"
        self.animation_count = 0
        self.animation_type = None

        # Animation variables
        self.frame_index = 0
        self.frame_duration = 150  # Time (in milliseconds) per frame
        self.last_frame_change = pygame.time.get_ticks()

        self.animation_frames = {

        "sprinting_sprites_right" : [
                            pygame.image.load(os.path.join("assets", "img", "hero", "hero_speed_right_0.png")).convert_alpha(),
                            pygame.image.load(os.path.join("assets", "img", "hero", "hero_speed_right_1.png")).convert_alpha(),
                            pygame.image.load(os.path.join("assets", "img", "hero", "hero_speed_right_2.png")).convert_alpha()
                            ],
        
        "sprinting_sprites_left" : [
                            pygame.image.load(os.path.join("assets", "img", "hero", "hero_speed_left_0.png")).convert_alpha(),
                            pygame.image.load(os.path.join("assets", "img", "hero", "hero_speed_left_1.png")).convert_alpha(),
                            pygame.image.load(os.path.join("assets", "img", "hero", "hero_speed_left_2.png")).convert_alpha()
                            ],

        "running_sprites_right" : [
                            pygame.image.load(os.path.join("assets", "img", "hero", "hero_run_right_1.png")).convert_alpha(),
                            pygame.image.load(os.path.join("assets", "img", "hero", "hero_run_right_2.png")).convert_alpha()],
        
        "running_sprites_left" : [
                            pygame.image.load(os.path.join("assets", "img", "hero", "hero_run_left_1.png")).convert_alpha(),
                            pygame.image.load(os.path.join("assets", "img", "hero", "hero_run_left_2.png")).convert_alpha()],
        
        "stand_right" : pygame.image.load(os.path.join("assets", "img", "hero", "hero_stand_right.png")).convert_alpha(),
        "stand_left" : pygame.image.load(os.path.join("assets", "img", "hero", "hero_stand_left.png")).convert_alpha()
        }

    def set_animation(self, animation_type):
        # Set the current animation based on the animation type
        self.current_animation = self.animation_frames.get(animation_type, None)
        
    def update_animation(self):
        if self.current_animation:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_frame_change >= self.frame_duration:
                self.frame_index = (self.frame_index + 1) % len(self.current_animation)
                self.last_frame_change = current_time
                self.image = self.current_animation[self.frame_index]

    def move_right(self, sprinting):
        self.rect.x += self.speed
        if sprinting:
            self.set_animation("sprinting_sprites_right")
        else :
            self.set_animation("running_sprites_right")

    def move_left(self, sprinting):
        self.rect.x -= self.speed
        if sprinting:
            self.set_animation("sprinting_sprites_left")
        else :
            self.set_animation("running_sprites_left")

    def move_up(self):
        self.rect.y -= self.speed
        
    def move_down(self):
        self.rect.y += self.speed * 2

    def stand(self, direction):
        if direction == "right":
            self.set_animation("stand_right")
        elif direction == "left":
            self.set_animation("stand_left")
        
    def dead(self):
        self.image = pygame.image.load(os.path.join("assets", "img", "hero", "hero_dead.png")).convert_alpha()



