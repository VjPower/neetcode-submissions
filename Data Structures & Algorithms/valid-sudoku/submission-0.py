class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        block_list = [set() for _ in range(9)]
        row_list = [set() for _ in range(9)]
        column_list = [set() for _ in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                if (board[i][j]!="."):
                    
                    if board[i][j] in row_list[i]:
                        return False
                    if board[i][j] in column_list[j]:
                        return False 

                    x = i//3
                    y = j//3
                    block_no = x*3 + y
                    if board[i][j] in block_list[block_no]:
                        return False

                    row_list[i].add(board[i][j])
                    column_list[j].add(board[i][j])
                    block_list[block_no].add(board[i][j])

        return True