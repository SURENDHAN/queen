from django.shortcuts import render
from .forms import NQueensForm

def solve_n_queens(N):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1  # Backtrack

    solutions = []
    board = [-1] * N
    solve(board, 0)
    return solutions

def nqueens_view(request):
    if request.method == 'POST':
        form = NQueensForm(request.POST)
        if form.is_valid():
            N = form.cleaned_data['number_of_queens']
            solutions = solve_n_queens(N)
            
            # Compute cell colors for the chessboard
            cell_colors = [
                ['white' if (row + col) % 2 == 0 else 'black' for col in range(N)]
                for row in range(N)
            ]
            
            context = {
                'solutions': solutions,
                'N': N,
                'range_N': range(N),
                'cell_colors': cell_colors,
            }
            return render(request, 'cod/nqueens_results.html', context)
    else:
        form = NQueensForm()
    return render(request, 'cod/nqueens_form.html', {'form': form})


