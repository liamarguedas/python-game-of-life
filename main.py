from source import Game
from source import Cell
from source import User
import random


BACKGROUND_COLOR = "black"
CELL_COLOR = "white"
CELL_SIZE = 10
MINIMUM_ALLOWED_CELLS = 3


def main():

    engine = Game(FPS=2)
    user = User(engine.get_instance())

    screen = engine.get_screen()
    cells = []

    engine.create_canvas()

    game_started = False

    while True:

        screen.fill(BACKGROUND_COLOR)

        user_events = engine.get_instance().event.get()

        # Add initial cell from user
        if not game_started and user.clicked(user_events):
            x_user, y_user = user.get_click_pos()
            if (x_user, y_user) not in [cell.get_position() for cell in cells]:
                new_cell = Cell(screen, CELL_COLOR, x_user, y_user, CELL_SIZE)
                cells.append(new_cell)

        # Verify if user wanted to start the game
        if not game_started and user.started_game(user_events):
            if len(cells) > MINIMUM_ALLOWED_CELLS:
                game_started = True
                engine.set_fps(2)  # Higher than 2 fps would be to fast!
            else:
                print("PALCEHOLDER: NEED CEELS (MORE THAN 3)")


        if game_started:

            # LOGICA DO JOGO





        # Render all cells
        for cell in cells:
            cell.draw()

        engine.render_canvas()


if __name__ == "__main__":
    main()
