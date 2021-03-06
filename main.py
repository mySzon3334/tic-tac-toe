import multiplayer
import gui
import visuals


def main():
    gui.main()
    game = gui.launch
    game_settings = gui.launch_settings
    if game == 'sp_game':
        pass
        # singleplayer.main()
    elif game == 'mp_game':
        gui.clear_launch()
        print(game_settings)
        multiplayer.main(game_settings, debug_mode=0)


if __name__ == '__main__':
    main()
