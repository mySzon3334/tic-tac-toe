white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


class Theme:
    def __init__(self, background_color, text_color, player1_color, player2_color, board_color):
        self.background_color = background_color
        self.text_color = text_color
        self.player1_color = player1_color
        self.player2_color = player2_color
        self.board_color = board_color


classic_theme = Theme(white, black, red, blue, black)
