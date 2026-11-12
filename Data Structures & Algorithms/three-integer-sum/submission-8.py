class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            # Skip duplicate anchor values.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return output
