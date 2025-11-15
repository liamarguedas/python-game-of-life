import pygame


class Cell:

    def __init__(self, screen, cell_color, x_init, y_init, size) -> None:

        self.screen = screen
        self.color = cell_color
        self.alive = True
        self.x = x_init
        self.y = y_init
        self.size = (size, size)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, *self.size))

    def is_alive(self):
        return self.alive

    def kill_cell(self, background_color):
        self.color = background_color
        self.alive = False
        self.draw()

    def set_new_position(self, x_new, y_new):
        self.x = x_new
        self.y = y_new

    def get_position(self):
        return self.x, self.y

    # def get_neighbors(self):

    # Metodo pra mover

    # Metodo para retornar vizinhos
