import math

PLAYER_X='X'
PLAYER_O='O'
EMPTY=''
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print(' - ' * 5)
def check_winner(board):
    lines=[board[i] for i in range(3)] + \
           [[board[i][j] for i in range(3) for j in range(3)]] + \
            [[board[i][i] for i in range(3)]] + \
            [[board[i][2-i] for i in range(3)]]
    for line in lines:
            if line[0] == line[1] == line[2] and line[0] !=EMPTY :
                return line[0]
    return None
def is_full(board):
    return all(cell !=EMPTY for row in board for cell in row)
def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if  board[r] [c]==EMPTY]
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_O:
        return 10
    if winner == PLAYER_X:
        return -10
    if is_full(board):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for r, c in get_empty_cells(board):
            board[r][c]=PLAYER_O
            score = minimax(board, False)
            board[r][c]=EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r, c in get_empty_cells(board):
            board[r][c] = PLAYER_X
            score=minimax(board, True)
            board[r][c] = EMPTY
            best_score = min(score, best_score)
        return best_score
def find_best_move(board):
    best_move=None
    best_score = -math.inf
    for r, c in get_empty_cells(board):
        board[r][c]=PLAYER_O
        score = minimax(board, False)
        board[r][c]=EMPTY
        if score>best_score:
            best_score=score
            best_move=(r, c)
    return best_move

def play_game():
    board=[[EMPTY]*3 for _ in range(3)]
    current_player=PLAYER_X

    while True:
        print_board(board)
        if current_player==PLAYER_X:
            print("Player X' s turn (AI)")
            move=find_best_move(board)
            if move:
                board[move[0]][move[1]]=PLAYER_X

        else:
            print("Player O's turn (You)")
            while True:
                try:
                    row=int(input("Enter row (0, 1, 2): "))
                    col=int(input("Enter col (0, 1, 2): " ))
                    if (row, col) in get_empty_cells(board):
                        board[row][col]=PLAYER_O
                        break
                    else:
                        print("Cell already occupied or out of range, try again.")
                except (ValueError, IndexError):
                    print("Invalid input, please enter numbers between 0 and 2.")

        winner=check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player=PLAYER_X if current_player==PLAYER_O else PLAYER_O


if __name__ == "__main__":
    play_game()