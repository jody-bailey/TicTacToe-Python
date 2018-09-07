# This code was written by Jody Bailey

player_board = [' '] * 9
keep_playing = True


def print_board(board):
    print('       |       |       \n'
          '   {6}   |   {7}   |   {8}  \n'
          '_______|_______|_______\n'
          '       |       |       \n'
          '   {3}   |   {4}   |   {5}  \n'
          '_______|_______|_______\n'
          '       |       |       \n'
          '   {0}   |   {1}   |   {2}  \n'
          '       |       |       \n'.format(board[0], board[1], board[2], board[3],
                                             board[4], board[5], board[6], board[7], board[8]))


def winner():
    if player_board[0] == 'X' and player_board[1] == 'X' and player_board[2] == 'X':
        return True
    elif player_board[0] == 'X' and player_board[4] == 'X' and player_board[8] == 'X':
        return True
    elif player_board[0] == 'X' and player_board[3] == 'X' and player_board[6] == 'X':
        return True
    elif player_board[3] == 'X' and player_board[4] == 'X' and player_board[5] == 'X':
        return True
    elif player_board[6] == 'X' and player_board[7] == 'X' and player_board[8] == 'X':
        return True
    elif player_board[1] == 'X' and player_board[4] == 'X' and player_board[7] == 'X':
        return True
    elif player_board[2] == 'X' and player_board[5] == 'X' and player_board[8] == 'X':
        return True
    elif player_board[3] == 'X' and player_board[5] == 'X' and player_board[7] == 'X':
        return True
    elif player_board[0] == 'O' and player_board[1] == 'O' and player_board[2] == 'O':
        return True
    elif player_board[0] == 'O' and player_board[4] == 'O' and player_board[8] == 'O':
        return True
    elif player_board[0] == 'O' and player_board[3] == 'O' and player_board[6] == 'O':
        return True
    elif player_board[3] == 'O' and player_board[4] == 'O' and player_board[5] == 'O':
        return True
    elif player_board[6] == 'O' and player_board[7] == 'O' and player_board[8] == 'O':
        return True
    elif player_board[1] == 'O' and player_board[4] == 'O' and player_board[7] == 'O':
        return True
    elif player_board[2] == 'O' and player_board[5] == 'O' and player_board[8] == 'O':
        return True
    elif player_board[3] == 'O' and player_board[5] == 'O' and player_board[7] == 'O':
        return True
    else:
        return False


def check_draw():
    empty = False
    for slot in player_board:
        if slot == ' ':
            empty = True
    if empty:
        return False
    else:
        return True


def valid_move(num):
    if player_board[num - 1] == ' ':
        return True
    else:
        return False


def clear_board():
    player_board[0] = ' '
    player_board[1] = ' '
    player_board[2] = ' '
    player_board[3] = ' '
    player_board[4] = ' '
    player_board[5] = ' '
    player_board[6] = ' '
    player_board[7] = ' '
    player_board[8] = ' '


def play():
    player1 = input("Please pick a marker 'X' or 'O'").upper()
    game_round = 1
    text = ''
    draw = False

    while player1 != 'X' and player1 != 'O':
        player1 = input("Must enter 'X' or 'O'").upper()
        print(player1)

    print('Player one is going first')

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    while not winner():
        if check_draw():
            draw = True
            break
        if game_round % 2 == 0:
            current_player = player2
            text = 'Player 2'
        else:
            current_player = player1
            text = 'Player 1'

        answer = 0

        while answer < 1 or answer > 9:
            try:
                answer = int(input('{} choose your move (1-9)'.format(text)))
            except (IOError, ValueError):
                print('Input not accepted. Try again.')

        while not valid_move(answer):
            print('Not a valid move. Try again.')
            answer = 0
            while answer < 1 or answer > 9:
                try:
                    answer = int(input('{} choose your move (1-9)'.format(text)))
                except (IOError, ValueError):
                    print('Input not accepted. Try again.')

        player_board[answer - 1] = current_player

        print_board(player_board)
        game_round += 1

    if draw:
        print('IT WAS A DRAW!!! ')
    else:
        print('{} WON THE GAME!!!'.format(text))


while keep_playing:
    play()
    toPlayOrNot = input('Would you like to play again? (Yes/No)').lower()
    while toPlayOrNot != 'yes' and toPlayOrNot != 'no':
        toPlayOrNot = input('Not a valid answer. Try again. Yes or No').lower()

    if toPlayOrNot == 'yes':
        keep_playing = True
        clear_board()
    else:
        keep_playing = False
