from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check the rows first for duplicates.
        for row_index in range(len(board)):
            row_set = set()
            for column_index in range(len(board[row_index])):
                if board[row_index][column_index].isdigit():
                    if board[row_index][column_index] in row_set:
                        return False
                    row_set.add(board[row_index][column_index])
        
        # Check the columns for duplicates.
        for column_index in range(9):
            column_set = set()
            for row_index in range(len(board)):
                if board[row_index][column_index].isdigit():
                    if board[row_index][column_index] in column_set:
                        return False
                    column_set.add(board[row_index][column_index])
        
        # Check the boxes.
        for row_box_idx in range(0,9,3):
            for col_box_idx in range(0,9,3):
                box_set = set()
                for row_index in range(row_box_idx, row_box_idx + 3):
                    for col_index in range(col_box_idx, col_box_idx + 3):
                        if board[row_index][col_index].isdigit():
                            if board[row_index][col_index] in box_set:
                                return False
                            box_set.add(board[row_index][col_index])
        
        return True