import pygame
import os

class Pause:
    @staticmethod
    def display_pause_menu(screen):
        font = pygame.font.Font(None, 36)
        menu_text = font.render("Paused", True, (255, 255, 255))
        continue_text = font.render("Continue", True, (0, 0, 0))
        quit_text = font.render("Quit", True, (0, 0, 0))

        screen_width = screen.get_width()
        screen_height = screen.get_height()

        menu_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 150)
        continue_button_rect = pygame.Rect(screen_width // 2 - 75, screen_height // 2 - 10, 150, 40)
        quit_button_rect = pygame.Rect(screen_width // 2 - 75, screen_height // 2 + 40, 150, 40)
        screen_overlay = pygame.Rect(screen_width, screen_height, 0, 0)

        # Define colors
        color = pygame.Color(0, 0, 0)  # Original color (black)
        shade_factor = 0.5  # Adjust this to control the shade intensity
        alpha_value = int(255 * shade_factor)  # Convert the factor to an alpha value

        # Create a translucent overlay with the adjusted shade
        overlay_color = color
        overlay_color.a = alpha_value
        screen_overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

        pygame.draw.rect(screen_overlay, overlay_color, screen.get_rect())

        pygame.draw.rect(screen, (0, 0, 0), menu_rect)
        pygame.draw.rect(screen, (255, 255, 255), continue_button_rect)
        pygame.draw.rect(screen, (255, 255, 255), quit_button_rect)

        # screen.blit(screen_overlay, (0, 0))
        screen.blit(menu_text, (screen_width // 2 - menu_text.get_width() // 2, screen_height // 2 - 30))
        screen.blit(continue_text, (screen_width // 2 - continue_text.get_width() // 2, screen_height // 2))
        screen.blit(quit_text, (screen_width // 2 - quit_text.get_width() // 2, screen_height // 2 + 50))

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if continue_button_rect.collidepoint(mouse_pos):
                        return
                        exit();
                    elif quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        exit()

pygame.init()
