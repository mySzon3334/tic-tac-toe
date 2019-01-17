import socket
import config as c

board_size = 3


def main():
    if c.type == 0:
        host()
    elif c.type == 1:
        player()
    else:
        print("Connection Error: In config.py selected wrong type, must be 0 or 1")


def host():
    board = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
    abc = ['A', 'B', 'C']
    inGame = False
    exit = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((c.ip, c.port))
    while not exit:
        try:
            s.listen(1)
            conn, addr = s.accept()
            inGame = True
        except:
            print('Connection Error: Error occurred while trying to accept incoming connection, retrying')
        while inGame:
            print_board(board)
            inp0 = input('Row -> ')
            inp1 = input('Column -> ')
            if inp0 == 'exit':
                # noinspection PyUnboundLocalVariable
                conn.sendall('Info: host quit the game, disconnecting'.encode())
                inGame = False
                exit = True
            else:
                board[int(inp0) - 1][int(abc.index(inp1))] = 'x'
                if check_board(board) == 'x':
                    print('You Win')
                    inGame = False
                buff = board
                conn.sendall(board_encode(board))
                data = conn.recv(3072)
                board = board_decode(data)
                if type(board) == str:
                    print(board)
                    board = buff
                    print('Continuing game')
                if check_board(board) == 'o':
                    print('You Lost')
                    print_board(board)
                    inGame = False
            # while after game
    try:
        # noinspection PyUnboundLocalVariable
        conn.close()
    except:
        print('error occurred while trying to disconnect, closing')
    print('disconnected')


def player():
    inGame = False
    exit = False
    buff = []
    abc = ['A', 'B', 'C']
    while not exit:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((c.ip, c.port))
            inGame = True
        except:
            print('Connection Error: Error occurred while trying to accept incoming connection, retrying')
        while inGame:
            data = s.recv(3072)
            board = board_decode(data)
            if type(board) == str:
                print(board)
                if len(buff) == 0:
                    print('Error: Game was unable to continue after incident, retrying')
                    inGame = False
                else:
                    board = buff
                    print('Continuing game')
            if check_board(board) == 'x':
                print('You Lost')
                print_board(board)
                inGame = False
            else:
                print_board(board)
                inp0 = input('Row -> ')
                inp1 = input('Column -> ')
                if inp0 == "exit":
                    s.sendall('Info: player quit the game, disconnecting'.encode())
                    inGame = False
                    exit = True
                else:
                    board[int(inp0) - 1][int(abc.index(inp1))] = 'o'
                    s.sendall(board_encode(board))
                    if check_board(board) == 'o':
                        print('You Win')
                        inGame = False
        print('end')
        s.close()
    s.close()


def print_board(board):
    """for p in range(0, board_size):
        print(board[p])"""
    for p in range(0, board_size):
        for p1 in range(0, board_size):
            if board[p][p1] == '0':
                board[p][p1] = ' '
    print('   A   B   C')
    print('1.', board[0][0], '|', board[0][1], '|', board[0][2])
    print('   __|___|__')
    print('2.', board[1][0], '|', board[1][1], '|', board[1][2])
    print('   __|___|__')
    print('3.', board[2][0], '|', board[2][1], '|', board[2][2])
    print('     |   |  ')


def board_encode(board):
    temp = []
    for p in range(0, board_size):
        for p1 in range(0, board_size):
            temp.append(str(board[p][p1]))
    # for p in range(0, len(temp)):
    string = ''.join(temp)
    print(string)
    string = string.encode()
    return string


def board_decode(string):
    string = string.decode()
    string = list(string)
    try:
        if string[0] == 'I' and string[1] == 'n' and string[2] == 'f':
            board = ''.join(string)
        else:
            temp = []
            board = []
            for p in range(0, board_size * board_size):
                temp.append(string[p])
                if len(temp) == board_size:
                    board.append(temp)
                    temp = []
    except:
        print(string)
    print(board)
    return board


def check_board(board):
    for p in range(0, 2):
        if p == 0:
            f = 'x'
        else:
            f = 'o'
        for p1 in range(0, 3):
            if board[p1][0] == f and board[p1][1] == f and board[p1][2] == f:
                return f
        for p1 in range(0, 3):
            if board[0][p1] == f and board[1][p1] == f and board[2][p1] == f:
                return f
        if board[0][0] == f and board[1][1] == f and board[2][2] == f:
            return f
        if board[0][2] == f and board[1][1] == f and board[2][0] == f:
            return f
    return -1


# board_decode(board_encode([['x', 0, 0], ['o', 'x', 0], ['o', 'o', 'o']]))


host()
#player()
