# HW - Nested List - Tic Tac Toe Game

class TicTacToe:
    def __init__(self, N):
        if N < 3:
            raise Exception("The width of the grid must be positive and greater than 3")
        self.N = N
        self.grid = [[None for _ in range(N)] for _ in range(N)]

    def print_grid(self):
        for i in range(self.N):
            for j in range(self.N):
                cell = self.grid[i][j] if self.grid[i][j] is not None else ' '
                print(cell, end=' ')
                if j != self.N - 1:
                    print('|', end=' ')
            print()
            if i != self.N - 1:
                print('-' * (self.N * 4 - 3))

    def is_winner(self):
        for i in range(self.N):
            if all(self.grid[i][j] == 'X' for j in range(self.N)):
                return "Player X won!"
            if all(self.grid[i][j] == 'O' for j in range(self.N)):
                return "Player O won!"
            if all(self.grid[j][i] == 'X' for j in range(self.N)):
                return "Player X won!"
            if all(self.grid[j][i] == 'O' for j in range(self.N)):
                return "Player O won!"

        if all(self.grid[i][i] == 'X' for i in range(self.N)) or all(self.grid[i][self.N - i - 1] == 'X' for i in range(self.N)):
            return "Player X won!"
        if all(self.grid[i][i] == 'O' for i in range(self.N)) or all(self.grid[i][self.N - i - 1] == 'O' for i in range(self.N)):
            return "Player O won!"

        if all(cell is not None for row in self.grid for cell in row):
            return "Tie!"

        return ""

    def move(self, role):
        symbol = 'X' if role == 1 else 'O'
        while True:
            try:
                a, b = map(int, input(f'Player {symbol}, make a move (row col): ').split())
                if a < 1 or a > self.N or b < 1 or b > self.N or self.grid[a - 1][b - 1] is not None:
                    raise ValueError
                self.grid[a - 1][b - 1] = symbol
                break
            except ValueError:
                print("Invalid location or cell already occupied. Try again.")

if __name__ == '__main__':
    n = int(input('Enter grid size: '))
    tic = TicTacToe(n)
    role = 1
    while True:
        tic.print_grid()
        tic.move(role)
        winner = tic.is_winner()
        if winner:
            tic.print_grid()
            print(winner)
            break
        role *= -1

"""

3
1 1
1 2
2 2
1 3
3 3
X|O|O
 |X| 
 | |X
Play X won!

3
1 1
1 2
2 1
2 2
3 3
3 2
X|O| 
X|O| 
 |O|X
Play O won!

3
1 3
1 1
2 2
3 3
3 1
O| |X
 |X| 
X| |O
Play X won!

3
1 1
1 3
1 2
2 2
3 2
2 1
2 3
3 3
3 1
X|X|O
O|O|X
X|X|O
Tie!
"""