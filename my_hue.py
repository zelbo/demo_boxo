from clamp_value import clamp


class Hue:
    minimum = 0  # 0 for full spectrum, 153 for pastel
    maximum = 255
    level = 0
    step = 0
    linked_hue = None

    def __init__(self, my_level, my_step, my_min):
        self.level = my_level
        self.step = my_step
        self.minimum = my_min

    def increment(self):
        self.level = self.level + self.step
        if (self.level > self.maximum) or (self.level < self.minimum):
            self.level = clamp(self.level, self.minimum, self.maximum)
            self.linked_hue.step = -self.step
            self.step = 0

    def set_boundaries(self, my_min, my_max):
        self.minimum = my_min
        self.maximum = my_max
