class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = len(board[0])
        rows = len(board)
        sub_boxes = (cols // 3) * (rows // 3) 
        for r in board:
            s = set()
            for i in r:
                if i != "." and i in s:
                    return False
                s.add(i)
        
        for c in range(cols):
            s = set()
            for r in range(rows):
                if board[r][c] != "." and board[r][c] in s:
                    return False
                s.add(board[r][c])


        box = {
            f"{i//3}{j//3}" : set() for i in range(9) for j in range(9)
        }
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "." and board[r][c] in box[f"{r//3}{c//3}"]:
                    return False
                
                box[f"{r//3}{c//3}"].add(board[r][c])
        return True