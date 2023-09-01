import pygame
import pytmx
import os

class Map:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TMX Map Rendering")

# Create an instance of the Map class with your TMX map filename
map_filename = os.path.join("levels", "maps", "level_1.tmx")
game_map = Map(map_filename)
map_surface = pygame.Surface((game_map.width, game_map.height), pygame.SRCALPHA).convert_alpha()

bg = pygame.image.load(os.path.join("assets", "img", "bg", "game_layer.png")).convert()

game_map.render(map_surface)
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill("purple")

    # Render the map onto the Pygame window
    # screen.blit(bg, (0, 0))
    screen.blit(map_surface, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
