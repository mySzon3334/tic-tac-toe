import socket
from functions import *

debug = 1


def main(debug_mode=0):
    if debug_mode == 1:
        global debug
        debug = 1
    type = 1
    ip = '25.50.83.172'
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
                data = netobj.recv(1024)
                decoded_data = decode_data(data)
                if decoded_data == -1:
                    print('stopping game')
                    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    in_game = False
                else:
                    board = decoded_data
                # check_game_state()
                #
                inp = wait_for_inp(0, board)
                if inp[0] == 'exit':
                    netobj.sendall('22player left the game'.encode())
                    in_game = False
                    game_exit = True
                board[int(inp[0]) - 1][int(abc.index(inp[1]))] = side
                netobj.sendall(encode_data(board))
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
