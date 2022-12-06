class Board():
    
    def __init__(self, code=None):
        self.__resetBoard()

        #If there is a code for the sudoku board provided, fill in the sodoku grid as intended
        self.code = code
        if code:
            for row in range(9):
                for col in range(9):
                    self.board[row][col] = int(code[0])
                    code = code[1:]

    # Method to reset the board to an empty state
    def __resetBoard(self):
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        return self.board
   
    # Method for converting a board to a code so that it can be saved or reused.
    def boardToCode(self, input_board=None):
        if input_board:
            _code = ''.join([str(i) for j in input_board for i in j])
            return _code

        else:
            self.code = ''.join([str(i) for j in self.board for i in j])
            return self.code

    # Method for finding the next empty square (0)
    def findEmptySquare(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return(row, col)
        
        return False

    # Method for checking if a value fits a square
    def checkSpace(self, num, space): # num = num to check and space = tuple with col + row
        # Cases that return false to stop check:
        if not self.board[space[0]][space[1]] == 0: # check to see if space has a number already
            return False

        for col in self.board[space[0]]:  # check if number in row
            if col == num:
                return False

        for row in range(len(self.board)): # check if number in column
            if self.board[row][space[1]] == num:
                return False
        
        # Get the current box row/column (3 boxes in row/col so get remainder of overall col/row when dividing by 3)
        _boxRow = space[0] // 3
        _boxCol = space[1] // 3

        for i in range(3): # check box
            for j in range(3):
                if self.board[i + (_boxRow * 3)][j + (_boxCol * 3)] == num:
                    return False
        
        return True

    def solve(self):
        spaces = self.findEmptySquare()

        if not spaces:
            return True
        else:
            row, col = spaces

        for n in range(1, 10):
            if self.checkSpace(n, (row, col)):
                self.board[row][col] = n

                if self.solve():
                    return self.board
                
                self.board[row][col] = 0
        
        return False

def main():
    # 0 in place for unknown numbers on sudoku board.
    sudoku1 = Board()
    sudoku1.board = [
                [0, 1, 0, 2, 0, 0, 9, 4, 3],
                [0, 2, 0, 0, 0, 0, 0, 0, 6],
                [4, 0, 0, 0, 0, 5, 0, 0, 0],
                [0, 9, 0, 0, 8, 0, 0, 0, 0],
                [3, 0, 0, 1, 2, 6, 0, 0, 7],
                [0, 0, 0, 0, 9, 0, 0, 2, 0],
                [0, 0, 0, 6, 0, 0, 0, 0, 2],
                [7, 0, 0, 0, 0, 0, 0, 8, 0],
                [1, 8, 6, 0, 0, 2, 0, 5, 0],
            ]

    sudoku1.solve()
    print(sudoku1.board)

if __name__ == '__main__':
    main()