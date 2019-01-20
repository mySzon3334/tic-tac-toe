import pygame as py
import settings as s
import functions as f

py.init()
display_size = 400
line_thickness = 5

gameDisplay = py.display.set_mode((display_size, display_size))
py.display.set_caption("Tik Tac Toe")
gameDisplay.fill(s.classic_theme.background_color)


def game_window(board):
    #board = [['x', 'x', ' '], ['o', 'x', 'o'], ['x', ' ', 'x']]
    a = (display_size - 2) / 3
    x = a / 2
    y = a / 2
    global gameDisplay
    py.draw.rect(gameDisplay, (0, 0, 0), (0, a, display_size, line_thickness))
    py.draw.rect(gameDisplay, (0, 0, 0), (0, 2 * a, display_size, line_thickness))
    py.draw.rect(gameDisplay, (0, 0, 0), (a, 0, line_thickness, display_size))
    py.draw.rect(gameDisplay, (0, 0, 0), (2 * a, 0, line_thickness, display_size))
    for p in range(0, 3):
        for p1 in range(0, 3):
            if board[p][p1] == 'o':
                message_display('o', 1, int(x), int(y))
            elif board[p][p1] == 'x':
                message_display('x', 1, int(x), int(y))
            x += a
        y += a
        x = a / 2

    py.display.update()
    gameDisplay.fill(s.classic_theme.background_color)


"""
def init():
    global gameDisplay
    gameDisplay = py.display.set_mode((display_size, display_size))
    py.display.set_caption("Tik Tac Toe")
    gameDisplay.fill(s.classic_theme.background_color)"""


def text_objects(text, font):
    textSurface = font.render(text, True, s.black)
    return textSurface, textSurface.get_rect()


def message_display(text, size, x=0, y=0):
    largeText = py.font.SysFont('Arial', int(display_size / 3))
    medText = py.font.SysFont('Arial', 50)
    """if size == 0:
        TextSurf, TextRect = text_objects(text, largeText)
     else:
        TextSurf, TextRect = text_objects(text, medText)"""
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)


#game_window([])
#f.wait_for_inp(1, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
