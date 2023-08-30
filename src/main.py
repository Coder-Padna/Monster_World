import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Full-Screen Window")

# Load background image
bg_path = os.path.join("assets", "img", "bg", "bg_intro.png")
background = pygame.image.load(bg_path).convert()

# Load play button images
play_button_path = os.path.join("assets", "img", "btn_play.png")
play_button = pygame.image.load(play_button_path).convert_alpha()
play_button_focused_path = os.path.join("assets", "img", "btn_play_fcs.png")
play_button_focused = pygame.image.load(play_button_focused_path).convert_alpha()
play_button_rect = play_button.get_rect(topleft=(400, screen.get_height() - play_button.get_height() - 80))

# Load exit button images
exit_button_path = os.path.join("assets", "img", "btn_exit.png")
exit_button = pygame.image.load(exit_button_path).convert_alpha()
exit_button_focused_path = os.path.join("assets", "img", "btn_exit_fcs.png")
exit_button_focused = pygame.image.load(exit_button_focused_path).convert_alpha()
exit_button_rect = exit_button.get_rect(bottomright=(screen.get_width() - 400, screen.get_height() - 80))

hovered_play_button = False
hovered_exit_button = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                show_exit_button = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_rect.collidepoint(event.pos):
                running = False

        elif event.type == pygame.MOUSEMOTION:
            if play_button_rect.collidepoint(event.pos):
                hovered_play_button = True
            else:
                hovered_play_button = False

            if exit_button_rect.collidepoint(event.pos):
                hovered_exit_button = True
            else:
                hovered_exit_button = False

    # Smoothly scale the background image to match the window size
    scaled_background = pygame.transform.smoothscale(background, screen.get_size())

    # Blit the scaled background image onto the screen
    screen.blit(scaled_background, (0, 0))

    # Draw play button if not showing exit button
    
    if hovered_play_button:
        screen.blit(play_button_focused, play_button_rect)
    else:
        screen.blit(play_button, play_button_rect)
    if hovered_exit_button:
        screen.blit(exit_button_focused, exit_button_rect)
    else:
        screen.blit(exit_button, exit_button_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
