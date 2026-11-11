class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        output = [1]*num_len
        
        # Calculate the product of all the elements to the left of index
        # and assign it to output.
        prefix = 1
        for i in range(num_len):
            output[i] = prefix
            prefix *= nums[i]
        
        # Calculate the product of all the elements to the right of the
        # index and assign it to the output.
        #   - in order to do that... traverse through the array in reverse.
        #   - Start assigning the suffix multipliers in reverse.
        suffix = 1
        for i in range(num_len - 1, -1 , -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output