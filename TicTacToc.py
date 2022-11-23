from sys import exit
from random import randrange

# board game to be printed
board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]
]

def print_board(board):
    print("  +---+---+---+")
    print(str(3) + " | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("  +---+---+---+")
    print(str(2) + " | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("  +---+---+---+")
    print(str(1) + " | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print("    1   2   3")
    print("")

def computer_moves(level):

    def check_to_play_corners():
        corner_squares = [(0,0), (0,2), (2,0), (2,2)]
        empty_squares = []
        for sq in corner_squares:
            if board[sq[0]][sq[1]] == " ":
                empty_squares += [sq]
        if len(empty_squares) != 0:
            return empty_squares[randrange(len(empty_squares))]
        else:
            return None

    def check_to_play_middle():
        middle_squares = [(0,1), (1,0), (1,2), (2,1)]
        empty_squares = []
        for sq in middle_squares:
            if board[sq[0]][sq[1]] == " ":
                empty_squares += [sq]
        if len(empty_squares) != 0:
            return empty_squares[randrange(len(empty_squares))]
        else:
            return None

    def danger_sequence(sequence):
        xs = 0
        empty = None
        for sq in sequence:
            if board[sq[0]][sq[1]] == "X":
                xs += 1
            elif board[sq[0]][sq[1]] == " ":
                empty = sq

        if xs == 2 and empty is not None:
            return empty
        return None

    def win_sequence(sequence):
        os = 0
        empty = None
        for sq in sequence:
            if board[sq[0]][sq[1]] == "O":
                os += 1
            elif board[sq[0]][sq[1]] == " ":
                empty = sq

        if os == 2 and empty is not None:
            return empty
        return None

    def win():
        for i in range(3):
            row = [(i,j) for j in range(3)]
            sq = win_sequence(row)
            if sq is not None:
                return sq

        for j in range(3):
            col = [(i,j) for i in range(3)]
            sq = win_sequence(col)
            if sq is not None:
                return sq

        sq = win_sequence([(0,0),(1,1),(2,2)])
        if sq is not None:
            return sq

        sq = win_sequence([(0,2),(1,1),(2,0)])
        if sq is not None:
            return sq

    def danger():
        for i in range(3):
            row = [(i,j) for j in range(3)]
            sq = danger_sequence(row)
            if sq is not None:
                return sq

        for j in range(3):
            col = [(i,j) for i in range(3)]
            sq = danger_sequence(col)
            if sq is not None:
                return sq

        sq = danger_sequence([(0,0),(1,1),(2,2)])
        if sq is not None:
            return sq

        sq = danger_sequence([(0,2),(1,1),(2,0)])
        if sq is not None:
            return sq


    if level == 1:
        squares = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    squares += [(i,j)]

        return squares[randrange(len(squares))]
    elif level == 2:
        
        sq = danger()
        if sq is not None:
            return sq
        elif board[1][1] == " ":
            return (1,1)
        else:
            corner_squares = [(0,0), (0,2), (2,0), (2,2)]
            empty_squares = []
            for sq in corner_squares:
                if board[sq[0]][sq[1]] == " ":
                    empty_squares += [sq]
            if empty_squares:
                return empty_squares[randrange(len(empty_squares))]

            middle_squares = [(0,1), (1,0), (1,2), (2,1)]
            empty_squares = []
            for sq in middle_squares:
                if board[sq[0]][sq[1]] == " ":
                    empty_squares += [sq]
            if empty_squares:
                return empty_squares[randrange(len(empty_squares))]

    elif level == 3: # hard
        # check if computer can win and win
        sq = win()
        if sq is not None:
            return sq

        # check if player can win and prevent him
        sq = danger()
        if sq is not None:
            return sq

        # check if middle is available and if so play there
        if board[1][1] == " ":
            return (1,1)

        # check for future loss
        if board[2][0] == "X" and board[1][1] == "O" and board[0][2] == "X":
            sq = check_to_play_middle()
            if sq is not None:
                return sq
        
        if board[2][2] == "X" and board[1][1] == "O" and board[0][0] == "X":
            sq = check_to_play_middle()
            if sq is not None:
                return sq

        if board[0][0] == "X" and board[1][1] == "O" and board[2][2] == "X":
            sq = check_to_play_middle()
            if sq is not None:
                return sq

        if board[0][2] == "X" and board[1][1] == "O" and board[2][0] == "X":
            sq = check_to_play_middle()
            if sq is not None:
                return sq
        
        if board[1][0] == "X" and board[1][1] == "O" and board[2][1] == "X" and board[2][0] == " ":
            return (2,0)

        if board[1][2] == "X" and board[1][1] == "O" and board[2][1] == "X" and board[2][2] == " ":
            return (2,2)

        if board[1][0] == "X" and board[1][1] == "O" and board[0][1] == "X" and board[0][0] == " ":
            return (0,0)

        if board[1][2] == "X" and board[1][1] == "O" and board[0][1] == "X" and board[0][2] == " ":
            return (0,2)

        # check for corner to play
        sq = check_to_play_corners()
        if sq is not None:
            return sq

        # check for middle to play
        sq = check_to_play_middle()
        if sq is not None:
            return sq
        


def check_winner(player):
    # check rows
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    # check columns
    for column in range(len(board)):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def main():
    # player and computer symbols
    player = "X"
    computer = "O"
    # player start at the beggining
    player_playing = player

    # Printing welcome messages
    print(f"{'-'*40} TIC TAC TOE {'-'*40}")
    print("\tIt's you Vs the computer. Your symbol is X and computer's symbol is O\n\n")

    print("This game has 3 difficulties. An easy one, a normal one and a hard one.")
    print("1- Easy")
    print("2- Normal")
    print("3- Hard")
    while True:
        level = input("Which one would you like to play? ").strip()
        if not level.isdigit():
            print("Please enter 1,2 or 3.")
            print("")
            continue
        level = int(level)
        if level != 1 and level != 2 and level != 3:
            print("Please enter 1,2 or 3.")
            print("")
            continue
        break
    print("\n")
    rounds_played = 0
    while True:

        rounds_played += 1

        if player_playing == player:
            print("It's your turn to play.")
        else:
            print("It's computer's turn to play.")

        print("Round #"+str(rounds_played)+"\n")
        print_board(board)
        if player_playing == player:
            # Player part of the game
            # Input infinite loop
            while True:
                empty_box = False
                # Getting the row to play 'X'
                while True:
                    try:
                        row_to_play = int(input("Enter the row to play: "))
                    except ValueError as e:
                        print("You must enter a number!")
                        continue
                    except KeyboardInterrupt as e:
                        print("\nYou entered Ctrl+C so the programm stopped.")
                        exit()
                    if row_to_play<1 or row_to_play>3:
                        print("You must enter a number between 1 and 3!")
                        continue
                    break
                row_to_play -= 1
                
                # Getting the column to play 'X'
                while True:
                    try:
                        column_to_play = int(input("Enter the column to play: "))
                    except ValueError as e:
                        print("You must enter a number!")
                        continue
                    except KeyboardInterrupt as e:
                        print("\nYou entered Ctrl+C so the programm stopped.")
                        exit()
                    if column_to_play<1 or column_to_play>3:
                        print("You must enter a number between 1 and 3!")
                        continue
                    if board[row_to_play][column_to_play-1] != " ":
                        print("This box to play must be empty!")
                        empty_box = True
                        break
                    break
                if empty_box:
                    continue
                column_to_play -= 1
                break
            print("")

            # Making the move based on the input
            board[row_to_play][column_to_play] = player_playing
        else:
            # computer makes his random move on the board
            sq = computer_moves(level)
            board[sq[0]][sq[1]] = "O"

        # checks whether we have a winner
        if check_winner(player_playing):
            print("")
            if player_playing == player:
                print("You have won!!\n")
            else:
                print("Computer has won ):\n")
            print_board(board)
            break
        
        # checks whether we have a draw
        if rounds_played == 9:
            print("")
            print("It's a draw. Meh.\n")
            print_board(board)
            break
        
        # changing the state of the game
        if player_playing == player:
            player_playing = computer
        else:
            player_playing = player

    input()

if __name__ == '__main__':
    main()