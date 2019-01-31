import pygame as py
import settings as s

display_size = 460
text_box_size = 60
line_thickness = 5

screens = []


def init():
    py.init()
    global screens
    gameDisplay = py.display.set_mode((display_size - text_box_size, display_size))
    screens.append(gameDisplay)
    py.display.set_caption("Tik Tac Toe")
    gameDisplay.fill(s.classic_theme.background_color)
    b = text_box_size
    a = (display_size - 2 - b) / 3
    message_display('Waiting for opponent move', 1, 20, 20)
    py.draw.rect(gameDisplay, (0, 0, 0), (0, b, display_size, line_thickness))
    py.draw.rect(gameDisplay, (0, 0, 0), (0, a + b, display_size + b, line_thickness))
    py.draw.rect(gameDisplay, (0, 0, 0), (0, 2 * a + b, display_size + b, line_thickness))
    py.draw.rect(gameDisplay, (0, 0, 0), (a, 0 + b, line_thickness, display_size + b))
    py.draw.rect(gameDisplay, (0, 0, 0), (2 * a, 0 + b, line_thickness, display_size + b))
    py.display.update()


def game_window(board, text):
    print('started drawing screen')
    gameDisplay = screens[0]
    gameDisplay.fill(s.classic_theme.background_color)
    message_display(text, 1, 20, 20)
    # board = [['x', 'x', ' '], ['o', 'x', 'o'], ['x', ' ', 'x']]
    b = text_box_size
    a = (display_size - 2 - b) / 3
    x = a / 2
    y = a / 2 + b
    b = text_box_size
    py.draw.rect(gameDisplay, (0, 0, 0), (0, b, display_size, line_thickness))
    py.draw.rect(gameDisplay, (0, 0, 0), (0, a + b, display_size, line_thickness))
    py.draw.rect(gameDisplay, (0, 0, 0), (0, 2 * a + b, display_size, line_thickness))
    py.draw.rect(gameDisplay, (0, 0, 0), (a, 0 + b, line_thickness, display_size))
    py.draw.rect(gameDisplay, (0, 0, 0), (2 * a, 0 + b, line_thickness, display_size))
    for p in range(0, 3):
        for p1 in range(0, 3):
            if board[p][p1] == 'o':
                message_display('o', 0, int(x), int(y))
            elif board[p][p1] == 'x':
                message_display('x', 0, int(x), int(y))
            x += a
        y += a
        x = a / 2

    py.display.update()

    print('finished drawing screen')


"""
def init():
    global gameDisplay
    gameDisplay = py.display.set_mode((display_size, display_size))
    py.display.set_caption("Tik Tac Toe")
    gameDisplay.fill(s.classic_theme.background_color)"""


def text_objects(text, font):
    textSurface = font.render(text, True, s.black)
    return textSurface, textSurface.get_rect()


def message_display(text, size=1, x=0, y=0):
    gameDisplay = screens[0]
    largeText = py.font.SysFont('Arial', int(display_size / 3))
    medText = py.font.SysFont('Arial', 20)
    if size == 0:
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = (x, y)
    else:
        TextSurf, TextRect = text_objects(text, medText)
        TextRect.center = (display_size / 2, y)

    # TextSurf, TextRect = text_objects(text, medText)

    gameDisplay.blit(TextSurf, TextRect)


def close_game_display():
    global screens
    screens.pop()
    py.quit()


if __name__ == '__main__':
    init()
    for p in range(0, 1000):
        game_window([['x', 'x', ' '], ['o', 'x', 'o'], ['x', ' ', 'x']])
