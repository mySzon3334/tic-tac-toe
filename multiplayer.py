import socket
from functions import *
import visuals as v

debug = 1


def main(debug_mode=0):
    if debug_mode == 1:
        global debug
        debug = 1
    type = 0
    ip = '192.168.1.33'
    port = 50001
    game_exit = False
    abc = ['A', 'B', 'C']
    side = 'o'
    while not game_exit:
        netobj = connection_setup(type, ip, port)
        in_game = True
        game_session = True

        while game_session:

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
                in_game = check_board(board, side)
                print('w8 4 inp')
                inp = wait_for_inp(1, board)
                if inp[0] == 'exit':
                    netobj.sendall('22player left the game'.encode())
                    in_game = False
                    game_exit = True
                board[int(inp[1])][int(inp[0])] = side
                in_game = check_board(board, side)
                netobj.sendall(encode_data(board))
                print('in game', in_game)
            # game_over_screen()


def connection_setup(type, ip, port):
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
        return conn
    elif type == 1:
        s.connect((ip, port))
        if debug == 1:
            print('Connected with host on', ip, port)
        return s


main()
