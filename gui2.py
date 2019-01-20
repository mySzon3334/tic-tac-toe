import pygame as py
import settings as s

py.init()

display_width = 800
display_height = 800


class Settings:
    pass

sett = Settings


def game_window(board):



def init(display_width, display_height):
    gameDisplay = py.display.set_mode((display_width, display_height))
    py.display.set_caption("Tik Tac Toe")
    gameDisplay.fill(s.classic_theme.background_color)


init(800, 600)
