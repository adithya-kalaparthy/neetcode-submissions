from math import ceil
class Solution:
    def _total_hours_at_speed(self, piles: list[int], speed: int) -> int:
        total_hrs = 0
        for i in piles:
            total_hrs += ceil(i/speed) 

        return total_hrs

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        # At speed = max(piles), every pile takes 1 hour (total = len(piles))
        if len(piles) == h:
            return right

        final_speed = right
        while left <= right:
            mid = (left + right) // 2
            if self._total_hours_at_speed(piles, mid) <= h:
                final_speed = mid
                right = mid - 1
            else:
                left = mid + 1

        return final_speed
        
        