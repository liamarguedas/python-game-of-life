import pygame


class Game:

    def __init__(self, FPS: int = 30, WIDTH: int = 1000, HEIGHT: int = 1000):

        self.FPS = FPS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.game_instance = pygame

    def create_canvas(self):
        self.game_instance.init()

    def render_canvas(self):
        self.game_instance.display.flip()
        self.game_instance.time.Clock().tick(self.FPS)

    def get_screen(self):
        screen = self.game_instance.display.set_mode((self.WIDTH, self.HEIGHT))
        return screen

    def get_instance(self):
        return self.game_instance
