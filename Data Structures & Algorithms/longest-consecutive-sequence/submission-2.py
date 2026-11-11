from typing import List


class Solution:

  def longestConsecutive(self, nums: List[int]) -> int:
    # 1. Guard against empty input
    if not nums:
      return 0

    # 2. Use a set for O(1) presence lookups (replaces count_map)
    num_set = set(nums)
    output_seq = []

    for num in num_set:
      # 3. Only start building if 'num' is the beginning of a sequence
      if (num - 1) not in num_set:
        curr_seq = []
        curr_val = num

        # 4. Expand forward as long as consecutive numbers exist
        while curr_val in num_set:
          curr_seq.append(curr_val)
          curr_val += 1

        # 5. Update best sequence found so far
        if len(curr_seq) > len(output_seq):
          output_seq = curr_seq

    return len(output_seq)