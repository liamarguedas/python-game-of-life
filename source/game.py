import pygame


class Game:

    def __init__(self, FPS: int = 30, WIDTH: int = 1000, HEIGHT: int = 1000):

        self.FPS = FPS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.game_engine = pygame

    def create_canvas(self):
        self.game_engine.init()

    def render_canvas(self):
        self.game_engine.display.flip()
        self.game_engine.time.Clock().tick(self.FPS)

    def get_screen(self):
        screen = self.game_engine.display.set_mode((self.WIDTH, self.HEIGHT))
        return screen

    def get_instance(self):
        return self.game_engine

    def set_fps(self, fps):
        self.FPS = fps
