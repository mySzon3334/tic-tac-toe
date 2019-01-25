import socket
from functions import *
import visuals as v
import gui as g

debug = 1
side = ''
result = 0  # 0 = ongoing 1 = draw 2 = win 3 = lose


def main(conn_settings, debug_mode=0):
    global result
    if debug_mode == 1:
        global debug
        debug = 1
    """type = 0
    ip = '192.168.1.33'
    port = 50001"""

    type = conn_settings[1]
    ip = conn_settings[2]
    port = conn_settings[3]

    game_exit = False
    # abc = ['A', 'B', 'C']
    while not game_exit:
        netobj = connection_setup(type, ip, port)
        in_game = True
        game_session = True

        while game_session:
            v.init()
            while in_game:
                print('main loop start')
                # data receiving and decoding
                data = netobj.recv(1024)
                decoded_data = decode_data(data)
                if decoded_data == -1:
                    print('stopping game')
                    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    in_game = False
                else:
                    board = decoded_data

                v.game_window(board)
                result = check_board(board, side)
                if result != 0:
                    in_game = False
                    break
                print('w8 4 inp')
                inp = wait_for_inp(1, board)
                if inp[0] == 'exit':
                    netobj.sendall('22player left the game'.encode())
                    in_game = False
                    game_exit = True
                board[int(inp[1])][int(inp[0])] = side
                v.game_window(board)
                result = check_board(board, side)
                netobj.sendall(encode_data(board))
                if result != 0:
                    in_game = False
                else:
                    in_game = True
                    print('in game', in_game)
            v.close_game_display()
            if result == 1:
                g.set_aftergametext('Draw')
            elif result == 2:
                g.set_aftergametext('You Won')
            elif result == 3:
                g.set_aftergametext('You Lost')
            g.main(1)
            if g.launch == 'mp_game':
                in_game = True
            elif g.launch == 'mainmenu':
                in_game = False
                game_session = False


def connection_setup(type, ip, port):
    global side
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if debug == 1:
        print('Created socket')
    if type == 0:  # host
        s.bind((ip, port))
        if debug == 1:
            print('Binding socket')
        s.listen(1)
        conn, addr = s.accept()
        if debug == 1:
            print('Accepted connection from', addr)
        conn.sendall('25000000000'.encode())
        side = 'o'
        return conn
    elif type == 1:
        s.connect((ip, port))
        side = 'x'
        if debug == 1:
            print('Connected with host on', ip, port)
        return s
