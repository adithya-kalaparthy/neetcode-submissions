class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Neetcode largest rectangle area problem.

        The algo is simple. Iterate through each height. Strech
        out hands on left and right side. If the right hand fits
        inside the height to the right, extend the hand until the
        hand no longer fits or until the absolute end.

        Similarly, extend the left hand, if the left hand fits
        inside the height to the left, extend the hand until the
        hand no longer fits or until absolute left end.

        So, the area becomes, width of the hands * height at
        the position.

        Move the position to the right.
        
        Args:
            heights: List of heights.
        """
        max_area = 0
        stack: list[tuple[int, int]] = []  # (start_idx, height)

        for curr_idx, curr_height in enumerate(heights):
            start_idx = curr_idx
            
            while stack and stack[-1][1] > curr_height:
                prev_start_idx, prev_height = stack.pop()
                width = curr_idx - prev_start_idx
                max_area = max(max_area, prev_height * width)
                start_idx = prev_start_idx

            stack.append((start_idx, curr_height))
            
        end_idx = len(heights)
        for start_idx, height in stack:
            width = end_idx - start_idx
            max_area = max(max_area, height * width)

        return max_area