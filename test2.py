import gui
import visuals

gui.main()
if gui.launch == 'mp_game':
    while 1:
        visuals.game_window([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
