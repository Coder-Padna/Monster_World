import pygame
from menu import Pause

pygame.init()

# display info
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

# Load and scale the images to full screen
picture = pygame.transform.smoothscale(pygame.image.load("../assets/img/bg/bg_intro.png"),
                                       (screen_width, screen_height))
play_button = pygame.image.load("../assets/img/btn_play_fcs.png")
exit_button = pygame.image.load("../assets/img/btn_exit_fcs.png")

rect = picture.get_rect()

REDUCED_SIZE = (980, 520)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

clock = pygame.time.Clock()

paused = False
running = True
fullscreen = False
font = pygame.font.Font(None, 36)  # Font for the text

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fullscreen = not fullscreen

                if fullscreen:
                    picture = pygame.image.load("../assets/img/bg/bg_intro.png")
                    screen = pygame.display.set_mode(REDUCED_SIZE)
                    picture = pygame.transform.smoothscale(picture, REDUCED_SIZE)
                    paused = True
                else:
                    picture = pygame.image.load("../assets/img/bg/bg_intro.png")
                    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
                    picture = pygame.transform.smoothscale(picture, (screen_width, screen_height))
                    paused = False

        if not paused:
            pass

        else:
            Pause.pause_menu(screen)

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
