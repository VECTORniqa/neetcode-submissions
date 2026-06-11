class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            s = set()
            for col in range(9):
                if board[row][col] in s:
                    return False
                elif board[row][col] != ".":
                    s.add(board[row][col])
        
        for row in range(9):
            s = set()
            for col in range(9):
                if board[col][row] in s:
                    return False
                elif board[col][row] != ".":
                    s.add(board[col][row])
        
        x = [(0,0) , (0,3), (0, 6),
        (3,0) , (3,3), (3,6),
        (6,0) , (6,3), (6, 6)]

        for i, j in x:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != ".":
                        s.add(item)
        
        return True
        
        
        


                    