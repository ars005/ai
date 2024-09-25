def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col]==1:
            return False
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,-1,-1), range(col,N)):
        if board[i][j]==1:
            return False
    return True

def solve_n_queens_util(board,row,N,solutions):
    if row==N:
        solution=[]
        for i in range(N):
            sol_row=""
            for j in range(N):
                if board[i][j]==1:
                    sol_row+='Q'
                else:
                    sol_row+='.'
            solution.append(sol_row)
        solutions.append(solution)
        return
    for col in range(N):
        if is_safe(board,row,col,N):
            board[row][col]=1
            solve_n_queens_util(board, row+1, N, solutions)
            board[row][col]=0

def solve_n_queens(N):
    board=[[0]*N for _ in range(N)]
    solutions=[]
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

def print_solutions(solutions):
    for idx,solution in enumerate(solutions):
        print(f"Solution{idx+1}:")
        for row in solution:
            print(row)
    print()

if __name__=="__main__":
    N=4
    solutions=solve_n_queens(N)
    print(f"Found {len(solutions)} solutions for {N}-Queens problem:")
    print_solutions(solutions)