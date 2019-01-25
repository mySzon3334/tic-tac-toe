import multiplayer
import gui


def main():
    gui.main()
    game = gui.launch
    game_settings = gui.launch_settings
    if game == 'sp_game':
        pass
        # singleplayer.main()
    elif game == 'mp_game':
        multiplayer.main(game_settings, debug_mode=0)


main()
