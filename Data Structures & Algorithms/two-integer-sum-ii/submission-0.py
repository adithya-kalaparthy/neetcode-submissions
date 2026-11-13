class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize the pointers
        left = 0
        right = len(numbers) - 1
        
        # Initialize the loop.
        while left < right:
            total = numbers[left] + numbers[right]

            # If total is greater than the target, then
            # move the right pointer because the left is already
            # at the least most possible value.
            if total > target:
                right -= 1
            # Similarly, if total is less than the target, then
            # move the left pointer because the right is already
            # at the highest possible value.
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]