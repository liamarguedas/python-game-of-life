class User:

    def __init__(self, instance) -> None:
        self.instance = instance
        self.click_pos = (None, None)

    @staticmethod
    def round_number(num, threshold=5):
        last_digit = num % 10
        if last_digit < threshold:
            return num - last_digit
        return num + (10 - last_digit)

    def user_click(self):
        for event in self.instance.event.get():
            if event.type == self.instance.MOUSEBUTTONDOWN:
                self.set_click_pos(*event.pos)
                return True
        return False

    def get_user_click_pos(self):
        return self.click_pos

    def set_click_pos(self, x, y):
        x_user, y_user = self.round_number(x), self.round_number(y)
        self.click_pos = (x_user, y_user)
