class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            min_height = min(heights[left], heights[right])
            width = right - left
            area = min_height * width

            if max_area < area:
                max_area = area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area 
        