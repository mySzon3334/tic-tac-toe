import gui
import visuals

# ======================================================================================================================
# THIS MODULE IS NOT USED
# ======================================================================================================================


gui.main()
print('6876529156')
if gui.launch == 'mp_game':
    visuals.init()
    while 1:
        visuals.game_window([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
