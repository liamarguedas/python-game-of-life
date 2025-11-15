from source import Game


BACKGROUND_COLOR = "black"
CELL_COLOR = "white"
CELL_SIZE = 10


def main():

    g = Game()
    screen = g.get_screen()

    g.create_canvas()

    while True:

        screen.fill(BACKGROUND_COLOR)

        g.render_canvas()


if __name__ == "__main__":
    main()
