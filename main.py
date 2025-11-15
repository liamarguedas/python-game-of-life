from source import Game
from source import Cell
from source import User
import random


BACKGROUND_COLOR = "black"
CELL_COLOR = "white"
CELL_SIZE = 10


def main():

    g = Game(FPS=60)
    u = User(g.get_instance())
    screen = g.get_screen()
    cells = list()

    g.create_canvas()

    while True:

        screen.fill(BACKGROUND_COLOR)

        if u.user_click():
            x_user, y_user = u.get_user_click_pos()
            c = Cell(screen, CELL_COLOR, x_user, y_user, CELL_SIZE)
            cells.append(c)

        for cell in cells:
            cell.draw()

        g.render_canvas()


if __name__ == "__main__":
    main()
