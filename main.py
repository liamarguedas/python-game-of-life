from source import Game
from source import Cell
from source import User
import random


BACKGROUND_COLOR = "black"
CELL_COLOR = "white"
CELL_SIZE = 10
MINIMUM_ALLOWED_CELLS = 3


def main():

    engine = Game(FPS=60)
    user = User(engine.get_instance(), CELL_SIZE)

    generation, killed = 0, 0
    screen = engine.get_screen()
    cells = []

    engine.create_canvas()

    game_started = False

    while True:

        screen.fill(BACKGROUND_COLOR)

        user_events = engine.get_instance().event.get()

        if user.reset_game(user_events):
            cells.clear()
            game_started = False

        # Add initial cell from user
        if not game_started and user.clicked(user_events):
            x_user, y_user = user.get_click_pos()
            if (x_user, y_user) not in [cell.get_position() for cell in cells]:
                cells.append(Cell(screen, CELL_COLOR, x_user, y_user, CELL_SIZE))

        # Verify if user wanted to start the game
        if not game_started and user.started_game(user_events):
            if len(cells) > MINIMUM_ALLOWED_CELLS:
                game_started = True
                engine.set_fps(2)  # Higher than 2 fps would be to fast!
            else:
                print("PALCEHOLDER: NEED CEELS (MORE THAN 3)")

        # If initial cells have been added (Game started)
        if game_started:
            print("-" * 10)
            print(f"Current generation: {generation}")
            print(f"Current alive cells: {len(cells)}")
            print(f"Killed cells: {killed}")
            print("-" * 10)
            generation += 1

            # Store alive cells and position
            cells_alive = [cell for cell in cells if cell.is_alive()]
            cells_alive_positions = [cell.get_position() for cell in cells_alive]

            for cell in cells_alive:

                cell_neighbors_position = cell.get_neighbors().values()

                # Retrieven how many alive neighbors the cell has
                cell_alive_neighbors = 0
                for neighbor_position in cell_neighbors_position:
                    if neighbor_position in cells_alive_positions:
                        cell_alive_neighbors += 1

                    # Rebirth dead cells if it has 3 alive neighbors
                    # Neighbors that are dead
                    if neighbor_position not in cells_alive_positions:
                        nons = cell.get_neighbors_from_cords(*neighbor_position)
                        alive_neighbors_of_nons = 0
                        for non in nons.values():
                            if non in cells_alive_positions:
                                alive_neighbors_of_nons += 1

                        if alive_neighbors_of_nons == 3:
                            cells.append(
                                Cell(
                                    screen,
                                    CELL_COLOR,
                                    neighbor_position[0],
                                    neighbor_position[1],
                                    CELL_SIZE,
                                )
                            )

                # If cell has less than 2 or cell has more than 3 neighbors -> kill
                if cell_alive_neighbors < 2 or cell_alive_neighbors > 3:

                    cell_to_remove_index = [c.get_identifier() for c in cells].index(
                        cell.get_identifier()
                    )
                    cells.pop(cell_to_remove_index)

                    cell.kill(BACKGROUND_COLOR)
                    killed += 1

        # Render all cells
        for cell in cells:
            cell.draw()

        engine.render_canvas()


if __name__ == "__main__":
    main()
