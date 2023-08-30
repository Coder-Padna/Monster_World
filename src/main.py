import pygame
import os
from menu import Pause

pygame.init()

# display info
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

# Load and scale the images to full screen
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the image
image_path = os.path.join(script_dir, "../assets/img/bg/bg_intro.png")

picture = pygame.transform.smoothscale(pygame.image.load(image_path), (screen_width, screen_height))

play_button_path = os.path.join(script_dir, "../assets/img/btn_play_fcs.png")
exit_button_path = os.path.join(script_dir, "../assets/img/btn_exit_fcs.png")


play_button = pygame.image.load(play_button_path)
exit_button = pygame.image.load(exit_button_path)

rect = picture.get_rect()

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

clock = pygame.time.Clock()

paused = False
running = True
fullscreen = True
font = pygame.font.Font(None, 36)  # Font for the text

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print("p is pressed")
                paused = True

    if not paused:
        pass

    else:
        Pause.display_pause_menu(screen)

    # testing
    text = font.render(str(display_info.current_h), True, "black")

    # Blit the text onto the screen
    text_rect = text.get_rect()
    text_rect.center = (screen_width // 2, 20)

    # screen.fill("purple")  # Fill screen with purple
    rect = rect.move((0, 0))
    screen.blit(picture, rect)
    screen.blit(play_button, (389, 640))
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
