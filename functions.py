def decode_data(string):
    board_size = 3
    string = string.decode()
    string = list(string)
    if len(string) > 0:
        if string[0] == '2' and string[1] == '2':
            msg = ''.join(string)
            print('Error occurred:', msg)
            return -1
        elif string[0] == '2' and string[1] == '5':
            temp = []
            board = []
            for p in range(0, board_size * board_size):
                temp.append(string[p])
                if len(temp) == board_size:
                    board.append(temp)
                    temp = []
            print(string, board)
            return board


def encode_data(board):
    board_size = 3
    temp = ['2', '5']
    for p in range(0, board_size):
        for p1 in range(0, board_size):
            temp.append(str(board[p][p1]))
    string = ''.join(temp)
    print(string)
    string = string.encode()
    return string


def wait_for_inp(inp_type, board):
    abc = ['A', 'B', 'C']
    if inp_type == 0:
        done = False
        while not done:
            inp0 = input('Row -> ')
            inp1 = input('Column -> ')
            if inp0 == 'exit':
                return -1
            elif board[inp0][abc.index(inp1)] == 0:
                # done = True
                return [inp0, inp1]


def show_board(board):
    board_size = 3
    for p in range(0, board_size):
        print(board[p])
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
