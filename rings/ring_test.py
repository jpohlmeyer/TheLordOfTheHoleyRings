import random


class RingTest:

    def __init__(self, center_position, sizes, is_black):
        self.holey_rings = []
        for size in sizes:
            for count in range(0, 5):
                self.holey_rings.append(HoleyRing(center_position, size, random.randint(0, 7)))
        self.holey_rings.reverse()
        self.ring_index = -1
        self.is_black = is_black

    def current_ring(self):
        return self.holey_rings[self.ring_index]

    def next_ring(self):
        if self.ring_index < len(self.holey_rings) - 1:
            self.ring_index += 1
            return True
        else:
            return False


class HoleyRing:

    def __init__(self, center_position, circle_radius, hole_type):
        self.center_position = center_position
        self.circle_radius = circle_radius
        self.hole_radius = circle_radius / 4
        self.line_width = max(circle_radius / 5, 1)
        self.hole_type = hole_type
        self.hole_position = self.calculate_hole_position()

    def calculate_hole_position(self):
        halfholesize = self.hole_radius
        if self.hole_type == 0:
            x = self.center_position
            y = self.center_position - self.circle_radius
        elif self.hole_type == 1:
            x = self.center_position + (self.circle_radius / 2) + halfholesize
            y = self.center_position - (self.circle_radius / 2) - halfholesize
        elif self.hole_type == 2:
            x = self.center_position + self.circle_radius
            y = self.center_position
        elif self.hole_type == 3:
            x = self.center_position + (self.circle_radius / 2) + halfholesize
            y = self.center_position + (self.circle_radius / 2) + halfholesize
        elif self.hole_type == 4:
            x = self.center_position
            y = self.center_position + self.circle_radius
        elif self.hole_type == 5:
            x = self.center_position - (self.circle_radius / 2) - halfholesize
            y = self.center_position + (self.circle_radius / 2) + halfholesize
        elif self.hole_type == 6:
            x = self.center_position - self.circle_radius
            y = self.center_position
        else:
            x = self.center_position - (self.circle_radius / 2) - halfholesize
            y = self.center_position - (self.circle_radius / 2) - halfholesize
        return x, y
