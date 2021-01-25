import pygame
from itertools import cycle


# TODO: there's a lot of 'self' here, maybe figure out how to do static singleton stuff?


class Boxo:
    drawing_surface = None
    boundary_left = 0
    boundary_right = 0
    boundary_top = 0
    boundary_bottom = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    velocity = 1
    # mode = lines (lines/box)
    box_iterator = cycle((0, 1))
    box_mode = next(box_iterator)

    def __init__(self, my_surface):
        self.drawing_surface = my_surface
        self.boundary_right, self.boundary_bottom = self.drawing_surface.get_size()
        self.x2 = self.boundary_right
        self.y2 = self.boundary_bottom

    def update(self):
        # Increment values and do bounds checking in one line! We live in the future!
        self.x1 = (self.x1 + self.velocity) if (self.x1 < self.boundary_right) else self.boundary_left
        self.x2 = (self.x2 - self.velocity) if (self.x2 > self.boundary_left) else self.boundary_right
        self.y1 = (self.y1 + self.velocity) if (self.y1 < self.boundary_bottom) else self.boundary_top
        self.y2 = (self.y2 - self.velocity) if (self.y2 > self.boundary_top) else self.boundary_bottom

    def draw(self, my_color):
        if self.box_mode == 0:
            pygame.draw.line(self.drawing_surface, my_color, (self.x1, self.boundary_top),
                             (self.x1, self.boundary_bottom))
            pygame.draw.line(self.drawing_surface, my_color, (self.x2, self.boundary_top),
                             (self.x2, self.boundary_bottom))
            pygame.draw.line(self.drawing_surface, my_color, (self.boundary_left, self.y1),
                             (self.boundary_right, self.y1))
            pygame.draw.line(self.drawing_surface, my_color, (self.boundary_left, self.y2),
                             (self.boundary_right, self.y2))
        if self.box_mode == 1:
            # rectangle is fucked - why? in meantime, do lines? (divide each coord by 2!)
            # pygame.draw.rect(self.drawing_surface, my_color, (self.x1, self.y1, self.x2, self.y2))
            my_points = [(self.x1, self.y1), (self.x2, self.y1), (self.x2, self.y2), (self.x1, self.y2)]
            pygame.draw.lines(self.drawing_surface, my_color, True, my_points)
        # if box mode, draw rect() instead

    def toggle_mode(self):
        self.box_mode = next(self.box_iterator)
