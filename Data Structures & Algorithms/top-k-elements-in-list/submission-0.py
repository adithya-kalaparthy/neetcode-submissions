from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Find the top frequent integers.
        
        Args:
            nums: List of integers
            k: Number of top frequent integers
        """
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        count_key_map = defaultdict(list)
        max_freq = 0
        for key, count in counts.items():
            count_key_map[count].append(key)
            if count > max_freq:
                max_freq = count
        

        output = []
        for freq in range(max_freq, 0, -1):
            if freq in count_key_map:
                output.extend(count_key_map[freq])
                if len(output) >= k:
                    return output[:k]
