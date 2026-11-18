class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = 0 if not m else len(matrix[0])

        if not m or not n:
            return False

        top_pointer = 0
        bottom_pointer = m-1

        while top_pointer <= bottom_pointer:
            left = 0
            right = n - 1

            mid_height = (top_pointer + bottom_pointer)//2
            mid_width = (left + right) // 2

            if matrix[mid_height][mid_width] == target:
                return True
            
            if matrix[mid_height][0] <= target <= matrix[mid_height][-1]:
                while left <= right:
                    row_mid_width = (left + right) // 2
                    if matrix[mid_height][row_mid_width] < target:
                        left = row_mid_width + 1
                    elif matrix[mid_height][row_mid_width] > target:
                        right = row_mid_width - 1
                    else:
                        return True
                return False
            
            if matrix[mid_height][mid_width] < target:
                top_pointer = mid_height + 1
            else:
                bottom_pointer = mid_height - 1
        
        return False
            