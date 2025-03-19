import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        create defaultdict(set) for rows, cols and 3xz3 square [r//3, c//3]
        traverse over the board, if '.' contniue else if current elemetn is in
        any dict then return False.
        add every element in rows, cols and sqaures
        """

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key = (r ///3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True
    
# TIme Complexity = O(9^2)