import pygame, string, random
from .position import Position


class Cell:

    def __init__(self, screen, cell_color, x_init, y_init, size) -> None:

        self.identifier = self.generate_cell_identifier()
        self.screen = screen
        self.color = cell_color
        self.alive = True
        self.x = x_init
        self.y = y_init
        self.size = (size, size)
        self.side_size = size
        self.neightbors = self.set_neighbors()

    @staticmethod
    def generate_cell_identifier(size=10):
        return "".join([random.choice(string.printable) for _ in range(size)])

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, *self.size))

    def is_alive(self):
        return self.alive

    def kill(self, background_color):
        self.color = background_color
        self.alive = False
        self.draw()

    def set_neighbors(self):
        return {
            Position.NW: (self.x - self.side_size, self.y - self.side_size),
            Position.N: (self.x, self.y - self.side_size),
            Position.NE: (self.x + self.side_size, self.y - self.side_size),
            Position.W: (self.x - self.side_size, self.y),
            Position.E: (self.x + self.side_size, self.y),
            Position.SW: (self.x - self.side_size, self.y + self.side_size),
            Position.S: (self.x, self.y + self.side_size),
            Position.SE: (self.x + self.side_size, self.y + self.side_size),
        }

    def get_identifier(self):
        return self.identifier

    def get_position(self):
        return self.x, self.y

    def get_neighbors(self):
        return self.neightbors

    def get_neighbors_from_cords(self, x, y):
        return {
            Position.NW: (x - self.side_size, y - self.side_size),
            Position.N: (x, y - self.side_size),
            Position.NE: (x + self.side_size, y - self.side_size),
            Position.W: (x - self.side_size, y),
            Position.E: (x + self.side_size, y),
            Position.SW: (x - self.side_size, y + self.side_size),
            Position.S: (x, y + self.side_size),
            Position.SE: (x + self.side_size, y + self.side_size),
        }
