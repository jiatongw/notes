class Solution:
    def solveNQueens(self, n):
        board = [["."] * n for i in range(0, n)]
        
        res = []
        
        self.dfs(board, 0, res)
        
        return res
        
    def dfs(self, board, colindex, res):
        if colindex == len(board):
            res.append(self.construct(board))
            return
        
        # 先走col, 再走row
        for rowindex in range(0, len(board)):
            if self.isvalid(board, rowindex, colindex):
                board[rowindex][colindex] = 'Q'
                self.dfs(board, colindex+1, res)
                board[rowindex][colindex] = '.'
                
    def isvalid(self, board, row, colindex):
        for i in range(0, colindex):
            if board[row][i] == 'Q':
                return False
            
        for i in range(0, row):
            if board[i][colindex] == 'Q':
                return False
        
        for i, j in zip(range(row-1, -1, -1), range(colindex-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # 先走clo后走row, 所以检查的时候，要查当前点的左上和左下
        for i, j in zip(range(row+1, len(board)), range(colindex-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True
    
    def construct(self, board):
        res = []
        
        for i in range(0, len(board)):
            res.append(''.join(board[i]))
        return res

s = Solution()
print(s.solveNQueens(4))