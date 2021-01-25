import sys
from pygame.locals import *
from hue_manager import *
from lines import *

# TODO: keys to adjust color step amount, toggle bouncing lines to just a box, qix mode?, use delta time?,
#  window sizes (full screen?), discordant mode: random starting positions (yuck), reset by setting to default values
#  Remove magic numbers

window_width = 960
window_height = 600

my_color = None
hue_manager = HueManager()
title = "Colored Lines Go Bounce Bounce!"

pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(title)
lines = Boxo(DISPLAY_SURFACE)


def game_exit():
    # clean up any loose ends.
    # what loose ends do we need to worry about in python?
    # find out and clean them up.
    pygame.quit()
    sys.exit()


while True:
    # TODO: organize to keep things in 'Input, Update, Render' order?
    # Get User Input
    for event in pygame.event.get():
        if event.type == QUIT:
            game_exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_exit()
            if event.key == pygame.K_TAB:
                hue_manager.toggle_pastel()
            if event.key == pygame.K_SPACE:
                lines.toggle_mode()
            if event.key == pygame.K_UP:
                hue_manager.adjust(1)
            if event.key == pygame.K_DOWN:
                hue_manager.adjust(-3)

    # Update Game State
    my_color = hue_manager.next_color()
    lines.update()

    # Render Game State
    lines.draw(my_color)
    pygame.display.update()
