import multiplayer


def main():
    game = 1
    # game = selectScreen()   # 0 = vs cpu / local    1 = multiplayer over wlan
    if game == 0:
        pass
        # singleplayer.main()
    elif game == 1:
        multiplayer.main()
