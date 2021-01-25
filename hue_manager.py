from my_hue import *
from itertools import cycle

# "Web safe" Hex 00, 33, 66, 99, cc, ff
# 0 – 255
# full spectrum min = 0, pastel min = 153
# smooth step_amount = 1, web safe step_amount = 51
# UP = step_amount, DOWN = step_amount * -1


class HueManager:
    step_size = 3  # 1 for slow shift of color, 3 is decent, 51 for very short gradient
    level_minimum = 0
    pastel_value = 153
    pastel_iterator = cycle((0, 1))
    pastel_mode = next(pastel_iterator)

    red = Hue(255, 0, level_minimum)
    green = Hue(level_minimum, step_size, level_minimum)
    blue = Hue(level_minimum, 0, level_minimum)
    red.linked_hue = blue
    green.linked_hue = red
    blue.linked_hue = green

    def reset(self):
        self.red.level = 255
        self.green.level = self.level_minimum
        self.blue.level = self.level_minimum
        self.red.step = 0
        self.green.step = self.step_size
        self.blue.step = 0
        self.red.minimum = self.level_minimum
        self.green.minimum = self.level_minimum
        self.blue.minimum = self.level_minimum

    def next_color(self):
        color_tuple = (self.red.level, self.green.level, self.blue.level)
        self.red.increment()
        self.blue.increment()
        self.green.increment()
        return color_tuple

    def toggle_pastel(self):
        self.pastel_mode = next(self.pastel_iterator)
        self.level_minimum = self.pastel_mode * self.pastel_value
        self.reset()

    def adjust(self, adjustment):
        # TODO: should this be two separate UP/DOWN functions?
        #  use clamp here?
        #  something wonky here, need more thinkin. should work without reset, but it don't.
        self.step_size = clamp((self.step_size + adjustment), 1, 52)
        # self.step_size = (self.step_size + adjustment) if (self.step_size in range(1, 52)) else self.step_size
        self.reset()
