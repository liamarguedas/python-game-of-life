class User:

    def __init__(self, engine, size) -> None:
        self.engine = engine
        self.size = size
        self.click_pos = (None, None)

    def round_number(self, num, threshold=5):
        last_digit = num % self.size
        if last_digit < threshold:
            return num - last_digit
        return num + (self.size - last_digit)

    def clicked(self, events):
        for event in events:
            if event.type == self.engine.MOUSEBUTTONDOWN:
                self.set_click_pos(*event.pos)
                return True
        return False

    def started_game(self, events):
        for event in events:
            if event.type == self.engine.KEYDOWN:
                if event.key == self.engine.K_SPACE:
                    return True
        return False

    def reset_game(self, events):
        for event in events:
            if event.type == self.engine.KEYDOWN:
                if event.key == self.engine.K_BACKSPACE:
                    return True
        return False

    def get_click_pos(self):
        return self.click_pos

    def set_click_pos(self, x, y):
        x_user, y_user = self.round_number(x), self.round_number(y)
        self.click_pos = (x_user, y_user)
